class Validator:
    @staticmethod
    def raise_if_string_is_empty_or_spaces(string, message):
        if string.strip() == "":
            raise ValueError(message)

    @staticmethod
    def raise_number_is_zero_or_below(number, message):
        if number <= 0:
            raise ValueError(message)

    @staticmethod
    def raise_if_number_not_in_range(number: int, min_value, max_value, message):
        if number < min_value or number > max_value:
            raise ValueError(message)

    @staticmethod
    def find_table_by_table_number(table_number):
        pass

