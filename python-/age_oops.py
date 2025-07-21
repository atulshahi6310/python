class ageFinder :
    def __init__(self , age):
        self.age = age 
    def greet(self):
        if self.age >= 18 :
            print( "eligible for drive" )
obj1 = ageFinder(19)
obj1.greet()