import random


print("**********************************")
print("**********************************")
print("*Bem-vindo ao jogo de Adivinhação*")
print("**********************************")
print("**********************************")


numero_secreto = random.randrange(1,101)
total_de_tentativas = 0
pontos = 1000



print("Qual o nível de dificuldade? ")
print("(1)Fácil (2)Médio (3)Difícil")
nivel = int(input("Digite o nível desejado!"))
if (nivel == 1):
    total_de_tentativas = 20
elif(nivel == 2):
    total_de_tentativas = 10
else:
    total_de_tentativas = 5



for rodada in range(1,total_de_tentativas + 1):
    print("Tentativa {} de {} ".format(rodada,total_de_tentativas))
    chute_str = input("Digite um número entre 1 e 100:\n")
    print("Você digitou o número",chute_str)
    chute = int(chute_str)

    if(chute < 1 or chute > 100):
        print("Você deve digitar um número entre 1 e 100!")
        continue


    acertou = chute == numero_secreto
    maior = chute > numero_secreto
    menor = chute < numero_secreto


    if (acertou):
        print("Você acertou o número secreto!!!")
        print("Sua pontuação é {} ".format(pontos))
        break
    else:
        if (maior):
            print("Seu chute foi maior que o número secreto!")
        elif(menor):
            print("O seu chute foi menor que o número secreto")
        pontos_perdidos = abs(numero_secreto - chute)
        pontos = pontos - pontos_perdidos
    

print("Fim de jogo!")

