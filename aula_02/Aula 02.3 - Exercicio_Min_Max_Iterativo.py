from math import inf
from random import shuffle
from time import time


def meu_min_max(iteravel):
    numero_minimo = inf
    numero_maximo = -inf

    for numero in iteravel:
        if numero > numero_maximo:
            numero_maximo = numero
    for numero in iteravel:
        if numero < numero_minimo:
            numero_minimo = numero
    return numero_minimo, numero_maximo


if __name__ == '__main__':
    print(meu_min_max([1]))
    print(meu_min_max([1, 5, 10]))
    lista = list(range(50001))
    shuffle(lista)
    print(meu_min_max(lista))

    print('Estudo Experimental sobre o tempo de execução da função max e min')
    inicio = 1_000_000
    for n in range(0, inicio * 10 + 1, inicio):
        inicio = time()
        meu_min_max(range(n))
        fim = time()
        tempo_de_execucao_em_segundos = fim - inicio
        print('*' * int(tempo_de_execucao_em_segundos * 10), n)
