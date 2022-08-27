from project_exam.baked_food.bread import Bread
from project_exam.baked_food.cake import Cake
from project_exam.drink.tea import Tea
from project_exam.drink.water import Water
from project_exam.table.inside_table import InsideTable
from project_exam.table.outside_table import OutsideTable


class FoodFactory:
    @staticmethod
    def create_food(food_type: str, name: str, price: float):
        if food_type == "Cake":
            return Cake(name, price)
        if food_type == "Bread":
            return Bread(name, price)
    @staticmethod
    def create_drink(drink_type: str, name: str, portion: int, brand : str):
        if drink_type == "Tea":
            return Tea(name, portion, brand)
        if drink_type == "Water":
            return Water(name, portion, brand)

    @staticmethod
    def create_table(table_type: str, table_number: int, capacity: int):
        if table_type == "InsideTable":
            return InsideTable(table_number, capacity)
        if table_type == "OutsideTable":
            return OutsideTable(table_number, capacity)

