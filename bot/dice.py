
import random

class dice():
    def __init__(self, sides):
        self.__sides = sides

    def roll(self):
        return random.randint(1,self.__sides)

    def roll_adv(self):
        rolls = []
        rolls.append(random.randint(1,self.__sides))
        rolls.append(random.randint(1,self.__sides))
        return rolls

    def roll_dis(self):
        rolls = []
        rolls.append(random.randint(1,self.__sides))
        rolls.append(random.randint(1,self.__sides))
        return rolls
    
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
    
    def get_multi_adv_total(self, rolls):
        total = []
        for set in rolls:
            total.append(max(set))
        return sum(total)
    
    def get_multi_dis_total(self, rolls):
        total = []
        for set in rolls:
            total.append(min(set))
        return sum(total)   
