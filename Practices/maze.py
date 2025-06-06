maze = [
    ["🐭", "◻️", "◻️", "⬛", "⬛", "◻️"],
    ["◻️", "⬛", "⬛", "⬛", "⬛", "◻️"],
    ["◻️", "◻️", "◻️", "◻️", "◻️", "◻️"],
    ["⬛", "⬛", "⬛", "◻️", "⬛", "⬛"],
    ["⬛", "⬛", "⬛", "◻️", "◻️", "◻️"],
    ["⬛", "⬛", "⬛", "⬛", "⬛", "🚪"]
]


def print_maze():
    for row in maze:
        print("".join(row))
    print()


user = [0, 0]



while True:

    print_maze()

    print("Que direccionar tomar:\n")
    print("[w] Up")
    print("[s] Down")
    print("[a] Left")
    print("[d] Right")

    direction = input("Direction:\n")

    current_row, current_column = user
    new_row, new_column = current_row, current_column

    match direction:
        case "w":
            new_row = current_row - 1
        case "s":
            new_row = current_row + 1
        case "a":
            new_column = current_column - 1
        case "d":
            new_column = current_column + 1
        case _:
            print('Direccion no valida!\n')
            continue

    if new_row < 0 or new_row > 5 or new_column < 0 or new_column > 5:
        print('No puedes desplazarte fuera del tablero\n')
        continue
    else:
        if maze[new_row][new_column] == "⬛":
            print('En esta direccion hay un obstaculo\n')
            continue

        elif maze[new_row][new_column] == "🚪":
            print('Felicitaciones Ganaste!\n')
            print_maze()
            break

        else:
            maze[current_row][current_column] = "◻️"
            maze[new_row][new_column] = "🐭"
            user = [new_row, new_column]

