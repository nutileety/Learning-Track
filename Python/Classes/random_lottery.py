from random import choice

class Lottery:
    def __init__(self):
        self.lottery_series = [1,2,3,4,5,6,7,8,9,0,'a','b','c','d','e']
        self.results = []

    def show_lottery(self):
        for possibility in range(4):
            possibility = choice(self.lottery_series)
            print("The generating series is:",possibility)
            self.results.append(possibility)
        return self.results

    def wining_series(self,win=[1,'b',3,8]):
        if self.results == win:
            print
    
lottery = Lottery()
print(lottery.show_lottery())
