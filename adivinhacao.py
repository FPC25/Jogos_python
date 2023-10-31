import random as rd
import math as mt

def perdidos (pontos, nivel):
    if (nivel == "1"):
        if pontos == 1:
            pontos = mt.ceil(pontos/2)
        else:
            pontos = round(pontos/2)
    elif (nivel == "2"):
        pontos = pontos
    else:
        pontos = pontos*2
    
    return(pontos)

def escolha_nivel (input_nivel, min_tentativas = 10):
    if (input_nivel == "1"):
        tentativas = mt.ceil(min_tentativas/1.5)
    elif (input_nivel == "2"):
        tentativas = min_tentativas
    elif (input_nivel == "3"):
        tentativas = mt.ceil(min_tentativas * 1.5)
    else:
        print("Valor padrão de dificuldade é: médio")
        input_nivel = "2"
        tentativas = min_tentativas

    return tentativas, input_nivel

def jogar():
    print("####################################")
    print("# Bem vindo ao jogo de Adivinhação #")
    print("####################################")

    numero_secreto = round(rd.randrange(1, 101))
    pontos_totais = 500

    nivel = input("Qual nível de dificuldade?\n (1) Difícil\n (2) Médio\n (3) Facil\n")
    tentativas, nivel = escolha_nivel(nivel)

    for i in range(0, tentativas):
        print("tentativa {} de {}".format(i+1, tentativas))
        chute = int(input("Digite um numero inteiro entre 1 e 100: "))

        print("Seu chute:", chute)

        if (chute < 1 or chute > 100):
                print("Você deve digitar um numero entre 1 e 100")
                continue

        acertou = int(chute) == numero_secreto 
        maior = int(chute) > numero_secreto
        menor = int(chute) < numero_secreto

        if (acertou):
            print("Você acertou!")
            print(f"sua pontuação final é: {pontos_totais}")
            break

        else:
            if (maior):
                print("Você errou! Seu chute é maior que o numero secreto")

            elif (menor):
                print("Você errou! Seu chute é menor que o numero secreto")
            
            pontos_totais = pontos_totais - perdidos(abs(numero_secreto - chute), nivel)
            
    if (acertou == False):
        print(f"Foi uma pena, o numero secreto era {numero_secreto}. Mais sorte na proxima!\n")

if (__name__ == "__main__"):
#aqui esta perguntando se o programa esta sendo individualmente rodado ou se ele esta sendo importado 
    jogar()