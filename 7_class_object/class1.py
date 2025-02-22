

#class 
#class is a blueprint of an object

#object
#its a instance of a class

#class attribute
#variable which are common for all object


#constructor
#function which is called when you create an object


#object /instance attribute
#this is unique for each student

class Student:
    dress_code='while'
    scool_name='oxford'

    #contructor
    def __init__(self,name,email,phone,roll_no):
        self.name=name
        self.email=email
        self.phone=phone
        self.roll_no=roll_no

s1=Student('akshay','akshay@gmail.com',8999999,10)
s2=Student('vikas','vikas@gmail.com',999999999,20)

print(s1.name)
print(s2.name)