from math import inf
from time import time


def _meu_min_max(iteravel, numero_minimo, numero_maximo):
    numero = len(iteravel)
    if numero == 0:
#        print(f' Numero Minimo:{numero_minimo} | Numero Máximo:{numero_maximo}')
        return
    if iteravel[numero - 1] < numero_minimo:
        numero_minimo = iteravel[numero - 1]
    if iteravel[numero - 1] > numero_maximo:
        numero_maximo = iteravel[numero - 1]
    iteravel.pop()
    _meu_min_max(iteravel, numero_minimo, numero_maximo)


def meu_min_max(iteravel):
    _meu_min_max(iteravel, numero_minimo=inf, numero_maximo=-inf)


if __name__ == '__main__':
    print('#### Mínimo e Máximo para Lista com apenas 1 elemento ####')
    meu_min_max([44])

    print('#### Mínimo e Máximo para Lista com vários elementos ####')

    inicio = 997
    for n in range(0, inicio):
        tempo_inicial = time()
        meu_min_max(list(range(n)))
        tempo_final = time()
        tempo_de_execucao_em_segundos = tempo_final - tempo_inicial
        print('*' * int(tempo_de_execucao_em_segundos * 10000), n)
        print(f'Tempo de Execução:{(tempo_de_execucao_em_segundos * 10000)}, para {n} elemtnos')