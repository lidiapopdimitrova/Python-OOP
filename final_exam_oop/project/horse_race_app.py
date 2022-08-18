from project.core.validator import Validator
from project.factory.horse_factory import HorseFactory
from project.factory.jockey_factory import JockeyFactory
from project.factory.race_factory import RaceFactory


class HorseRaceApp:
    def __init__(self):
        self.horses = []
        self.jockeys = []
        self.horse_races = []

    def add_horse(self, horse_type: str, horse_name: str, horse_speed: int):
        if Validator.check_if_valid_horse_type(horse_type):
            Validator.check_if_horse_already_exists(horse_name, self.horses, f"Horse {horse_name} has been already added!")
            horse = HorseFactory.create_a_horse(horse_type, horse_name, horse_speed)
            self.horses.append(horse)
            return f"{horse_type} horse {horse_name} is added."

    def add_jockey(self, jockey_name: str, age: int):
        Validator.check_if_jockey_already_exists(self.jockeys, jockey_name, f"Jockey {jockey_name} has been already added!")
        jockey = JockeyFactory.create_a_jockey(jockey_name, age)
        self.jockeys.append(jockey)
        return f"Jockey {jockey_name} is added."

    def create_horse_race(self, race_type: str):
        Validator.check_if_race_already_exists(self.horse_races, race_type, f"Race {race_type} has been already created!")
        race = RaceFactory.create_race(race_type)
        self.horse_races.append(race)
        return f"Race {race_type} is created."

    def add_horse_to_jockey(self, jockey_name: str, horse_type: str):
        jockey = Validator.find_jockey_by_name(self.jockeys, jockey_name, f"Jockey {jockey_name} could not be found!")
        horse = Validator.find_available_horse(self.horses, horse_type, f"Horse breed {horse_type} could not be found!")

        if jockey.horse is not None:
            return f"Jockey {jockey_name} already has a horse."

        horse.is_taken = True
        jockey.horse = horse
        return f"Jockey {jockey_name} will ride the horse {horse.name}."

    def add_jockey_to_horse_race(self, race_type: str, jockey_name: str):
        race = Validator.horse_race_exists(self.horse_races, race_type, f"Race {race_type} could not be found!")
        jockey = Validator.find_jockey_by_name(self.jockeys, jockey_name, f"Jockey {jockey_name} could not be found!")

        Validator.doesnt_have_a_horse_check(jockey, f"Jockey {jockey_name} cannot race without a horse!")

        if jockey in race.jockeys:
            return f"Jockey {jockey_name} has been already added to the {race_type} race."

        race.jockeys.append(jockey)
        return f"Jockey {jockey_name} added to the {race_type} race."

    def start_horse_race(self, race_type: str):
        race = Validator.horse_race_exists(self.horse_races, race_type, f"Race {race_type} could not be found!")
        Validator.raise_if_there_are_less_than_needed_drivers(race, 2, f"Horse race {race_type} needs at least two participants!")

        jockeys_sorted = sorted(race.jockeys, key=lambda x: -x.horse.speed)
        winner = jockeys_sorted[0]
        return f"The winner of the {race_type} race, with a speed of {winner.horse.speed}km/h is {winner.name}!" \
               f" Winner's horse: {winner.horse.name}."
