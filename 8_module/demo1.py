
sample1=100

def get_value():
    return 200

class Circle:
    pi=3.14

    def __init__(self,radius):
        self.radius=radius
    
    def area(self):
        return self.pi*(self.radius**2)

    def circumfrence(self):
        return 2*self.pi*self.radius