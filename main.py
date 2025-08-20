import random

def escolher_dificuldade():
    print("Bem vindo ao jogo!")
    print("Por favor escolha uma dificuldade abaixo:\n")
    print("1 - Facil (10 Tentativas) ")
    print("2 - Medio (6 Tentativas) ")
    print("3 - Dificil (3 Tentativas) ")

    escolha = input("Escolha um numero: ")
    while True:
        if escolha == "1":
            print('Voce escolheu o Modo facil')
            return 10
        elif escolha == "2":
            print('Voce escolheu o Modo medio')
            return 6
        elif escolha == "3":
            print('Voce escolheu o Modo dificil')
            return 3
        else:
            print("Por favor digite uma escolha valida!")
            break
    

def jogar():
    numero_secreto = random.randint(1,100)

    maximo_tentativas = escolher_dificuldade()
    tentaivas_usadas = 0

    print("Adivinhe o numero de 1 - 100!")

    while tentaivas_usadas < maximo_tentativas:
        try:
            chutar = int(input(f'Tentativa {tentaivas_usadas + 1}: '))
        except ValueError:
            print("Digite um numero valido!")
            continue   


        tentaivas_usadas += 1

        if chutar == numero_secreto:
            print(f"Meus parabens voce acertou o numero secreto {numero_secreto} em {tentaivas_usadas} tentativas") 
            break
        elif chutar < numero_secreto:
            print("O Numero e maior!\n")
        else:
            print("O Numero e menor!\n")

    if chutar != numero_secreto:
            print(f'Fim, suas tentativas acabaram! O numero era {numero_secreto}.')    

jogar()







