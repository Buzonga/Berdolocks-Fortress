import random

class Dice:

    @staticmethod
    def roll(number_dices):
        result = 0
        for i in range(number_dices):
            roll = random.randint(1, 6)
            result += roll
        return result