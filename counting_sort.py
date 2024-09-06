# -*- coding: utf-8 -*-
import sys


def counting_sort(array: list, array_ordered: list, max_value: int):
    """
    Algoritmo de ordenação Counting Sort.
    Esta função ordena um vetor (array) de modo crescente.
    Recebe o VALORES.
    """
    aux_array = [0 for _ in range(max_value)]

    for index in range(0, len(array)):
        aux_array[array[index]] = aux_array[array[index]] + 1

    for i in range(1, max_value):
        aux_array[i] = aux_array[i] + aux_array[i -1]
    
    for j in range(len(array)-1, -1, -1):
        array_ordered[aux_array[array[j]]] = array[j]
        aux_array[array[j]] = aux_array[array[j]] - 1
     

def main():
    """
    Função criada apenas para testes do algoritmo 
    de ordenação Counting Sort.
    """

    file_name = sys.argv[1]

    try:
        with open(file_name, 'r') as file:
            lines = file.readlines()
            #Caso de list comprehension
            numbers = [int(line.strip()) for line in lines]
            
        array_ordered = [0 for _ in range(len(numbers))]
        counting_sort(numbers, array_ordered, max(numbers))
        print(array_ordered)
        

    except FileNotFoundError:
        print("Erro: Arquivo '{}' não encontrado.".format(file_name))


if __name__ == '__main__':
    main()