import random

numeros = []
print("\nJogo de adivinhar o número escolhido pelo computador!!\nDigite \"pronto\" para finalizar a escolha de números\n\n")

#definindo números da lista
while True:
    num = input("Digite alguns números: ")

    if num.lower() == 'pronto':
        break

    num_int = int(num)
    numeros.append(num_int)

#número escolhido pelo computador
numero_aleatorio = random.choice(numeros)

#escolha do jogador e verificação da existência do número dentro da lista
print(numeros)

tentativas = 0
acertou = False

while not acertou:
    tentativas += 1
    escolha_jogador = int(input("Digite seu palpite: "))

    if escolha_jogador in numeros:
        if escolha_jogador == numero_aleatorio:
            print(f"Parabéns, você acertou o número escolhido pelo computador em {tentativas} tentativa(s)!!")
            break
        else:
            print(f"Você errou =( . Tente novamente!")
    else:
        print("Número não foi digitado pelo jogador!!")
