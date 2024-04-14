from abc import ABC, abstractmethod


class Pizza(ABC):

    @abstractmethod
    def prepare(self):
        pass

    @abstractmethod
    def bake(self):
        pass

    @abstractmethod
    def serve(self):
        pass


class CheesyPizza(Pizza):

    def prepare(self):
        print('preparing cheesy...')

    def bake(self):
        print('baking cheesy...')

    def serve(self):
        print('serving cheesy...')


class VeggiePizza(Pizza):

    def prepare(self):
        print('preparing cheesy...')

    def bake(self):
        print('baking cheesy...')

    def serve(self):
        print('serving cheesy...')


class PizzaFactory(ABC):

    @abstractmethod
    def create_pizza(self):
        pass


class CheesyPizzaFactory(PizzaFactory):

    def create_pizza(self):
        return CheesyPizza()


class VeggiePizzaFactory(PizzaFactory):

    def veggie_pizza(self):
        return VeggiePizza()
    


cheesy = CheesyPizzaFactory()
cheesy_inst = cheesy.create_pizza()
cheesy_inst.prepare()
cheesy_inst.bake()
cheesy_inst.serve()



