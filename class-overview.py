class Person:
    def __init__(self,gender,name):
        self.gender = gender
        self.name = name
    def display(self):
        print("You're a ", self.gender ,", and you're name is: ", self.name)
    
people = Person('Male','Alex')
people.display()