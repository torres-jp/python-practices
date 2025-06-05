import random

player1_health = int(input("Introduce la vida de tu personaje: "))
player2_health = int(input("Introduce la vida de tu personaje: "))

while player1_health > 0 and player2_health > 0:
    # player 1 actions

    if random.random() > 0.2:
        player1_damage = random.randint(10, 100)
        if player1_damage == 100:
            print("Golpe Critico, el rival no puede atacar en el siguiente turno.")

        player2_health -= player1_damage

        if player2_health <= 0:
            print("La vida de player 2 llego a 0")
            break
        else:
            print(f"Healt restante de player 2: {player2_health}")

    else:
        print("player 1 esquiva el ataque del enemigo")

    # player 2 actions

    if random.random() > 0.25:
        player2_damage = random.randint(10, 120)
        if player2_damage == 100:
            print("Golpe Critico, el rival no puede atacar en el siguiente turno.")

        player1_health -= player2_damage

        if player1_health <= 0:
            print("La vida de player 1 llego a 0")
            break
        else:
            print(f"Healt restante de player 1: {player1_health}")

    else:
        print("player 2 esquiva el ataque del enemigo")


if player1_health > 0:
    print("Player 1 Gano")
else:
    print("Player 2 Gano")
