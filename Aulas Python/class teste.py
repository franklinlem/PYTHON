class Dog:
    def __init__(self, Nome, Raca, Idade):
        self.Nome = Nome
        self.Raca = Raca
        self.Idade = Idade

    def bark(self):
        print('Au au!!!')

dog = Dog('Dick', 'Yorkshire', '12 anos')
print(dog.Nome, dog.Raca, dog.Idade)
dog.bark()
