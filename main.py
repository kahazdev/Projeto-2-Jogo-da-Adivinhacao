import random

def escolher_dificuldade():
    print("Bem vindo ao jogo!")
    print("Por favor escolha uma dificuldade abaixo:\n")
    print("1 - Fácil (10 Tentativas) ")
    print("2 - Médio (6 Tentativas) ")
    print("3 - Difícil (3 Tentativas) ")

    
    while True:
        escolha = input("Escolha um número: ")
        if escolha == "1":
            print('Você escolheu o Modo facil')
            return 10
        elif escolha == "2":
            print('Você escolheu o Modo medio')
            return 6
        elif escolha == "3":
            print('Você escolheu o Modo dificil')
            return 3
        else:
            print("Por favor digite uma escolha valida!")

    

def jogar():
    numero_secreto = random.randint(1,100)

    maximo_tentativas = escolher_dificuldade()
    tentaivas_usadas = 0

    print("Adivinhe o número de 1 - 100!")

    while tentaivas_usadas < maximo_tentativas:
        try:
            chutar = int(input(f'Tentativa {tentaivas_usadas + 1}: '))
        except ValueError:
            print("Digite um número valido!")
            continue   


        tentaivas_usadas += 1

        if chutar == numero_secreto:
            print(f"Meus parabéns! você acertou o número secreto {numero_secreto} em {tentaivas_usadas} tentativas") 
            break
        elif chutar < numero_secreto:
            print("O número é maior!\n")
        else:
            print("O número é menor!\n")

    if chutar != numero_secreto:
            print(f'Fim, suas tentativas acabaram! O número era: {numero_secreto}.')    

jogar()







