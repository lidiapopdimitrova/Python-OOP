
from polimorphism_and_abstraction_exercise.project_animals.animals.animal import Mammal


class Mouse(Mammal):
    def __init__(self, name, weight, living_region):
        super().__init__(name, weight, living_region)

    @property
    def allowed_foods(self):
        return ['Vegetable', 'Fruit']

    @property
    def weight_incremental(self):
        return 0.1

    def make_sound(self):
        return "Squeak"


class Dog(Mammal):
    def __init__(self, name, weight, living_region):
        super().__init__(name, weight, living_region)

    @property
    def allowed_foods(self):
        return ['Meat']

    @property
    def weight_incremental(self):
        return 0.4

    def make_sound(self):
        return "Woof!"


class Cat(Mammal):
    def __init__(self, name, weight, living_region):
        super().__init__(name, weight, living_region)

    @property
    def allowed_foods(self):
        return ['Meat', 'Vegetable']

    @property
    def weight_incremental(self):
        return 0.30

    def make_sound(self):
        return "Meow"


class Tiger(Mammal):
    def __init__(self, name, weight, living_region):
        super().__init__(name, weight, living_region)

    @property
    def allowed_foods(self):
        return ['Meat']

    @property
    def weight_incremental(self):
        return 1.0

    def make_sound(self):
        return "ROAR!!!"

