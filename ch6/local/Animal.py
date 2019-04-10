class Animal(object):
    type = "animal"
    def __init__(self,name,age):
        self.name = name
        self.age = age
class Dog(Animal):
    def __init__(self,name,age):
        super().__init__(name, age)
    def eat(self):
        print(self.name," is eating!")
dog = Dog('dog',9000)
print(Dog.type)
print(dog.type)


