from src.models.ingredient import (
    Ingredient,
    Restriction,
)  # noqa: F401, E261, E501


# Req 1
def test_ingredient():
    ingredient = Ingredient("tomate")
    assert ingredient.name == "tomate"
    assert ingredient.restrictions == set()

    ingredient = Ingredient("presunto")
    expected_restrictions = {
        Restriction.ANIMAL_MEAT,
        Restriction.ANIMAL_DERIVED,
    }
    assert ingredient.restrictions == expected_restrictions

    # repr
    ingredient = Ingredient("tomate")
    assert repr(ingredient) == "Ingredient('tomate')"

    # eq
    ingredient1 = Ingredient("tomate")
    ingredient2 = Ingredient("tomate")
    ingredient3 = Ingredient("presunto")
    assert ingredient1 == ingredient2
    assert ingredient1 != ingredient3

    # hash
    ingredient1 = Ingredient("tomate")
    ingredient2 = Ingredient("tomate")
    ingredient3 = Ingredient("presunto")
    assert hash(ingredient1) == hash(ingredient2)
    assert hash(ingredient1) != hash(ingredient3)
