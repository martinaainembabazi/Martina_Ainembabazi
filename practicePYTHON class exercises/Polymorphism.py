#Polymorphism with inheritance
class Bird:
    def fly(self):
        print("Birds enjoy flying")

class Parrot(Bird):
    def fly(self):
        print("Parrots like flying while talking")

class Hen(Bird):
    def fly(self):
        print("A hen is a bird that does not fly")

 #how we use polymorphism
def flight_test(bird):
    bird.fly()   

#creating objects
parrot1=Parrot()
hen1=Hen()

flight_test(parrot1)
flight_test(hen1)

