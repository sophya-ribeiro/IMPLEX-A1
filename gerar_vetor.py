import random

"""
Gera um arquivo .txt com números aleatórios.
Recebe 'fim', 'inc', 'stp' e 'rpt'

[[RANDOM]]
[[REVERSE]]
[[SORTED]]
[[NEARLY SORTED]]
"""

def gerar_numeros_aleatorios(n, nome_arquivo):

    numeros = [random.randint(1, n**2) for _ in range(n)]
    # 'n**2' limitação para manter o tempo do counting sort linear
    
    with open(nome_arquivo, 'w') as arquivo:
        for numero in numeros:
            arquivo.write(f"{numero}\n")
    
    print(f"Arquivo '{nome_arquivo}' gerado com {n} números aleatórios.")


def gerar_vetor_quase_ordenado(n, nome_arquivo):
    numeros = [random.randint(1, n**2) for _ in range(n)]

    numeros.sort()

    i_toshuffle = [random.randint(1, n) for _ in range(int(0.1 * n))]
    #lista de índices das posições que serão trocadas 

    for i in range(0, len(i_toshuffle)):
        numeros[i_toshuffle[i]] = random.randint(1, n**2)

    with open(nome_arquivo, 'w') as arquivo:
        for numero in numeros:
            arquivo.write(f"{numero}\n")
    
    print(f"Arquivo '{nome_arquivo}' gerado com {n} números aleatórios.")

#-----------------------------------------------------------------------------

"""
Os seguintes parâmetros refere aos gráficos:
> inc é o tamanho inicial de um vetor de entrada;
> fim é o tamanho final;
> stp é o intervalo entre dois tamanhos; e
> rpt é o número de repetições a serem realizadas
"""



def main():
    n = int(input("Digite a quantidade de números aleatórios: "))
    nome_arquivo = input("Digite o nome do arquivo a ser gerado (ex: numeros.txt): ")

    print("\n\
          [1] Gerar vetor aleatório;\n\
          [2] Gerar vetor 'quase' ordenado;\n\
          Escolha: ", end='')
    op = int(input())
    
    if(op == 1):
        gerar_numeros_aleatorios(n, nome_arquivo)

    elif(op == 2):
        gerar_vetor_quase_ordenado(n, nome_arquivo)

    else:
        print("Opção inválida.")


if __name__ == "__main__":
    main()