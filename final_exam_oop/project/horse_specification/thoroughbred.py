from project.horse_specification.horse import Horse


class Thoroughbred(Horse):
    def __init__(self, name: str, speed: int):
        super().__init__(name, speed)
        self.train_increase = 3

    @property
    def max_speed(self):
        return 140

    def train(self):
        self.speed += self.train_increase
        if self.speed > self.max_speed:
            self.speed = self.max_speed
        pass