# -*- coding: utf-8 -*-

import sys

def swap_values(index1: int, index2: int, array: list):
    """
    Função que realiza a troca de posição entre dois valores
    presentes nas posições index1 e index2 de um vetor.
    """
    
    
    backup = array[index1]
    array[index1] = array[index2]
    array[index2] = backup

def bubble_sort(array: list, size_array: int):
    """
    Algoritmo de ordenação Bubble Sort.
    Esta função ordena um vetor (array) de modo crescente.
    Recebe o vetor e o tamanho do vetor.
    """
    
    for i in range(0, size_array-1):
        for j in range(0, size_array-1):
            if array[j] > array[j+1]:
                swap_values(j,j+1, array)

def main():
    """
    Função criada apenas para testes do algoritmo 
    de ordenação Bubble sort.
    """

    file_name = sys.argv[1]

    try:
        with open(file_name, 'r') as file:
            lines = file.readlines()
            #Caso de list comprehension
            numbers = [int(line.strip()) for line in lines]
            
        bubble_sort(numbers, len(numbers))

        for index in range(0, len(numbers)-1):
            print(f"{numbers[index]} ", end='')
        print(f"{numbers[len(numbers)-1]}")

    except FileNotFoundError:
        print("Erro: Arquivo '{}' não encontrado.".format(file_name))

if __name__ == "__main__":
    main()