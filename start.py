# class Cat
class Cat:

    def __init__(self, woolColor, eyesColor, name):
        self.woolColor = woolColor
        self.eyesColor = eyesColor
        self.name = name

    def purr(self):
        print("mrrr")

    def scrabble(self):
        print("krkrkrkr")

    def allInOne(self):
        self.purr()
        self.scrabble()
        return "Continue?"


myCat = Cat("black", "green", "Timea")

print(myCat.name)
print(myCat.allInOne())