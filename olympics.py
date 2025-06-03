class Players:
    def __init__(self, name, country):
        self.name = name
        self.country = country

    
    def __eq__(self, other: object) -> bool:
        if isinstance(other, Players):
            return self.name == other.name and self.country == other.country
        return False 

    def __hash__(self) -> int:
        return hash(self.name, self.country)


class Olympics:
    def __init__(self):
        self.events = []
        self.participants = {}

    def event_register(self):
        event = input("Introduce el nombre del evento deportivo").strip()

        if event in self.events:
            print(f"El evento {event} ya esta registrado")
        else:
            self.events.append(event)
            print(f"Evento {event} registrado correctamente.")

    def players_register(self):
        if not self.events:
            print("No hay eventos registrados. Por favor elige uno primero.")
            return

        name = input("Introduce el nombre de este participante: ").strip()
        country = input("Introduce el pais del participante").strip()
        participant = Players(name, country)

        print("Eventos disponibles: ")
        for index, event in enumerate(self.events):
            print(f"{index + 1}. {event}")

        event_choice = (
            int(input("Selecciona el numero del evento para asignar al participante")) - 1
        )

        if event_choice >= 0 and event_choice < len(self.events):
            event = self.events[event_choice]

            if participant in self.participants[event]:
                print(f'El participante {name} de {country} se registro en el evento deportivo {event}')
            
            else:
                self.participants[event].append(participant)
                print(f'El participante {name} de {country} se registro en el evento deportivo {event}')
        else:
            print("Seleccion de evento invalido. El participante no esta registrado")



olympics = Olympics()


print("Simulador de juegos olimpicos")

while True:
    print()

    print("1. Registro de Eventos")
    print("2. Registro de Participantes")
    print("3. Simulacion de eventos")
    print("4. Creacion de Informes")
    print("5. Salir del Programa")

    option = input("Selecciona una accion: ")
    match option:
        case "1":
            olympics.event_register()
        case "2":
            olympics.players_register()
        case "3":
            pass
        case "4":
            pass
        case "5":
            print("Saliendo del simulador ...")
            break
        case _:
            print("Opcion Incorrecta, selecciona una nueva.")
