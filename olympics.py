class Players:
    def __init__(self, name, country):
        self.name = name
        self.country = country



class Olympics:
    
    def __init__(self):
        self.events = []

    def event_register(self):
        
        event = input("Introduce el nombre del evento deportivo").strip()

        if event in self.events:
            print(f'El evento {event} ya esta registrado')
        else:
            self.events.append(event)
            print(f'Evento {event} registrado correctamente.')

    def players_register(self):

        if not self.events:
            print('No hay eventos registrados. Por favor elige uno primero.')
            return

        name = input('Introduce el nombre de este participante: ').strip()
        country = input('Introduce el pais del participante').strip()
        participant = Players(name, country)

        print('Eventos disponibles: ')
        for index, event in enumerate(self.events):
            print(f'{event}')

        

olympics = Olympics()


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
            olympics.event_register()
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