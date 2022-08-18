from project.horse_specification.horse import Horse


class Appaloosa(Horse):
    def __init__(self, name: str, speed: int):
        super().__init__(name, speed)
        self.train_increase = 2

    @property
    def max_speed(self):
        return 120

    def train(self):
        self.speed += self.train_increase
        if self.speed > self.max_speed:
            self.speed = self.max_speed
        return self.speed