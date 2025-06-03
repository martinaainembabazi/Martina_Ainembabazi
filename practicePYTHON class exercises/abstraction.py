#import ABC and the abstract method
from abc import ABC,abstractmethod


class Vehicle(ABC):
    @abstractmethod
    def start(self):
        pass #This method start has no implementation


class Motorbike(Vehicle):
    def start(self):
        print("Motorbike engine starts")

class Toyota(Vehicle):
    def start(self):
        print("Toyota engine starts")

#cant create object of abstract class
# vehicle1=vehicle()#this woud raise an error

motorbike1=Motorbike() 
toyota1=Toyota()  
motorbike1.start()   
toyota1.start()   

#Exercise
#Submit your work for Method overriding,method overloading,method overloading and MRO