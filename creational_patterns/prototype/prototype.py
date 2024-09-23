"""
When to Use:
    -When your system should be independent of how its products are created, composed, and represented.
    -When the classes to instantiate are specified at run-time.
    -To avoid building a class hierarchy of factories that parallels the class hierarchy of products.
    -When instances of a class can have one of only a few different combinations of state.
Check list:
    -Add a clone() method to the existing "product" hierarchy.
    -Design a "registry" that maintains a cache of prototypical objects. The registry could be encapsulated in a new Factory class, or in the base class of the "product" hierarchy.
    -Design a factory method that: may (or may not) accept arguments, finds the correct prototype object, calls clone() on that object, and returns the result.
    -The client replaces all references to the new operator with calls to the factory method.

"""
import copy 

class Prototype():
    def __init__(self):
        self.objects = {}
    
    def register_obj(self, name, obj):
        self.objects[name] = obj
    
    def unregister_obj(self, name):
        del self.objects[name]
    
    def clone(self, name, **attrs):
        obj = copy.deepcopy(self.objects.get(name))
        obj.__dict__.update(attrs)
        return obj

class Car:
    def __init__(self):
        self.paint = 'Red'
        self.brand = 'ferrari'
        self.model = 'G510'

    def __str__(self):
        return f'{self.paint} {self.model} {self.brand}'


car1 = Car()
proto = Prototype()
proto.register_obj('car',car1)

car2 = proto.clone(name='car', brand= 'ferrari2')

print(car1)
print(car2)