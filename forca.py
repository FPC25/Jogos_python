import random as rd
import math as mt
import os

#função para escolher o nivel de dificuldade
def escolha_nivel (input_nivel, min_tentativas):
    #nivel dificil 
    if (input_nivel == "1"):
        tentativas = mt.floor(min_tentativas*1.5)
    #nivel medio
    elif (input_nivel == "2"):
        tentativas = int(input_nivel) * min_tentativas
    #nivel facil 
    elif (input_nivel == "3"):
        tentativas = int(input_nivel) * min_tentativas
    #nivel padrão = medio
    else:
        print("Valor padrão de dificuldade é: médio")
        input_nivel = "2"
        tentativas = int(input_nivel) * min_tentativas

    #devolve o numero de tentaticas e o nivel de dificuldade
    return tentativas, input_nivel

#função pra procurar os indexes das letras de chute 
def achar_index(chute, palavra):
    #configura para a pavra estar sempre com letras minusculas
    palavra = palavra.lower()
    #procura para ver a primeira correspondencia, se tiver
    index = palavra.find(chute.lower())
    #cria a lista de indexes para as posições das letras correspondentes ao chute, se houver
    indexes = []

    #se houver alguma correpondencia
    if index != -1:
        #adiciona na lista
        indexes.append(index)
        #enquanto ainda tiver outras correspondencias
        while index != -1:
            #procura novamente a partir da letra seguinte a ultima correspondencia
            index = palavra.find(chute.lower(), index+1)
            if index != -1: #se tiver alguma correspondecia coloca na lista
                indexes.append(index)
    #em ambos os casos devolve a lista de indexes com todas as posições onde achamos correspondecias             
        return indexes
    
    else:
        return indexes

#função para verficar se encontrou alguma correspondecia ou não e dar um feedback para o jogador
def verify(chute, acerto, palavra):
    #procuras os indexes onde há correspondecias entre chute e letas na palavra secreta
    index = achar_index(chute, palavra)
    #se tiver alguma correspondencia
    if not index == []:
        #se ainda não a tiver encontrada 
        if not chute in acerto:
            for i in index:
                #substitui a letra na lista que mosta as posições que ainda precisam ser descobertas 
                acerto[i] = palavra[i]
            #e da uma mensagem mostrando que o jogador acertou 
            print(f"\nAcertou! A letra {chute} está presente na palavra secreta!!")
        else: # se ele já tiver chutado a letra indica pra ele que uma rodada foi despediçada por ele ter colocado letra repetida
            print("\nVocê já chutou essa letra!")
    # se a lista de indexes veio vazia avisa o jogador que ele errou
    else:
        print("\nErrou! Essa letra não está presente na palavra secreta!!")

    #devolve a lista com a posições que ainda precisam ser descobertas
    return acerto

#função que vai escolher a palavra secreta com base num arquivo de palavras
def seleciona_palavra (nome_arq):
    #le o arquivo
    with open(nome_arq, 'r') as arq:
        #coloca o conteudo do arquivo em uma lista
        palavras = [linha.strip() for linha in arq]

    palavra = palavras[round(rd.randrange(0, len(palavras)))] #seleciona 

    condicao = len(palavra) >= 2
    if not condicao:
        while (condicao):
            palavra = palavras[round(rd.randrange(0, len(palavras)))]

    #devolve uma palavra escolhida aleatoriamente
    return palavra

#função de fim de jogo que vai verificar qual fim de jogo do jogador
def fim_de_jogo(fim_tentativas, acertos, palavra_secreta, venceu, enforcou):

    #se o jogador não terminou as tentativas 
    if (not fim_tentativas):
        #mas acertou todas as letras
        if (acertos.count("_") == 0):
            #indica que ele venceu 
            venceu = True
            #e da uma mensagem mostando a palavra secreta 
            print(f"\nVocê venceu o jogo!!!\nA palavra secreta era {palavra_secreta}")
    #se ele terminou todas as tentativas, mas não descobriu a palavra secreta
    else:
        #mas acertou todas as letras
        if (acertos.count("_") == 0):
            #indica que ele venceu 
            venceu = True
            #e da uma mensagem mostando a palavra secreta 
            
        #senão
        else:
            #indica que ele perdeu 
            enforcou = True
            #e da a triste noticia, mostrando qual era a palavra secreta
            caveira(palavra_secreta)

    return venceu, enforcou

#função desenvolvida pelo professor, mas que não cabe no meu jogo por conta da dificuldade do levando 
#a lista de palavras dadas para o jogo.
def desenha_forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if(erros == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(erros == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(erros == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(erros == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(erros == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(erros == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (erros == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()

#mensagens de fim de jogo

def trofeu(palavra_secreta):
    print(f"\nParabens!!\nVocê venceu o jogo!!!\nA palavra secreta era {palavra_secreta}\n")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")

def caveira(palavra_secreta):
    print(f"\nQue triste, você perdeu o jogo!!!\nA palavra secreta era {palavra_secreta}\n")
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")

def jogar():

    print("####################################")
    print("#### Bem vindo ao jogo da Forca ####")
    print("####################################")

    #identificando onde em qual pasta estamos e buscando a lista de palavras cujo arquivo esta na mesma pasta
    pwd = os.getcwd()
    nome = f'{pwd}/palavras.dat'

    #definindo pseudo-aleatoriamente a palavra secreta 
    palavra_secreta = seleciona_palavra(nome)
    acertos = ["_" for i in palavra_secreta] # para cada letra na palavra secreta adiciona o "_"

    #escolhendo o nivel de dificuldade e numero de tentativas
    nivel = input("Qual nível de dificuldade?\n (1) Difícil\n (2) Médio\n (3) Facil\n")
    tentativas, nivel = escolha_nivel(nivel, len(set(palavra_secreta)))
    
    #setando as variaveis de fim de jogo e um contador
    enforcou, venceu = False, False
    cont = 1

    #enquanto não mudarmos as variaveis de fim de jogo
    while (not enforcou and not venceu):
        #mostra pro usuario quantas tentativas ainda têm
        print(f"tentativa {cont} de {tentativas}")

        #pede o chute dele
        chute = input(f"\nQual é o seu chute?\n{acertos}\nChute: ")
        while (chute == " " or chute == ""):
            print("O chute precisa ser uma leta.")
            chute = input(f"\nQual é o seu chute?\n{acertos}\nChute: ")

        #com base no chute (já limpo de espaços e afins) verficia quantos acertos teve
        acertos = verify(chute.strip(), acertos, palavra_secreta)

        #variavel que altera o fim de jogo pra perder
        fim_tentativas = cont >= tentativas 

        #verfica se ganhou ou perdeu o jogo
        venceu, enforcou = fim_de_jogo(fim_tentativas, acertos, palavra_secreta, venceu, enforcou)
        
        #conta mais uma tentativa
        cont += 1

#se o jogo estiver rodando como só ele mesmo (sem estar sendo chamado de outro lugar), roda o jogo
if (__name__ == "__main__"):
    jogar()
