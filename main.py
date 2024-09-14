import bubble_sort
import counting_sort
import heap_sort
import quick_sort
import insertion_sort
import merge_sort

import random
import math
import sys
import time

import matplotlib.pyplot as plt
import numpy as np


#-------Funções auxiliares-------#

def gerar_numeros_aleatorios(n: int) -> list:
 
    # 'n' limitação para manter o tempo do counting sort linear
    numeros = [random.randint(0, n) for _ in range(n)]
    return numeros

  
def gerar_vetor_quase_ordenado(n: int) -> list:
    numeros = [random.randint(0, n) for _ in range(n)]

    numeros.sort()

    i_toshuffle = [random.randint(0, n-1) for _ in range(math.ceil(0.1 * n))]
    #lista de índices das posições que serão trocadas 

    for i in range(0, len(i_toshuffle)):
        numeros[i_toshuffle[i]] = random.randint(0, n)

    return numeros


def gerar_grafico(tamanhos, tempos_bubble, tempos_insertion, tempos_merge, tempos_quick, tempos_heap, tempos_counting, escolha: int):
    fig, ax = plt.subplots()

    ax.plot(tamanhos, tempos_bubble, label='Bubble', marker='o')
    ax.plot(tamanhos, tempos_insertion, label='Insertion', marker='o')
    ax.plot(tamanhos, tempos_merge, label='Merge', marker='o')
    ax.plot(tamanhos, tempos_quick, label='Quick', marker='o')
    ax.plot(tamanhos, tempos_heap, label='Heap', marker='o')
    ax.plot(tamanhos, tempos_counting, label='Counting', marker='o')

    xticks_interval = 500
    xticks = np.arange(min(tamanhos), max(tamanhos) + xticks_interval, xticks_interval)
    ax.set_xticks(xticks)

    ax.set_xlabel('Tamanho do Vetor')
    ax.set_ylabel('Tempo de Execução (segundos)')

    if escolha == 1 :
        ax.set_title('[[RANDOM]]')
    elif escolha == 2:
        ax.set_title('[[NEARLY SORTED]]')
    elif escolha == 3:
        ax.set_title('[[SORTED]]')
    else:
        # Se a escolha for 4
        ax.set_title('[[REVERSE]]')
    ax.legend()
    ax.grid(True)

    plt.show()

