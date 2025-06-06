class Person:
    def __init__(self, id: int, name: str):
        self.id = id
        self.name = name
        self.partner = None
        self.children = []


    def add_partner(self, partner):
        if self.partner is not None:
            print(f'{self.name} ya tiene pareja: {self.partner.name}.')
        else:
            self.partner = partner
            partner.partner = self
            print(f'{self.name} es pareja de {partner.name}.')


    def add_child(self,child):
        if child not in self.children:
            self.children.append(child)
            print(f'{self.name} ah tenido un hijo {child.name}')
        else:
            print(f'{child.name} es hijo de {self.name}')


class Family_tree:
    def __init__(self):
        self.people = {}


    def add_person(self,id,name):
        if id in self.people:
            print(f'La persona con id {id} ya existe')
        else:
            person = Person(id,name)
            self.people[id] = person
            print(f'La persona con nombre {name} [ID: {id} ah sido añadido al arbol]')

    def remove_person(self,id):
        if id in self.people:
            person = self.people[id]
            del self.people[id]
            print(f'La persona {person} [ID: {id}] ah sido eliminada')
        else:
            print(f'La persona con ID: {id} no existe en el arbol.')

    def set_partner(self,id1,id2):
        if id1 in self.people and id2 in self.people:
            person1 = self.people[id1]
            person2 = self.people[id2]


    def add_child(self):
        pass


    def print_tree(self):
        pass