from PizzaBases import BasePizza, MargheritaPizza
from Toppings.ExtraCheese import ExtraCheeseTopping
from Toppings.Mushroom import ExtraMushroom


class CalculatePizzaCost:

    def calculate_pizza_cost(self):
        base_selected = MargheritaPizza
        topping_selected = ExtraCheeseTopping
        topping_selected_2 = ExtraMushroom
        pizza = topping_selected_2(topping_selected(base_selected())).cost()
        return pizza


if __name__ == "__main__":
    print(CalculatePizzaCost().calculate_pizza_cost())
