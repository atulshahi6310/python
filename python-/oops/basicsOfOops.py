# class 
class person :
    def __init__(self , name , age ):
      self.name =name 
      self.age = age 
    def greet(self):
        print(f"{self.name}  {self.age}")

p1 =  person("atul" , 19)
p1.greet()