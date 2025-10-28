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
escolha_jogador = int(input("Digite seu palpite: "))

if escolha_jogador in numeros:
    if escolha_jogador == numero_aleatorio:
        print("Parabéns, você acertou o número escolhido pelo computador!!)")
    else:
        print(f"Você perdeu =( . O número escolhido pelo computador foi: {numero_aleatorio}")
else:
    print("Número não foi digitado pelo jogador!!")