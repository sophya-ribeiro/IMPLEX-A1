import bubble_sort
import counting_sort
import heap_sort
import quick_sort
import insertion_sort
import merge_sort

import time
import matplotlib.pyplot as plt

#-------Funções auxiliares-------#

def ler_arquivo(nome_arquivo: str):
    try:
        with open(nome_arquivo, 'r') as arquivo:
            linhas = arquivo.readlines()
            numeros = [int(linha.strip()) for linha in linhas]
        return numeros
    except FileNotFoundError:
        print("Erro: Arquivo '{}' não encontrado.".format(nome_arquivo))
        return None

#----------Main----------#

def main():
    nome_arquivo = 'mil.txt'
    vetor = ler_arquivo(nome_arquivo)

    start = time.time()
    heap_sort.heap_sort(vetor)
    end = time.time()

    print()
    print(f"Tempo de execução HEAP SORT: {end-start:.6f}")
    print()

    vetor = ler_arquivo(nome_arquivo)
    start = time.time()
    insertion_sort.insertion_sort(vetor)
    end = time.time()

    print(f"Tempo de execução INSERTION SORT: {end-start:.6f}")
    print()

    vetor = ler_arquivo(nome_arquivo)
    tam_vetor = len(vetor)

    start = time.time()
    quick_sort.quick_sort(vetor, 0, tam_vetor-1)
    end = time.time()

    print(f"Tempo de execução QUICK SORT: {end-start:.6f}")
    print()

    vetor = ler_arquivo(nome_arquivo)
    start = time.time()
    merge_sort.merge_sort(vetor, 0, len(vetor) -1)
    end = time.time()

    print(f"Tempo de execução MERGE SORT: {end-start:.6f}")
    print()

    vetor = ler_arquivo(nome_arquivo)
    start = time.time()
    bubble_sort.bubble_sort(vetor, len(vetor))
    end = time.time()

    print(f"Tempo de execução BUBBLE SORT: {end-start:.6f}")
    print()

    vetor = ler_arquivo(nome_arquivo)
    start = time.time()
    array_ordered = [0 for _ in range(len(vetor))]
    counting_sort.counting_sort(vetor, array_ordered, max(vetor))
    end = time.time()

    print(f"Tempo de execução COUNTING SORT: {end-start:.6f}")
    print()


main()