# -*- coding: utf-8 -*-
import sys


def counting_sort():
    """
    Algoritmo de ordenação Counting Sort.
    Esta função ordena um vetor (array) de modo crescente.
    Recebe o VALORES.
    """
    pass



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
            
        counting_sort()

        '''
        for index in range(0, len(numbers)-1):
            print(f"{numbers[index]} ", end='')
        print(f"{numbers[len(numbers)-1]}")
        '''

    except FileNotFoundError:
        print("Erro: Arquivo '{}' não encontrado.".format(file_name))

if __name__ == "__main__":
    main()