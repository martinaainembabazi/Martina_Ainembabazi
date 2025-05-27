class Insect:
    def live(self):
        print("The insects can live in either water or land")

class Mosquito(Insect):
    def live(self):
        print("This insect lives on land")

class Chameleon(Insect) :
    def live(self):
        print("This insect lives on water")


i=Insect()
m=Mosquito()
c=Chameleon()
i.live()
m.live()
c.live()                       