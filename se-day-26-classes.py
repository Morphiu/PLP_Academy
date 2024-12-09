# Assingnment 1

class Supe:
    def __init__(self, heroName, mainPower, age, city):
        self.heroName = heroName
        self.mainPower = mainPower
        self.age = age
        self.city = city

class hero(Supe):
    def __init__(self, heroName, mainPower, age, city, popularity):
        super().__init__ (heroName, mainPower, age, city)
        self.popularity = popularity
    def traversal(self):
        return "Flying"

class villain(Supe):
    def traversal(self):
        return "Super-Jumping"

supe1 = hero('One-punch man', 'Super-strength', 40, 'City-z', 'loved')
supe2 = hero('Metro-man', 'Super-strength', 1000, 'MetroCity', 'loved')
supe3 = hero('Tony-Stark', 'Super-Inteligent', 45, 'New-york', 'loved')
supe4 = villain('Dr. Doom', 'Magic & Science', 45000, 'Manhattan')

print(f'{supe1.heroName} moves by {supe1.traversal()}')
print(f'{supe4.heroName} moves by {supe4.traversal()}')


#Activity 2
class animals:
    def move(self):
        return "Running"

class vehicles:
    def move(self):
        return "Driving"

class Airplane:
    def move(self):
        return "Flying"

car = vehicles()
plane = Airplane()
mammal = animals()

print(f'{car.move()}')
print(f'{plane.move()}')
print(f'{mammal.move()}')