def testar_vetor_aleatorio(fim: int, inc: int, stp: int):
    rpt = int(input("\tParâmetro rpt (número de repetições para média): "))

    print()
    print(f"{'Tamanho':<10}{'Bubble':<10}{'Insertion':<10}{'Merge':<10}{'Heap':<10}{'Quick':<10}{'Counting':<10}")

    # É o número de pontos de medição que o gráfico deverá apresentar
    n_pontos = ((fim - inc) // stp)+ 1

    # Aqui são as listas de testes, em cada posição haverá a média dos tempos de execução 
    tempos_bubble = [0.0] * n_pontos
    tempos_insertion = [0.0] * n_pontos
    tempos_heap = [0.0] * n_pontos
    tempos_quick = [0.0] * n_pontos
    tempos_merge = [0.0] * n_pontos
    tempos_counting = [0.0] * n_pontos
    tamanhos = []

    indice_tempos = 0 # iterador para percorrer o número de pontos de medição

    for n in range(inc, fim + 1, stp):
        """
        Soma os valores de tamanho dos vetores para teste, a partir dos quais será construído o gráfico.
        Em outras palavras, percorre os pontos de medição, em que 'n' assume o tamanho atual do vetor.
        """
        tamanhos.append(n)
        
        for _ in range(0, rpt):
            """
            Roda o número de casos de teste para o vetor aleatório, a fim de obter, 
            ao final, uma média dos tempos de execução de cada algoritmo.
            """
            vetor = gerar_numeros_aleatorios(n)

            #cópias do vetor gerado aleatóriamente para passagem como parâmetro para cada algoritmo de ordenação
            copia_bubble = vetor.copy()
            copia_insertion = vetor.copy()
            copia_heap = vetor.copy()
            copia_merge = vetor.copy()
            copia_quick = vetor.copy()
            copia_counting = vetor.copy()

            # Medindo tempo do BUBBLE SORT
            start = time.time()
            bubble_sort.bubble_sort(copia_bubble, len(copia_bubble))
            end = time.time()
            tempos_bubble[indice_tempos] += (end - start)

            # Medindo tempo do INSERTION SORT
            start = time.time()
            insertion_sort.insertion_sort(copia_insertion)
            end = time.time()
            tempos_insertion[indice_tempos] += (end - start)

            # Medindo tempos do HEAP SORT
            start = time.time()
            heap_sort.heap_sort(copia_heap)
            end = time.time()
            tempos_heap[indice_tempos] += (end - start)

            # Medindo tempo do MERGE SORT
            start = time.time()
            merge_sort.merge_sort(copia_merge, 0, len(copia_merge) -1)
            end = time.time()
            tempos_merge[indice_tempos] += (end - start)

            # Medindo tempo do QUICK SORT
            start = time.time()
            quick_sort.quick_sort(copia_quick, 0, len(copia_quick)-1)
            end = time.time()
            tempos_quick[indice_tempos] += (end - start)

            # Medindo tempo do COUNTING SORT
            start = time.time()
            array_ordered = [0 for _ in range(len(copia_counting))]
            max_value = max(copia_counting)
            counting_sort.counting_sort(copia_counting, array_ordered, max_value)
            end = time.time()
            tempos_counting[indice_tempos] += (end - start)
        
        # Coloca a média na posição corresponde da lista de testes, conforme o tamanho do vetor utilizado.
        tempos_bubble[indice_tempos] /= rpt
        tempos_insertion[indice_tempos] /= rpt
        tempos_heap[indice_tempos] /= rpt
        tempos_quick[indice_tempos] /= rpt
        tempos_merge[indice_tempos] /= rpt
        tempos_counting[indice_tempos] /= rpt 

        print(f"{n:<10}{tempos_bubble[indice_tempos]:<10.6f}{tempos_insertion[indice_tempos]:<10.6f}{tempos_merge[indice_tempos]:<10.6f}{tempos_heap[indice_tempos]:<10.6f}{tempos_quick[indice_tempos]:<10.6f}{tempos_counting[indice_tempos]:<10.6f}")

        indice_tempos += 1

    gerar_grafico(tamanhos, tempos_bubble, tempos_insertion, tempos_merge, tempos_quick, tempos_heap, tempos_counting, 1)
    print()



def testar_caso_unico(fim: int, inc: int, stp: int, escolha: int):
    """
    Gera os testes para cada caso que não necessita de repetições para
    realizar uma média de tempos.
    """
    print()
    print(f"{'Tamanho':<10}{'Bubble':<10}{'Insertion':<10}{'Merge':<10}{'Heap':<10}{'Quick':<10}{'Counting':<10}")

    # É o número de pontos de medição que o gráfico deverá apresentar
    n_pontos = ((fim - inc) // stp)+ 1

    # Aqui são as listas de testes, em cada posição haverá o tempo de execução de um algoritmo 
    tempos_bubble = [0.0] * n_pontos
    tempos_insertion = [0.0] * n_pontos
    tempos_heap = [0.0] * n_pontos
    tempos_quick = [0.0] * n_pontos
    tempos_merge = [0.0] * n_pontos
    tempos_counting = [0.0] * n_pontos
    tamanhos = []

    indice_tempos = 0 # iterador para percorrer o número de pontos de medição

    for n in range(inc, fim + 1, stp):
        """
        Soma os valores de tamanho dos vetores para teste, a partir dos quais será construído o gráfico.
        Em outras palavras, percorre os pontos de medição, em que 'n' assume o tamanho atual do vetor.
        """

        tamanhos.append(n)
        

        if escolha == 2:
            # recebe um vetor com 10% de seus valores embaralhados entre si.
            vetor = gerar_vetor_quase_ordenado(n)
            
        elif escolha == 3:
            #vetor = (gerar_numeros_aleatorios(n)).sort()

            # Os valores gerados aqui podem começar em 0
            vetor = [value for value in range(0, n+1)]
            # if(indice_tempos == 0 or indice_tempos == 1):
            #     print(vetor)

        else: 
            #vetor = (gerar_numeros_aleatorios(n)).sort(reverse=True)

            
            # Gera o vetor decrescente
            vetor = [value for value in range(n, 0, -1)]
            # if(indice_tempos == 0 or indice_tempos == 1):
            #     print(vetor)

        #cópias do vetor gerado aleatóriamente para passagem como parâmetro para cada algoritmo de ordenação
        copia_bubble = vetor.copy()
        copia_insertion = vetor.copy()
        copia_heap = vetor.copy()
        copia_merge = vetor.copy()
        copia_quick = vetor.copy()
        copia_counting = vetor.copy()

        # Medindo tempo do BUBBLE SORT
        start = time.time()
        bubble_sort.bubble_sort(copia_bubble, len(copia_bubble))
        end = time.time()
        tempos_bubble[indice_tempos] += (end - start)

        # Medindo tempo do INSERTION SORT
        start = time.time()
        insertion_sort.insertion_sort(copia_insertion)
        end = time.time()
        tempos_insertion[indice_tempos] += (end - start)

        # Medindo tempos do HEAP SORT
        start = time.time()
        heap_sort.heap_sort(copia_heap)
        end = time.time()
        tempos_heap[indice_tempos] += (end - start)

        # Medindo tempo do MERGE SORT
        start = time.time()
        merge_sort.merge_sort(copia_merge, 0, len(copia_merge) -1)
        end = time.time()
        tempos_merge[indice_tempos] += (end - start)

        # Medindo tempo do QUICK SORT
        start = time.time()
        quick_sort.quick_sort(copia_quick, 0, len(copia_quick)-1)
        end = time.time()
        tempos_quick[indice_tempos] += (end - start)

        # Medindo tempo do COUNTING SORT
        start = time.time()
        array_ordered = [0 for _ in range(len(copia_counting))]
        max_value = max(copia_counting)
        counting_sort.counting_sort(copia_counting, array_ordered, max_value)
        end = time.time()
        tempos_counting[indice_tempos] += (end - start)
        
        print(f"{tempos_insertion[indice_tempos]:<10.6f}{tempos_merge[indice_tempos]:<10.6f}{tempos_heap[indice_tempos]:<10.6f}{tempos_quick[indice_tempos]:<10.6f}{tempos_counting[indice_tempos]:<10.6f}")

        indice_tempos += 1

    gerar_grafico(tamanhos, tempos_bubble, tempos_insertion, tempos_merge, tempos_quick, tempos_heap, tempos_counting, escolha)
    print()

#----------- MAIN -----------#

def main():

    sys.setrecursionlimit(100000)

    print("\n\
          \t[1] Testar caso vetor aleatório;\n\
           \t[2] Testar caso vetor quase ordenado;\n\
           \t[3] Testar caso vetor ordenado crescentemente;\n\
           \t[4] Testar caso vetor ordenado decrescentemente;\n\
           Escolha: ", end='')   
    escolha = int(input())

    inc = int(input("\tParâmetro inc (tamanho inicial do vetor): "))
    fim = int(input("\tParâmetro fim (tamanho final do vetor): "))
    stp = int(input("\tParâmetro stp (intervalos entre os tamanhos): "))

    if escolha == 1:
        testar_vetor_aleatorio(fim, inc, stp)

    elif escolha == 2:
        testar_caso_unico(fim, inc, stp, 2)

    elif escolha == 3:
        testar_caso_unico(fim, inc, stp, 3)

    elif escolha == 4:
        testar_caso_unico(fim, inc, stp, 4)

    else:
        print("Escolha inválida!")
           

if __name__ == '__main__':
    main()