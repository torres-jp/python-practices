class Olympics:

    def __init__(self):
        self.events = []

    def event_register(self):
        
        event = input("Introduce el nombre del evento deportivo")

        self.events.append(event)




print("Simulador de juegos olimpicos")

while True:

    print()

    print("1. Registro de Eventos")
    print("2. Registro de Participantes")
    print("3. Simulacion de eventos")
    print("4. Creacion de Informes")
    print("5. Salir del Programa")


    option = input('Selecciona una accion: ')

    match option:
        case "1":
            pass
        case "2":
            pass
        case "3":
            pass
        case "4":
            pass
        case "5":
            print("Saliendo del simulador ...")
            break
        case _:
            print('Opcion Incorrecta, selecciona una nueva.')