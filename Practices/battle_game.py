import random
import time

player1_health = int(input("Introduce la vida de tu Player 1: "))
player2_health = int(input("Introduce la vida de tu Player 2: "))

turn = 0
regenerate = False


while player1_health > 0 and player2_health > 0:

    turn += 1
    print(f'Turno {turn}')
    # player 1 actions
    if regenerate:
        print("Player 1 recupera vitalidad")
        regenerate = False

    elif random.random() > 0.2:
        player1_damage = random.randint(10, 100)
        print(f'El ataque de player 1 realizo: {player1_damage} de daño')

        if player1_damage == 100:
            regenerate = True
            print("Golpe Critico, el rival no puede atacar en el siguiente turno.")

        player2_health -= player1_damage

        if player2_health <= 0:
            print("La vida de player 2 llego a 0")
            break
        else:
            print(f"Healt restante de player 2: {player2_health}")

    else:
        print("player 1 esquiva el ataque del enemigo")

######################################################
    # player 2 actions

    if regenerate:
        print("Player 2 recupera vitalidad")
        regenerate = False
    elif  random.random() > 0.25:
        player2_damage = random.randint(10, 120)
        print(f'El ataque de player 2 realizo: {player2_damage} de daño')
        if player2_damage == 120:
            regenerate = False
            print("Golpe Critico, el rival no puede atacar en el siguiente turno.")

        player1_health -= player2_damage

        if player1_health <= 0:
            print("La vida de player 1 llego a 0")
            break
        else:
            print(f"Vida restante de player 2: {player2_health}")

    else:
        print("player 1 esquiva el ataque del enemigo")


    time.sleep(1)

if player1_health > 0:
    print("Player 1 Gano")
else:
    print("Player 2 Gano")
