from abc import ABC, abstractmethod 
#Abstraction is king that cant operate on a kingdom directly
#Refined Abstractions : a king with advanced permession
#Implementor : abstract Class of Lords
#concrete implementors: puppet Lords used to operate on that non loyal city

#Abstract Implementor
class Lord(ABC):
    def __init__(self, name, city):
      self.name = name
      self.city = city
    @abstractmethod
    def build_city(self) ->str :
        pass
    @abstractmethod
    def attack(self, city:str) -> str :
        pass
    # @abstractmethod
    # def trade():
    #     pass

class Nobel(Lord):
    def __init__(self, name, city):
        super().__init__(name, city);

    def build_city(self):
        return f'by your order {self.city} is build';

    def attack(self, city:str) -> str :
        return f'by your order {self.city} is attacking {city}'



#Abstraction
class Monarch(ABC):
    def __init__(self, puppet:Lord):
      self._puppet = puppet

    @abstractmethod
    def _build_city(self) -> str :
        pass

    @abstractmethod
    def _attack(self,city:str) -> str:
        pass

    # @abstractmethod
    # def _trade():
    #     pass

# cocrete abstraction
class King(Monarch):
    def __init__(self, puppet:Lord):
        super().__init__(puppet)

    def _build_city(self):
        return self._puppet.build_city();
    
    def _attack(self, city:str) -> str:
        return self._puppet.attack(city);


if __name__ == "__main__" :
    jean = Nobel(name='Jean-Baptiste Colbert', city='Agadir');
    Francoi = Nobel(name='François de Neufville', city='Berkane')
    city = input('City you wanna operate: ').lower();
    nobel = jean if city == str('Agadir').lower() else Francoi
    Louis_XIV = King(nobel);
    build = Louis_XIV._build_city();
    attack = Louis_XIV._attack(city='England')
    print(attack)