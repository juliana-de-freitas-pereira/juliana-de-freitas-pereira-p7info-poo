frases = [
    "I love you",
    "Bom dia",
    "Descobridor dos sete mares",
    "Hipopótamo",
    "Agora eu era herói",
    "O que faço eu da vida sem você"
]

for frase in frases:
    mensagem = ""
    maior = ""
    i = 0
    a = frase.split(" ")

    while i < len(a):
        mensagem += str(len(a[i])) + "-"
        if len(a[i]) > len(maior):
            maior = a[i]

        i += 1

    mensagem = mensagem[-len(mensagem):-1]
    print("{:25s} {}".format(mensagem, maior))