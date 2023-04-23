from src.models.ingredient import Ingredient
from src.models.dish import Dish
import csv
# Req 3


class MenuData:
    def __init__(self, source_path: str) -> None:
        self.dishes = set()

        with open(source_path, mode="r") as file:
            data = csv.DictReader(file)

            data_dishes = {}

            for row in data:
                float_price = float(row["price"])
                int_qnty = int(row["recipe_amount"])

                if row["dish"] not in data_dishes:
                    data_dishes[row["dish"]] = Dish(row["dish"], float_price)

                data_dishes[row["dish"]].add_ingredient_dependency(
                    Ingredient(row["ingredient"]),
                    int_qnty
                    )

                self.dishes = set(data_dishes.values())
