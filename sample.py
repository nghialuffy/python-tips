from datetime import datetime


class Person:
    weight = 0

    def __init__(self, name: str, age: int):
        """
        This is the constructor
        """
        if age < 0:
            raise ValueError('Age must be positive')
        self._name = name
        self._age = age

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age):
        if age < 0:
            raise ValueError('Age must be positive')
        self._age = age

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    def __str__(self):
        return f'Person({self._name}, {self._age}, {self.weight})'

    @classmethod
    def eat(cls):
        print('Eating')
        cls.weight += 1

    @classmethod
    def eat_and_watch_clock(cls):
        # cls.eat()
        Person.eat()
        Person.watch_clock()

    @staticmethod
    def watch_clock():
        print(f"Now is {datetime.now()}")

    @staticmethod
    def watch_clock_and_eat():
        Person.watch_clock()
        Person.eat()


p1 = Person('John', 20)
p2 = Person('Mary', 16)
p3 = Person('Jane', 69)

p1.name = 'Nghia'
print(p1)

print(p1.age)
print(p1._age)


try:
    p1.age = -1
except ValueError as e:
    print(e)

p1.eat()
print(p1)

p1.eat()
p1.watch_clock()
p2.watch_clock_and_eat()
p3.eat_and_watch_clock()

print(p1)
