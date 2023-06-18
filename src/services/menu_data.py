import csv
from src.models.dish import Dish
from src.models.ingredient import Ingredient


class MenuData:
    def __init__(self, source_path: str) -> None:
        self.dishes: set[Dish] = set()
        self.ingredients: set[Ingredient] = set()
        self._load_menu_data(source_path)

    def _load_menu_data(self, source_path: str) -> None:
        with open(source_path, newline="") as file:
            reader = csv.reader(file)
            next(reader)
            for row in reader:
                dish_name = row[0]
                dish_price = float(row[1])
                ingredient_name = row[2]
                recipe_amount = int(row[3])

                ingredient = Ingredient(ingredient_name)
                self.ingredients.add(ingredient)

                dish = self._find_or_create_dish(dish_name, dish_price)
                dish.add_ingredient_dependency(ingredient, recipe_amount)

    def _find_or_create_dish(self, dish_name: str, dish_price: float) -> Dish:
        for dish in self.dishes:
            if dish.name == dish_name and dish.price == dish_price:
                return dish

        dish = Dish(dish_name, dish_price)
        self.dishes.add(dish)
        return dish
