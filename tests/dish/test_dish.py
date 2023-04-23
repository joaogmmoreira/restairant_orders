from src.models.dish import Dish  # noqa: F401, E261, E501
from src.models.ingredient import Restriction, Ingredient
import pytest


# Req 2
def test_dish():
    strogonoff = Dish("strogonoff", 42.90)
    ravioli_de_camarao = Dish("Ravioli de Camarão", 59.90)

    carne = Ingredient("carne")
    creme_de_leite = Ingredient("creme de leite")
    massa_de_ravioli = Ingredient("massa de ravioli")
    camarao = Ingredient("camarão")

    strogonoff.add_ingredient_dependency(creme_de_leite, 1)
    strogonoff.add_ingredient_dependency(carne, 2)

    ravioli_de_camarao.add_ingredient_dependency(massa_de_ravioli, 2)
    ravioli_de_camarao.add_ingredient_dependency(camarao, 2)

    assert strogonoff.name == "strogonoff"
    assert ravioli_de_camarao.name == "Ravioli de Camarão"

    assert (hash(strogonoff) != hash(strogonoff)) is False
    assert (hash(strogonoff) != hash(ravioli_de_camarao)) is True

    assert (strogonoff == ravioli_de_camarao) is False
    assert (strogonoff == strogonoff) is True

    assert repr(strogonoff) == "Dish('strogonoff', R$42.90)"
    assert repr(ravioli_de_camarao) == "Dish('Ravioli de Camarão', R$59.90)"

    assert carne in strogonoff.recipe
    assert creme_de_leite in strogonoff.recipe
    assert camarao in ravioli_de_camarao.recipe
    assert massa_de_ravioli in ravioli_de_camarao.recipe

    assert strogonoff.get_ingredients() == {
        carne,
        creme_de_leite
    }

    assert ravioli_de_camarao.get_ingredients() == {
        massa_de_ravioli,
        camarao
    }

    assert ravioli_de_camarao.get_restrictions() == {
        Restriction.LACTOSE,
        Restriction.GLUTEN,
        Restriction.ANIMAL_MEAT,
        Restriction.SEAFOOD,
        Restriction.ANIMAL_DERIVED
    }

    with pytest.raises(TypeError, match="Dish price must be float."):
        Dish("moqueca", "140")

    with pytest.raises(
        ValueError, match="Dish price must be greater then zero."
    ):
        Dish("picanha", -2)
