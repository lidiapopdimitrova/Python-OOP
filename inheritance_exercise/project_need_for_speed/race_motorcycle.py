from inheritance_exercise import Motorcycle


class RaceMotorcycle(Motorcycle):
    DEFAULT_FUEL_CONSUMPTION = 8

    def __init__(self, fuel, horse_power):
        super().__init__(fuel, horse_power)
        self.fuel_consumption = self.DEFAULT_FUEL_CONSUMPTION

    def drive(self, kilometers):
        if self.fuel - kilometers * self.fuel_consumption >= 0:
            self.fuel -= kilometers * self.fuel_consumption