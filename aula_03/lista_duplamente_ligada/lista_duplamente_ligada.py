class ListaVaziaErro(Exception):
    pass


class Noh:
    def __init__(self, valor, esquerdo=None, direito=None):
        self.valor = valor
        self.esquerdo = esquerdo
        self.direito = direito

    def __iter__(self):
        noh_atual = self
        while noh_atual != None:
            yield noh_atual
            noh_atual = noh_atual.proximo


class ListaDuplamenteLigada():
    def __init__(self):
        self.tam = 0
        self.primeiro = None
        self.ultimo = None
        self._noh_inicial: Noh = None

    def adicionar(self, valor, indice=None):
        if self.tam == 0:
            self._noh_inicial = Noh(valor, self._noh_inicial)
            self.primeiro = self._noh_inicial
            self.ultimo = self._noh_inicial
            self.tam += 1

        elif self.tam != 0:
            noh = Noh(valor)
            self.ultimo = noh
            self._noh_inicial.direito = noh
            noh.esquerdo = self._noh_inicial
            self.tam += 1
