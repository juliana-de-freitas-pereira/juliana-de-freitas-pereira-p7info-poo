class FilaContagem(object):
    def _init_(self):
        self.elementos = []

    def adicionar(self, numero):
        self.elementos.append(numero)

    def remover(self):
        return self.elementos.pop(0)

    def estaVazia(self):
        return len(self.elementos) == 0

    def mostrar(self):
        for a in self.elementos:
            print(a)

filadecontagem = FilaContagem()
print("Lista de contagem com números inseridos:")
filadecontagem.adicionar(1)
filadecontagem.adicionar(2)
filadecontagem.adicionar(3)
filadecontagem.adicionar(4)
filadecontagem.adicionar(5)

filadecontagem.mostrar()

filadecontagem.remover()
print("\nLista de contagem após remoção do número:")
filadecontagem.mostrar()