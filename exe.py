import bubble_sort
import counting_sort
import heap_sort
import quick_sort
import insertion_sort
import merge_sort

import time
import matplotlib.pyplot as plt
import numpy as np

#-------Funções auxiliares-------#

def ler_arquivo(nome_arquivo: str):
    try:
        with open(nome_arquivo, 'r') as arquivo:
            linhas = arquivo.readlines()
            numeros = [int(linha.strip()) for linha in linhas]
        return numeros
    except FileNotFoundError:
        print(f"Erro: Arquivo '{nome_arquivo}' não encontrado.")

def salvar_em_arquivo(tamanhos, tempos_bubble, tempos_insertion, tempos_merge, tempos_quick, tempos_heap, tempos_counting):
    with open('saida.txt', 'w') as file:
        file.write(f"{'Tamanho':<10}{'Bubble':<10}{'Insertion':<10}{'Merge':<10}{'Quick':<10}{'Heap':<10}{'Counting':<10}\n")
        for i in range(len(tamanhos)):
            file.write(f"{tamanhos[i]:<10}{tempos_bubble[i]:<10.6f}{tempos_insertion[i]:<10.6f}{tempos_merge[i]:<10.6f}{tempos_quick[i]:<10.6f}{tempos_heap[i]:<10.6f}{tempos_counting[i]:<10.6f}\n")
        

def medir_tempo(func, array):
    inicio = time.time()
    func(array)
    fim = time.time()
    return fim - inicio

def gerar_tabela_comparacao(vetores_nomes):
    # print(f"{'Tamanho':<10}{'Bubble':<10}{'Insertion':<10}")
    print(f"{'Tamanho':<10}{'Bubble':<10}{'Insertion':<10}{'Merge':<10}{'Quick':<10}{'Heap':<10}{'Counting':<10}")

    tempos_bubble = []
    tempos_insertion = []
    tempos_merge = []
    tempos_quick = []
    tempos_heap = []
    tempos_counting = []
    tamanhos = []

    for nome_arquivo in vetores_nomes:
        vetor = ler_arquivo(nome_arquivo)
        tamanho = len(vetor)
        max_value = max(vetor)

        tempos = [
            medir_tempo(lambda arr: bubble_sort.bubble_sort(arr.copy(), len(arr)), vetor),
            medir_tempo(lambda arr: insertion_sort.insertion_sort(arr.copy()), vetor),
            medir_tempo(lambda arr: merge_sort.merge_sort(arr.copy(), 0, len(arr) - 1), vetor),
            medir_tempo(lambda arr: quick_sort.quick_sort(arr.copy(), 0, len(arr) - 1), vetor),
            medir_tempo(lambda arr: heap_sort.heap_sort(arr.copy()), vetor),
            medir_tempo(lambda arr: counting_sort.counting_sort(arr.copy(), [0] * len(arr), max_value), vetor)
        ]

        tempos_bubble.append(tempos[0])
        tempos_insertion.append(tempos[1])
        tempos_merge.append(tempos[2])
        tempos_quick.append(tempos[3])
        tempos_heap.append(tempos[4])
        tempos_counting.append(tempos[5])
        tamanhos.append(tamanho)

        salvar_em_arquivo(tamanhos, tempos_bubble, tempos_insertion, tempos_merge, tempos_quick, tempos_heap, tempos_counting)
        print(f"{tamanho:<10}" + "".join([f"{tempo:<10.6f}" for tempo in tempos]))

    # return tamanhos, tempos_bubble, tempos_insertion
    return tamanhos, tempos_counting, tempos_bubble, tempos_insertion, tempos_merge, tempos_quick, tempos_heap 

#----------Main----------#

def main():

    print()
    vetores_nomes = ['Dados/mil.txt', 'Dados/doismil.txt', 'Dados/tresmil.txt', 'Dados/quatromil.txt', 'Dados/cincomil.txt']
    # tamanhos, tempos_bubble, tempos_insertion = gerar_tabela_comparacao(vetores_nomes)
    tamanhos, tempos_bubble, tempos_insertion, tempos_merge, tempos_quick, tempos_heap, tempos_counting = gerar_tabela_comparacao(vetores_nomes)
    print()

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
    ax.set_title('Vetor aleatório')
    ax.legend()
    ax.grid(True)

    plt.show()

if __name__ == '__main__':
    main()
