
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
if __name__=='__main__': 
    print('this is inside demo1')