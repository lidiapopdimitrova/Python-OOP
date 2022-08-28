from project_exam.bakery import Bakery

bakery = Bakery("name")
print(bakery.add_table("OutsideTable", 55, 15))
print(bakery.add_table("InsideTable", 3, 10))
print(bakery.add_food("Cake", "Carrot", 44))
print(bakery.add_food("Cake", "Apple", 94))
print(bakery.reserve_table(55))
print(bakery.add_drink("Tea", "peach", 300, "nestle"))
print(bakery.add_drink("Tea", "Cherry", 300, "nestle"))


print(bakery.order_food(55, "Carrot", "Apple", "Fanta"))
print(bakery.order_drink(55, "peach", "Apple", "Fanta"))
print(bakery.leave_table(55))


print(bakery.get_free_tables_info())

print(bakery.get_total_income())