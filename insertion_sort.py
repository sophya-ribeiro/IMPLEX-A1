# -*- coding: utf-8 -*-

"""
Algoritmo de ordenação por Max-Heap

"""
    
def insertion_sort(vetor: list):
    
    for j in range(len(vetor)):
        chave = vetor[j]
        i = j - 1
        
        while i >= 0 and vetor[i] > chave:
            vetor[i + 1] = vetor[i]
            i = i - 1
        
        vetor[i + 1] = chave
