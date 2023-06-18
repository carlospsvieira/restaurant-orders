from src.models.dish import Dish
from src.models.ingredient import Ingredient
import pytest


def test_dish():
    dish = Dish("Sushi_box", 45.99)
    assert dish.name == "Sushi_box"
    assert dish.price == 45.99
    assert dish.recipe == {}

    # eq and hash
    dish2 = Dish("Sushi_box", 45.99)
    dish3 = Dish("Churrasco_individual", 39.99)
    assert dish == dish2
    assert dish != dish3
    assert hash(dish) == hash(dish2)
    assert hash(dish) != hash(dish3)

    # repr
    assert repr(dish) == "Dish('Sushi_box', R$45.99)"

    # testing add_ingredient_dependency
    ingredient1 = Ingredient("Calabresa")
    ingredient2 = Ingredient("Tomate")
    dish.add_ingredient_dependency(ingredient1, 2)
    dish.add_ingredient_dependency(ingredient2, 1)
    assert dish.recipe == {ingredient1: 2, ingredient2: 1}

    # testing get_restrictions
    restrictions = dish.get_restrictions()
    assert restrictions == set()

    # testing get_ingredients
    ingredients = dish.get_ingredients()
    expected_ingredients = {ingredient1, ingredient2}
    assert set(ingredients) == expected_ingredients

    with pytest.raises(TypeError):
        Dish("Sushi_box", "45.99")
    with pytest.raises(ValueError):
        Dish("Sushi_box", -45.99)
