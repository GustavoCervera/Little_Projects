import random

def Ganhador(player):
    pass

def Gerar_Objeto():
    number = random.randint(0,2)
    if number == 0:
        move = "pedra"
    elif number == 1:
        move = "papel"
    else:
        move = "tesoura"
    return move


my_count = 0
pc_count = 0
while True:
    my_answer = input("Voce deseja jogar? ")
    if my_answer == "n":
        print("Obrigado por jogar conosco!")
        print("O Score final foi de: \n")
        print("Player {} x {} Computer".format(my_count,pc_count))
        break
    else:
        my_move = input("Qual eh o golpe que deseja... ")
        pc_move = Gerar_Objeto()
        
        print("Seu golpe: \t\t{}".format(my_move))
        print("Golpe do pc: \t{}".format(pc_move))
        
        print("\n")
        if my_move == "pedra":
            if pc_move == "pedra":
                result = "empate"
            elif pc_move == "papel":
                result = "Ponto PC"
                pc_count = pc_count + 1
            else:
                result = "Ponto Player"
                my_count = my_count + 1
        
        if my_move == "papel":
            if pc_move == "papel":
                result = "empate"
            elif pc_move == "tesoura":
                result = "Ponto PC"
                pc_count = pc_count + 1
            else:
                result = "Ponto Player"
                my_count = my_count + 1
                
        if my_move == "tesoura":
            if pc_move == "tesoura":
                result = "empate"
            elif pc_move == "pedra":
                result = "Ponto PC"
                pc_count = pc_count + 1
            else:
                result = "Ponto Player"
                my_count = my_count + 1
                
                
        print("Resultado: \t\t{}".format(result))
