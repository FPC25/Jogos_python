import adivinhacao
import forca


def escolhe_jogo():
    print("###################################")
    print("########## Menu de Jogos ##########")
    print("####################################")

    jogo = "5"
    while (jogo != "1" or jogo != "2"):
        jogo  = input("Escolha o jogo que quer jogar:\n (1) Adivinhação\n (2) Forca\n")
        if (jogo == "1"):
            #advinhação
            print("Iniciando jogo da adivinhacao")
            break
        elif (jogo == "2"):
            #forca
            print("Iniciando jogo da  forca")
            break
        else:
            print("As opções são 1 e 2 para acessar os jogos\n")

    if jogo == "1":
        adivinhacao.jogar()

    elif jogo == "2":
        forca.jogar()

if (__name__ == "__main__"):
    escolhe_jogo()

