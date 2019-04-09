class Animal(object):
    def __init__(self,name,age):
        self.name = name
        self.age = age
class Dog(Animal):
    def __init__(self,name,age):
        super().__init__(name, age)
    def eat(self):
        print("Dog is eating!")
class Cat(Animal):
    def __init__(self,name,age):
        super().__init__(name, age)
    def eat(self):
        print("Cat is eating!")