import pytest
from src.menu import Menu

def test_exercise(capsys):
    menu = Menu()
    menu.add_meal("Tofu ratatouille")

    menu.print_meals()
    out,err = capsys.readouterr()
    assert out == "Tofu ratatouille\n"

    menu.clear_menu()
    menu.add_meal("Tomato and mozzarella salad")
    menu.print_meals()
    out,err = capsys.readouterr()
    assert out == "Tomato and mozzarella salad\n"
