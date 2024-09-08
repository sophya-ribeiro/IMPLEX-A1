# -*- coding: utf-8 -*-

"""
Algoritmo de ordenação por Max-Heap

"""

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

