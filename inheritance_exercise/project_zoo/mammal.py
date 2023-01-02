from inheritance_exercise import Animal


class Mammal(Animal):
    def __init__(self, name):
        super().__init__(name)