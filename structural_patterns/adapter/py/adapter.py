class Computer:
    def __init__(self, name):
        self.name = name;
    
    def __str__(self):
        return f'the computer {self.name}'

    def execute(self):
        return f' excute a prog'

class Human:
    def __init__(self, name):
        self.name = name

    def __str__(self) :
        return f'person {self.name}'

    def _speak(self):
        return f'speaking command'

class Synthesizer:
    def __init__(self, name):
        self.name = name
    
    def __str__(self) :
        return f'Synthesizer {self.name}'

    def _play(self):
        return f'playing song'

class Adapter:
    def __init__(self, obj, **adapted_method):
        self.obj = obj
        self.__dict__.update(adapted_method)

    def __str__(self):
        return str(self.obj)

if __name__ == "__main__":
    computer = Computer('Asus')
    human = Human('taha')

    adapter = Adapter(human, execute= human._speak)
    print(adapter.execute())