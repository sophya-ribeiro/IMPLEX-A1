import random

"""
Gera um arquivo .txt com números aleatórios.
Recebe 'fim', 'inc', 'stp' e 'rpt'

[[RANDOM]]
[[REVERSE]]
[[SORTED]]
[[NEARLY
SORTED]]
"""

def gerar_numeros_aleatorios(n, nome_arquivo):

    numeros = [random.randint(1, 1000) for _ in range(n)]
    
    with open(nome_arquivo, 'w') as arquivo:
        for numero in numeros:
            arquivo.write(f"{numero}\n")
    
    print(f"Arquivo '{nome_arquivo}' gerado com {n} números aleatórios.")

#-----------------------------------------------------------------------------

"""
Os seguintes parâmetros refence aos gráficos:
> inc é o tamanho inicial de um vetor de entrada;
> fim é o tamanho final;
> stp é o intervalo entre dois tamanhos; e
> rpt é o número de repetições a serem realizadas

> o tamanho máximo do vetor aleatório é n^2, sendo n 
o tamanho do vetor a ser ordenado.
"""

n = int(input("Digite a quantidade de números aleatórios: "))
nome_arquivo = input("Digite o nome do arquivo a ser gerado (ex: numeros.txt): ")

gerar_numeros_aleatorios(n, nome_arquivo)
 