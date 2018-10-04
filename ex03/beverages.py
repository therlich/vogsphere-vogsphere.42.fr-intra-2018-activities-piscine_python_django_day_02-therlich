class HotBeverage(object):
    def __init__(self):
        self.price=0.30
        self.name="hot beverage"

    def description(self):
        return "Just some hot water in a cup."

    def __str__(self):
        return "name : {}\nprice : {:.2f}\ndescription : {}".format(self.name, self.price, self.description())

class Coffee(HotBeverage):
    def __init__(self):
        self.name="coffee"
        self.price=0.40

    def description(self):
        return "A coffee, to stay awake."

class Tea(HotBeverage):
    def __init__(self):
        HotBeverage.__init__(self)
        self.name="tea"

class Chocolate(HotBeverage):
    def __init__(self):
        self.name="chocolate"
        self.price=0.50

    def description(self):
        return "Chocolate, sweet chocolate..."

class Cappuccino(HotBeverage):
    def __init__(self):
        self.name="cappuccino"
        self.price=0.45

    def description(self):
        return "Un po’ di Italia nella sua tazza!"


if __name__ == '__main__':

    my_beverage=HotBeverage()
    my_coffee=Coffee()
    my_tea=Tea()
    my_chocolate=Chocolate()
    my_cappuccino=Cappuccino()

    print(my_beverage)
    print(my_coffee)
    print(my_tea)
    print(my_chocolate)
    print(my_cappuccino)
