# -*- coding: utf-8 -*-

"""
Algoritmo de ordenação por Max-Heap

"""
#--------imports--------#

import sys
from typing import List, Optional

#-------funções principais-------#

def pai(i: int):
    return (i - 1) // 2

def filho_esquerdo(i: int):
    return 2 * i + 1

def filho_direito(i: int):
    return 2 * i + 1 + 1

def ajusta_max_heap(vetor: list, i: int, tam_heap: int):
    esq = filho_esquerdo(i)  # l
    dir = filho_direito(i)   # r

    if esq < tam_heap and vetor[esq] > vetor[i]:
        maior = esq
    else:
        maior = i

    if dir < tam_heap and vetor[dir] > vetor[maior]:
        maior = dir

    if maior != i:
        vetor[i], vetor[maior] = vetor[maior], vetor[i]
        ajusta_max_heap(vetor, maior, tam_heap)

def constroi_max_heap(vetor: List[int], tam_heap: int):
    for i in range(tam_heap // 2 - 1, -1, -1):
        ajusta_max_heap(vetor, i, tam_heap)

def heap_sort(vetor: list):
    tam_heap = len(vetor)
    constroi_max_heap(vetor, tam_heap)
    
    for i in range(tam_heap - 1, 0, -1):
        vetor[0], vetor[i] = vetor[i], vetor[0]
        ajusta_max_heap(vetor, 0, i)

#-------funções auxiliares-------#

def ler_arquivo(nome_arquivo: str):
    try:
        with open(nome_arquivo, 'r') as arquivo:
            linhas = arquivo.readlines()
            numeros = [int(linha.strip()) for linha in linhas]
        return numeros
    except FileNotFoundError:
        print("Erro: Arquivo '{}' não encontrado.".format(nome_arquivo))
        return None

def imprimir_vetor(vetor: list):
    if vetor:
        print(" ".join(str(numero) for numero in vetor))
    else:
        print("O vetor está vazio.")

#--------main--------#

def main():

    nome_arquivo = sys.argv[1]
    vetor = ler_arquivo(nome_arquivo)

    print("\nVetor nominal: ")
    imprimir_vetor(vetor)
    print("\n")

    heap_sort(vetor)

    print("Vetor ordenado: ")
    imprimir_vetor(vetor)
    print("\n")

if __name__ == '__main__':
    main()
