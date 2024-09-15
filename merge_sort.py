# -*- coding: utf-8 -*-
# Estudantes: Sophya Ribeiro e Soraya Ferreira

import sys
import math

def merge(Array: list, p: int, q: int, r: int):
    """
    Esta função realiza a mescla ordenada de elementos dentro
    de um vetor. Recebe o vetor (array) e três índices (p, q, r) que 
    delimitam os subvetores que serão criados.
    """

    size1 = q - p + 1 # número de elementos no subvetor da esquerda
    size2 = r - q # número de elementos no subvetor da direira
    
    Left = [0 for item in range(0, size1)]
    Right = [0 for item in range(0, size2)]

    for i in range(0, size1):
        Left[i] = Array[p + i]

    for j in range(0, size2):
        Right[j] = Array[q + j + 1]
    
    Left.append(float('inf'))
    Right.append(float('inf'))

    i = 0
    j = 0

    for k in range(p, r + 1):
        if Left[i] <= Right[j]:
            Array[k] = Left[i]
            i += 1
        else:
            Array[k] = Right[j]
            j += 1 

def merge_sort(Array: list, p: int, r: int):
    """
    Algoritmo recursivo de ordenação Merge Sort. 
    Recebe um vetor a ordenar de modo crescente (Array)
    e os índices dos subvetores que serão criados ao longo
    do algoritmo, 'p' é o índice inicial, e 'r' é o índice final.
    """
    #Se houver ao menos 2 elementos no vetor
    if p < r:
        q = (p + r) // 2 # tamanho do vetor dividido por 2
        merge_sort(Array, p, q)
        merge_sort(Array, q + 1, r)
        merge(Array, p, q, r)

def main():
    """
    Função criada apenas para testes do algoritmo 
    de ordenação Merge Sort.
    """

    file_name = sys.argv[1]

    try:
        with open(file_name, 'r') as file:
            lines = file.readlines()
            #Caso de list comprehension
            numbers = [int(line.strip()) for line in lines]
            
        merge_sort(numbers, 0, len(numbers) -1)

        for index in range(0, len(numbers)-1):
            print(f"{numbers[index]} ", end='')
        print(f"{numbers[len(numbers)-1]}")

    except FileNotFoundError:
        print("Erro: Arquivo '{}' não encontrado.".format(file_name))

if __name__ == "__main__":
    main()