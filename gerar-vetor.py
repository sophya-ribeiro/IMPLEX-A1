import random

def gerar_numeros_aleatorios(n, nome_arquivo):
    numeros = [random.randint(1, 1000) for _ in range(n)]
    
    with open(nome_arquivo, 'w') as arquivo:
        for numero in numeros:
            arquivo.write(f"{numero}\n")
    
    print(f"Arquivo '{nome_arquivo}' gerado com {n} números aleatórios.")

n = int(input("Digite a quantidade de números aleatórios: "))
nome_arquivo = input("Digite o nome do arquivo a ser gerado (ex: numeros.txt): ")

gerar_numeros_aleatorios(n, nome_arquivo)
