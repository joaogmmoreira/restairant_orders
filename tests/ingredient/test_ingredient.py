from src.models.ingredient import Ingredient  # noqa: F401, E261, E501
from src.models.ingredient import Restriction


# Req 1
# Test
def test_ingredient():
    mussarela = Ingredient("queijo mussarela")
    bacon = Ingredient("bacon")

    assert hash(bacon) == hash("bacon")
    assert hash(mussarela) == hash("queijo mussarela")

    assert mussarela.name == "queijo mussarela"
    assert bacon.name == "bacon"

    assert (mussarela == bacon) is False
    assert (mussarela == mussarela) is True

    assert repr(mussarela) == "Ingredient('queijo mussarela')"
    assert repr(bacon) == "Ingredient('bacon')"

    assert mussarela.restrictions == {
        Restriction.LACTOSE,
        Restriction.ANIMAL_DERIVED
        }
