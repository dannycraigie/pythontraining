#class Dog:
    #energy = "High"

#    def __init__(self, energy, foodtype = "dry", barkvol = "Loud"):
#        self.energy = energy
#        self.foodtype = foodtype
#        self.barkvol = barkvol
#
#    def speak(self):
#        print("Woof")

#lassie = Dog("High", "Wet")

#clifford = Dog("Low")

#shep = Dog("Superhigh", "Wet")

#lassie.speak()
#clifford.speak()
#print(lassie.energy)
#print(clifford.energy)
#print(shep.energy, shep.barkvol)
#print("Lassie eats", lassie.foodtype, "food")
#print("shep eats", shep.foodtype, "food")
#print("clifford eats", clifford.foodtype, "food")

class Students:

    def __init__(self, name, age, class_ = "Default"):
        self.name = name
        self.age = age
        self.class_ = class_

    def test_score(self, a:int, b:int, c:int):
        avg=(a+b+c)/3
        avg = round(avg)
        return(avg)

danny = Students("Danny", 46, "Python, Linux & Git")
andy = Students("Andy", 40)
tracy = Students("Tracy", 24) 

print(danny.name, "is", danny.age, "he studies", danny.class_, 
"with an avg test result of", danny.test_score(84, 68, 83))

        


