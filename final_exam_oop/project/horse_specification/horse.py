from abc import ABC, abstractmethod

from project.core.validator import Validator


class Horse(ABC):
    @abstractmethod
    def __init__(self, name: str, speed: int):
        self.name = name
        self.speed = speed
        self.is_taken = False

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        Validator.string_is_less_than_a_number_of_symbols(value, 4, f"Horse name {value} is less than 4 symbols!")
        self.__name = value

    @property
    def speed(self):
        return self.__speed

    @speed.setter
    def speed(self, value):
        Validator.horse_speed_is_within_the_limit(value, self.max_speed, "Horse speed is too high!")
        self.__speed = value

    @property
    @abstractmethod
    def max_speed(self):
        pass

    @abstractmethod
    def train(self):
        pass
