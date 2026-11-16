from abc import ABC,abstractmethod


class absclass(ABC):
    def print(self,x):
        print("Passed Value",x)


    @abstractmethod
    def task(self):
        print(" we are inside absclass")


class Test_Class(absclass):
    def task(self):
        print("We are inside Test Class")

obj = Test_Class()
obj.task()
obj.print(10982)
