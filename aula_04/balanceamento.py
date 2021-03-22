import unittest

## Código para adicionar path do projeto
import sys
from os import path

file_path = path.abspath(__file__)
projeto_path = path.join(file_path, '..', '..')
projeto_path = path.abspath(projeto_path)
sys.path.append(projeto_path)


## Fim

def esta_balanceada(expressao):
    """
    Função que calcula se expressão possui parenteses, colchetes e chaves balanceados
    O Aluno deverá informar a complexidade de tempo e espaço da função
    Deverá ser usada como estrutura de dados apenas a pilha feita na aula anterior
    :param expressao: string com expressao a ser balanceada
    :return: boleano verdadeiro se expressao está balanceada e falso caso contrário
    """

    if len(expressao) == 0:
        return True
    else:
        elementos = []
        abre_parenteses = 0
        fecha_parenteses = 0
        abre_colchetes = 0
        fecha_colchetes = 0
        abre_chaves = 0
        fecha_chaves = 0

        for elemento in expressao:
            elementos.append(elemento)
            if elemento == '(':
                abre_parenteses += 1
            if elemento == '[':
                abre_colchetes += 1
            if elemento == '{':
                abre_chaves += 1
            if elemento == ')':
                fecha_parenteses += 1
            if elemento == ']':
                fecha_colchetes += 1
            if elemento == '}':
                fecha_chaves += 1

        if abre_colchetes != fecha_colchetes or abre_chaves != fecha_chaves or abre_parenteses != fecha_parenteses:
            return False

        abre = abre_chaves + abre_colchetes + abre_parenteses
        for i in elementos[:-1]:
            while abre >= 1:
                abre -= 1
                if i == ')':
                    return False
                if i == ']':
                    return False
                if i == '}':
                    return False

        if abre_colchetes == fecha_colchetes and abre_chaves == fecha_chaves and abre_parenteses == fecha_parenteses:
            return True

        return elementos


class BalancearTestes(unittest.TestCase):
    def test_expressao_vazia(self):
        self.assertTrue(esta_balanceada(''))

    def test_parenteses(self):
        self.assertTrue(esta_balanceada('()'))

    def test_chaves(self):
        self.assertTrue(esta_balanceada('{}'))

    def test_colchetes(self):
        self.assertTrue(esta_balanceada('[]'))

    def test_todos_caracteres(self):  #
        self.assertTrue(esta_balanceada('({[]})'))
        self.assertTrue(esta_balanceada('[({})]'))
        self.assertTrue(esta_balanceada('{[()]}'))

    def test_chave_nao_fechada(self):
        self.assertFalse(esta_balanceada('{'))

    def test_colchete_nao_fechado(self):
        self.assertFalse(esta_balanceada('['))

    def test_parentese_nao_fechado(self):
        self.assertFalse(esta_balanceada('('))

    def test_chave_nao_aberta(self):
        self.assertFalse(esta_balanceada('}{'))

    def test_colchete_nao_aberto(self):
        self.assertFalse(esta_balanceada(']['))

    def test_parentese_nao_aberto(self):
        self.assertFalse(esta_balanceada(')('))

    def test_falta_de_caracter_de_fechamento(self):
        self.assertFalse(esta_balanceada('({[]}'))

    def test_falta_de_caracter_de_abertura(self):
        self.assertFalse(esta_balanceada('({]})'))

    def test_expressao_matematica_valida(self):
        self.assertTrue(esta_balanceada('({[1+3]*5}/7)+9'))

    def test_char_errado_fechando(self):
        self.assertFalse(esta_balanceada('[)'))
