class ListaVaziaErro(Exception):
    pass


class Noh:
    def __init__(self, valor, esquerdo=None, direito=None):
        self.valor = valor
        self.esquerdo = esquerdo
        self.direito = direito

    def __iter__(self):
        noh_atual = self
        while noh_atual is not None:
            yield noh_atual
            noh_atual = noh_atual.direito


class ListaDuplamenteLigada():
    def __init__(self):
        self.tam = 0
        self.primeiro = None
        self.ultimo = None
        self._noh_inicial: Noh = None

    def __len__(self):
        if self._noh_inicial is None:
            return 0
        for indice, _ in enumerate(self._noh_inicial, start=1):
            pass
        return indice

    def __getitem__(self, indice_produrado):
        for indice, noh in enumerate(self._noh_inicial):
            if indice == indice_produrado:
                return noh.valor

    def adicionar(self, valor):
        if self.tam == 0:
            self._noh_inicial = Noh(valor, self._noh_inicial)
            self.primeiro = self._noh_inicial
            self.ultimo = self._noh_inicial
            self.tam += 1

        elif self.tam != 0:
            noh = Noh(valor)
            ultimo_noh = self._noh_inicial
            while ultimo_noh.direito is not None:
                ultimo_noh = ultimo_noh.direito
            ultimo_noh.direito = noh
            self.ultimo = ultimo_noh.direito

            for indice_atual, noh_atual in enumerate(self._noh_inicial, start=1):
                if indice_atual == self.tam:
                    noh = Noh(valor, noh_atual.direito)
                    noh_atual.direito = noh
                    self.tam += 1
                    break
