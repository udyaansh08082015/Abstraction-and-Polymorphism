from abc import ABC, abstractmethod
class animal(ABC):

    def move(self):
        pass 

class Human(animal):
    def move(self):
        print("I can walk and run")

class Snake(animal):
    def move(self):
        print("I can slither")

class Dog(animal):
    def move(self):
        print("I can bark and jump")


class Lion(animal):
    def move(self):
        print("I can hunt and roar")


human = Human()
human.move()


snake = Snake()
snake.move()

dog = Dog()
dog.move()

lion = Lion()
lion.move()