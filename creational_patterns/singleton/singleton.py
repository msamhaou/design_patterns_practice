"""
Intent:
    -Single Instance: The class is responsible for creating and maintaining its one and only instance.
    -Global Access Point: The class provides a way to access its unique instance from anywhere in the program.
    -Lazy Initialization: The instance is typically created when it's first requested, not when the class is loaded.
When to Use Singleton:
    -When you need exactly one instance of a class, and it must be accessible to clients from a well-known access point.
    -When the sole instance should be extensible by subclassing, and clients should be able to use an extended instance without modifying their code.
"""

class Singleton:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(cls).__new__(cls)
            cls._instance.initialize()
        return cls._instance
    
    def initialize(self):
        self.some_attr = "Init value"
    
    def do_smt(self):
        return 'M acting'

if __name__ == '__main__':
    s = Singleton()
    print(s.do_smt())
