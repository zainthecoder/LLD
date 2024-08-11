from Faiz.DecoratorDesignPattern.PizzaBases.basepizza import BasePizza


class ExtraMushroom(BasePizza):

    def __init__(self, base_pizza: BasePizza):
        self.pizza = base_pizza

    def cost(self):
        return self.pizza.cost()+10
