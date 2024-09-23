from abc import ABC, abstractmethod

"""
When to Use the Factory Method Pattern:
    -When a Class Cannot Anticipate the Type of Objects to Create: If a class needs to delegate the responsibility of object creation to its subclasses.
    -When You Want to Localize the Knowledge of Which Helper Class is Required: This is useful when the exact type of the object being created varies.
    -To Favor Composition over Inheritance: By using Factory Methods, you can change the created objects by changing the factory, reducing dependency on concrete classes.
    -When the Creation Process is Complex: If the creation involves a multi-step process, encapsulating this process in a factory makes the client code simpler.
"""

#abstract product
class Consumable(ABC):
    def __init__(self):
        self.stat = ''
        self.value = 0

    def __str__(self):
        return f'{self.stat} + {self.value}'

    # @abstractmethod
    # def consume(self):
    #     return self.value
    
#Concrete Products
class ManaPotion(Consumable):
    def __init__(self):
        self.stat = 'mana'
        self.value = 10
    
class HealthPotion(Consumable):
    def __init__(self):
        self.stat = 'health'
        self.value = 10

class FireResistancePotion(Consumable):
    def __init__(self):
        self.stat = 'fire_resist'
        self.value = 20

#Abstract Creator

class Consumer(ABC):
    def __init__(self):
        self.mana = 0
        self.health = 10
    def create_consumable(self) -> Consumable:
        pass

    def new_consumable(self) -> Consumable:
        consumable = self.create_consumable()
        consumable.consume()
        return consumable
    
class Berserk(Consumer):
    def create_consumable(self):
        health = HealthPotion()
        return health

class Sorcier(Consumer):
    def create_consumable(self):
        mana = ManaPotion()
        return mana


if __name__ == '__main__':
    stat = input("Please enter stats: ")

    if stat == 'Mana':
        consumer = Sorcier()
    elif stat == 'Health':
        consumer = Berserk()
    else:
        raise ValueError('No Stats')

    consumable = consumer.create_consumable()
    print(consumable)


    