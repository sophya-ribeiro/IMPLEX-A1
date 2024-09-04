# -*- coding: utf-8 -*-

"""
Algoritmo de ordenação por Max-Heap

"""
#--------imports--------#

import sys
from typing import List, Optional

#-------funções principais-------#

# def insertion_sort(vetor: list):
    
#     for j in range(len(vetor)):
#         chave = vetor[j]
#         i = j - 1
        
# 		while i > 0 and vetor[i] > chave:
# 			vetor[i+1] = vetor[i]
#             i = i -1
        
# 		vetor[i+1] = chave
        
def insertion_sort(vetor: list):
    
    for j in range(len(vetor)):
        chave = vetor[j]
        i = j - 1
        
        while i >= 0 and vetor[i] > chave:
            vetor[i + 1] = vetor[i]
            i = i - 1
        
        vetor[i + 1] = chave


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

    insertion_sort(vetor)

    print("Vetor ordenado: ")
    imprimir_vetor(vetor)
    print("\n")

if __name__ == '__main__':
    main()