# -*- coding: utf-8 -*-

"""
Algoritmo de ordenação por Max-Heap

"""
#--------imports--------#

import sys
from typing import List, Optional

#-------funções principais-------#

def particionar(vetor, p, r):
    x = vetor[r]
    i = p - 1

    for j in range(p, r):
        if vetor[j] <= x:
            i = i+1
            aux = vetor[i]
            vetor[i] = vetor[j]
            vetor[j] = aux
    
    aux = vetor[i+1]
    vetor[i+1] = vetor[r]
    vetor[r] = aux

    return i+1

def quick_sort(vetor, p, r):
    if p < r:
        q = particionar(vetor, p, r)
        quick_sort(vetor, p, q-1)
        quick_sort(vetor, q+1, r)


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

    tam_vetor = len(vetor)
    quick_sort(vetor, 0, tam_vetor-1)

    print("Vetor ordenado: ")
    imprimir_vetor(vetor)
    print("\n")

if __name__ == '__main__':
    main()
