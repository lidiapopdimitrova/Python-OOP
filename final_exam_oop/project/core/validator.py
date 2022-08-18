
class Validator:
    @staticmethod
    def validate_string_is_not_empty_or_spaces(string, message):
        if string.strip() == "":
            raise ValueError(message)

    @staticmethod
    def validate_if_age_is_over_or_equal_to_18(age, message):
        if age < 18:
            raise ValueError(message)

    @staticmethod
    def string_is_less_than_a_number_of_symbols(string, min_len, message):
        if len(string) < min_len:
            raise ValueError(message)

    @staticmethod
    def horse_speed_is_within_the_limit(speed, max_speed, message):
        if speed > max_speed:
            raise ValueError(message)

    @staticmethod
    def race_type_is_valid(race, message):
        if race == "Winter" or race == "Spring" or race == "Autumn" or race == "Summer":
            return race
        return ValueError(message)

    @staticmethod
    def check_if_valid_horse_type(horse_type):
        if horse_type == "Appaloosa" or horse_type == "Thoroughbred":
            return True
        return False

    @staticmethod
    def check_if_horse_already_exists(horse_name, horse_list, message):
        for horse in horse_list:
            if horse.name == horse_name:
                raise Exception(message)

    @staticmethod
    def check_if_jockey_already_exists(jockey_list, jockey_name: str, message):
        for jockey in jockey_list:
            if jockey.name == jockey_name:
                raise Exception(message)

    @staticmethod
    def check_if_race_already_exists(race_list, race_type, message):
        for race in race_list:
            if race.race_type == race_type:
                raise Exception(message)

    @staticmethod
    def find_jockey_by_name(jockey_list, jockey_name, message):
        for jockey in jockey_list:
            if jockey.name == jockey_name:
                return jockey
        raise Exception(message)

    @staticmethod
    def find_available_horse(horses_list, horse_type, message):
        for index in range(len(horses_list) - 1, -1, -1):
            horse = horses_list[index]
            if horse.__class__.__name__ == horse_type and not horse.is_taken:
                return horse
        raise Exception(message)

    @staticmethod
    def horse_race_exists(races_list, race_type, message):
        for race in races_list:
            if race.race_type == race_type:
                return race
        raise Exception(message)

    @staticmethod
    def doesnt_have_a_horse_check(jockey_obj, message):
        if jockey_obj.horse is None:
            raise Exception(message)

    @staticmethod
    def raise_if_there_are_less_than_needed_drivers(horse_race, min_number, message):
        if len(horse_race.jockeys) < min_number:
            raise Exception(message)



