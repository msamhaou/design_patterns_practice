from abc import ABC, abstractmethod

class Car:
    def __init__(self):
        self.engine = None
        self.wheels = None
        self.color = None
        self.model = None
        self.brand = None

    def __str__(self):
        return f"""{self.color} {self.brand} {self.model}, Description: 
            -wheels: {self.wheels}
            -engine: {self.engine}
        """

class CarBuilder(ABC):
    def __init_(self):
        self.car = None
    @abstractmethod
    def add_engine(self):
        pass

    @abstractmethod
    def add_wheels(self):
        pass

    @abstractmethod
    def add_color(self):
        pass

    @abstractmethod
    def add_model(self):
        pass

    @abstractmethod
    def add_brand(self):
        pass

    @abstractmethod
    def get_car(self):
        return self.car
    
#Concrete Builders

class FerrariBuilder(CarBuilder):
    def __init__(self):
        self.car = Car()

    def add_engine(self):
        self.car.engine = "V12 5999 cc, patrol"
    
    def add_wheels(self):
        self.car.wheels = 4

    def add_color(self):
        self.car.color = "Red"

    def add_model(self):
        self.car.model = "599 GTB Fiorano"
    
    def add_brand(self):
        self.car.brand = "Ferrari"

    def get_car(self):
        return self.car


class ToyotaBuilder(CarBuilder):
    def __init__(self):
        self.car = Car()

    def add_engine(self):
        self.car.engine = "V4 1998 cc, gasoline"
    
    def add_wheels(self):
        self.car.wheels = 4
    def add_color(self):
        self.car.color = "Black"

    def add_model(self):
        self.car.model = "GT86 2.0 D-4S Sport"
    
    def add_brand(self):
        self.car.brand = "Ferrari"
    
    def get_car(self):
        return self.car

#director
class Director():
    def __init__(self, builder: CarBuilder):
        self.builder = builder

    def construct_car(self):
        self.builder.add_engine()
        self.builder.add_wheels()
        self.builder.add_color()
        self.builder.add_brand()
        self.builder.add_model()


if __name__ == '__main__':
    director = Director(ToyotaBuilder())
    director.construct_car()
    car = director.builder.get_car()
    print(car)