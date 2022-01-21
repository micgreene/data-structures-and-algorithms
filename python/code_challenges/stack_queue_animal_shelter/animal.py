class Animal():
    '''
    This class represents an animal being kept in a shelter.
    Attributes:
        self.name: string
        self.species: string (should only be 'dog' or 'cat')
    '''
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def __str__(self):
        return f'The {self.species} named {self.name}'

    def __repr__(self):
        return f'Animal(name: {self.name}, species: {self.species})'
