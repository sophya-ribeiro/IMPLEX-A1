import bubble_sort
import counting_sort
import heap_sort
import quick_sort
import insertion_sort
import merge_sort
import random
import math
import time


#-------Funções auxiliares-------#

def gerar_numeros_aleatorios(n: int) -> list:
 
    # 'n**2' limitação para manter o tempo do counting sort linear
    numeros = [random.randint(1, n**2) for _ in range(n)]
    return numeros

  
def gerar_vetor_quase_ordenado(n: int) -> list:
    numeros = [random.randint(1, n**2) for _ in range(n)]

    numeros.sort()

    i_toshuffle = [random.randint(1, n) for _ in range(math.ceil(0.1 * n))]
    #lista de índices das posições que serão trocadas 

    for i in range(0, len(i_toshuffle)):
        numeros[i_toshuffle[i]] = random.randint(1, n**2)

    return numeros


#----------- MAIN -----------#

def main():


    print("\t[1] Testar caso vetor aleatório;\
           \t[2] Testar caso vetor quase ordenado;\
           \t[3] Testar caso vetor ordenado crescentemente;\
           \t[4] Testar caso vetor ordenado decrescentemente;\
           Escolha: ", end='')   
    escolha = int(input())

    inc = int(input("\tParâmetro inc (tamanho inicial do vetor): "))
    fim = int(input("\tParâmetro fim (tamanho final do vetor): "))
    stp = int(input("\tParâmetro str (intervalos entre os tamanhos): "))

    if escolha == 1:
        rpt = int(input("\tParâmetro rpt (número de repetições para média): "))

        for caso in range(0, rpt):
            for n in range(inc, fim + 1, stp):
                vetor = gerar_numeros_aleatorios(n)

                #cópias do vetor gerado aleatóriamente para passagem como parâmetro para cada algoritmo de ordenação
                copia_bubble, copia_insertion, copia_heap, copia_merge, copia_quick, copia_counting = vetor.copy()

                

                




if __name__ == '__main__':
    main()
