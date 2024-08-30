# -*- coding: utf-8 -*-
 
"""
Algoritmo de ordenação por Max-Heap

- Receber um tamanho de vetor
- Ler os elementos do vetor
- Construir max-heap com o vetor lido
- Ordenar a max-heap
         
"""

def pai(i):
    return i//2

def filho_esquerdo(i):
    return 2*i

def filho_direito(i:int):
    return 2 * i + 1

def ajusta_max_heap(vetor:list, i, tam_heap):
    esq = filho_esquerdo(i) #l
    dir = filho_direito(i)  #r

    if esq <= tam_heap and vetor[esq] > vetor[i]:
        maior = esq
    else:
        maior = i

    if dir <= tam_heap and vetor[dir] > vetor[i]:
        maior = dir
   
    if maior != i:
        tam_heap = tam_heap - 1
        temp = vetor[i]
        vetor[i] = vetor[maior]
        vetor[maior] = vetor[temp]
        #trocar posições a[i] com a[maior]
        ajusta_max_heap(vetor, maior, tam_heap)

