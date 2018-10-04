from beverages import *
import random

class CoffeeMachine(object):
    def __init__(self, times_used=0):
        self.times_used=0

    class EmptyCup(HotBeverage):
        def __init__(self):
            self.name="empty cup"
            self.price=0.90

        def description(self):
            return "An empty cup?! Gimme my money back!"

    class BrokenMachineException(Exception):
        def __init__(self):
            self.message="This coffee machine has to be repaired."

        def __str__(self):
            return self.message

    def repair(self):
        self.times_used=0
        return


    def serve(self, bev): #bev derives from HotBeverage (coffe, tea, ...)
        rand_num=random.randint(0,1)
        if self.times_used==10:
            raise CoffeeMachine.BrokenMachineException()
        elif rand_num==0:
            self.times_used+=1
            return CoffeeMachine.EmptyCup()
        else:
            self.times_used+=1
            return bev


if __name__ == '__main__':
    machine=CoffeeMachine()
    repaired=0
    beverages=[Coffee(),Tea(),Chocolate(),Cappuccino()]
    while repaired<2:
        try:
            rand_bev=beverages[random.randint(0,3)]
            print(machine.serve(rand_bev))
        except:
            machine.repair()
            print("\nThat repair was quick!\n")
            repaired+=1
