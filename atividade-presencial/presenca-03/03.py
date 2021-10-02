class Pilha:
    def _init_(self):
        self.numeros = list()

    def adicionar_numero(self, novo):
        self.numeros.append(novo)
    
    def remover_numero(self):
        del self.numeros[-1]

    def mostrar(self):
        print(*self.numeros)

pilhacontagem = Pilha()
print("Lista:")

pilhacontagem.adicionar_numero(1)
pilhacontagem.adicionar_numero(2)
pilhacontagem.adicionar_numero(3)
pilhacontagem.adicionar_numero(4)
pilhacontagem.adicionar_numero(5)
pilhacontagem.adicionar_numero(6)

pilhacontagem.mostrar()
print("\nLista com elemento removido:")

pilhacontagem.remover_numero()

pilhacontagem.mostrar()