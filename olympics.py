import random


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
        self.results = {}
        self.country_results = {}

    def event_register(self):
        event = input("Introduce el nombre del evento deportivo: ").strip()

        if event in self.events:
            print(f"El evento {event} ya esta registrado")
        else:
            self.events.append(event)
            print(f"Evento {event} registrado correctamente.")

    def players_register(self):
        if not self.events:
            print("No hay eventos registrados. Por favor elige uno primero: ")
            return

        name = input("Introduce el nombre de este participante: ").strip()
        country = input("Introduce el pais del participante: ").strip()
        participant = Players(name, country)

        print("Eventos disponibles: ")
        for index, event in enumerate(self.events):
            print(f"{index + 1}. {event}")

        event_choice = (
            int(input("Selecciona el numero del evento para asignar al participante: "))
            - 1
        )

        if event_choice >= 0 and event_choice < len(self.events):
            event = self.events[event_choice]

            if participant in self.participants[event]:
                print(
                    f"El participante {name} de {country} se registro en el evento deportivo: {event}"
                )

            else:
                self.participants[event].append(participant)
                print(
                    f"El participante {name} de {country} se registro en el evento deportivo: {event}"
                )
        else:
            print("Seleccion de evento invalido. El participante no esta registrado: ")

    def simulate_events(self):
        if not self.events:
            print("No hay eventos registrados , por favor registra un evento primero: ")
            return

        for event in self.events:
            if len(self.participants[event]) < 3:
                print(f"No hay participante suficientes para el {event}: ")
                continue

            event_participants = random.sample(self.participant[event], 3)
            random.shuffle(event_participants)

            gold, silver, bronze = event_participants
            self.results[event] = [gold, silver, bronze]

            self.update_country_results(gold.country, "gold")
            self.update_country_results(silver.country, "silver")
            self.update_country_results(bronze.country, "bronze")

            print(f"Simulacion del evento: {event}")
            print(f"Oro {gold.name} ({gold.country})")
            print(f"Silver {silver.name} ({silver.country})")
            print(f"Bronze {bronze.name} ({bronze.country})")

    def update_country_results(self, country, medal):
        if country not in self.country_results:
            self.country_results[country] = {"gold": 0, "silver": 0, "bronze": 0}

        self.country_results[country][medal] += 1

    def show_reports(self):

        print('Informe juegos olimpicos: ')

        if  self.results:
            for event, winners in self.results.items():
                print(f"Evento : {event}")
                print(f"Oro {winners[0].name} ({winners[0].country})")
                print(f"Silver {winners[1].name} ({winners[1].country})")
                print(f"Bronze {winners[2].name} ({winners[2].country})")

        else:
            print("No hay resultados registrados")

        if self.country_results:
            for country,medals in sorted(self.country_results.items(), key=lambda x: (x[1]["gold"], x[1]["silver"], x[1]["bronze"])):
                print(f'{country}: Oro {medals['gold']}, Silver {medals['silver']}, Bronze {medals['bronze']}')

        else:
            print("No hay medallas registradas")    

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
            olympics.simulate_events()
        case "4":
            olympics.show_repors()
        case "5":
            print("Saliendo del simulador ...")
            break
        case _:
            print("Opcion Incorrecta, selecciona una nueva.")
