from abc import ABC, abstractmethod

#abstruct product 
class Sword(ABC):
    @abstractmethod
    def spell(self):
        pass


#concrete products
class FireSword(Sword):
    def spell(self):
        print('fire ring')

class WingSword(Sword):
    def spell(self):
        print('turnado')

#abstract factory
class Environment(ABC):
    def __init__(self):
        self.name = None
    @abstractmethod
    def create_weapon(self):
        pass

#concrete factories
class FireKingdom(Environment):
    def __init__(self):
        self.name = 'fireKingdom'
    def create_weapon(self):
        return FireSword()
    pass

class Turnamida(Environment):
    def __init__(self):
        self.name = 'turnamida'
    def create_weapon(self):
        return WingSword()
    pass


class Player(object):
    def __init__(self):
        self.sword = None
        self.world = None

    def set_world(self, factory: Environment):
        self.world = factory.name
        self.sword = factory.create_weapon()

if __name__ == '__main__' :
    player = Player()
    ll = Turnamida()

    player.set_world(ll)
    player.sword.spell()