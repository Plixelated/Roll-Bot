
import random

class dice():
    def __init__(self, sides):
        self.__sides = sides

    def roll(self):
        return random.randint(1,self.__sides)

    def roll_adv(self):
        roll1 = random.randint(1,self.__sides)
        roll2 = random.randint(1,self.__sides)
        if roll1 >= roll2:
            print(f'{roll1},{roll2}')
            return roll1
        else:
            print(f'{roll1},{roll2}')
            return roll2

    def roll_dis(self):
        roll1 = random.randint(1,self.__sides)
        roll2 = random.randint(1,self.__sides)
        if roll1 <= roll2:
            print(f'{roll1},{roll2}')
            return roll1
        else:
            print(f'{roll1},{roll2}')
            return roll2
    
    def roll_multi(self, times):
        rollArr = []
        for i in range(times):
            rollArr.append(self.roll())
        return rollArr
    
    def roll_multi_adv(self, times):
        rollArr = []
        for i in range(times):
            rollArr.append(self.roll_adv())
        return rollArr

    def roll_multi_dis(self, times):
        rollArr = []
        for i in range(times):
            rollArr.append(self.roll_dis())
        return rollArr
