#Father Mother Skills
class Father:
    def skill(self):
        print("Hunting")

class Mother:
    def skill(self):
        print("Cooking")


class Child(Mother,Father):
            pass


c=Child()
c.skill()   
 
