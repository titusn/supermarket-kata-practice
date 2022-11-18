from shopping_cart import ShoppingCart, UnderflowError
from item import Item
import pytest

@pytest.fixture
def shopping_cart():
    return ShoppingCart()

def test_new_shopping_cart_starts_with_0_items(shopping_cart):
    assert shopping_cart.item_count == 0

def test_after_adding_an_item_shopping_cart_contains_1_item(shopping_cart):
    shopping_cart.add("Garlic")
    assert shopping_cart.item_count == 1

def test_removing_single_item_empties_cart(shopping_cart):
    shopping_cart.add("Cucumber")
    shopping_cart.remove("Cucumber")
    assert shopping_cart.item_count == 0

def test_error_when_removing_item_from_empty_cart(shopping_cart):
     with pytest.raises(UnderflowError):
         shopping_cart.remove("Cucumber")

def test_after_adding_2_items_shopping_cart_contains_2_items(shopping_cart):
    shopping_cart.add("Garlic")
    shopping_cart.add("Onions")
    assert shopping_cart.item_count == 2

def test_after_adding_2_items_and_removing_last_item_shopping_cart_contains_first_item(shopping_cart):
    shopping_cart.add("Garlic")
    shopping_cart.add("Onions")
    shopping_cart.remove("Onions")
    assert shopping_cart.items() == ["Garlic"]

def test_total_price_is_price_of_single_item(shopping_cart):
    item = Item("Carrot", 0.40)
    shopping_cart.add(item)
    assert shopping_cart.total_price() == 0.40

def test_given_shopping_cart_with_single_item_total_price_is_price_of_that_item(shopping_cart):
    item = Item("Stick", 0.50)
    shopping_cart.add(item)
    assert shopping_cart.total_price() == 0.50

def test_given_shopping_cart_with_2_items_total_price_is_their_price_sum(shopping_cart):
    stick = Item("Stick", 0.50)
    carrot = Item("Carrot", 0.40)
    
    shopping_cart.add(stick)
    shopping_cart.add(carrot)
    
    assert shopping_cart.total_price() == 0.90