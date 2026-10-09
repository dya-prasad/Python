



#1 class---->multiple objects    veedu indakkanulla plan ahn class ,undakkiya veedu ahnu class inte object
#this concept is called oops
#class blueprint of object                        smartphone,laptop,tv-->electronic category
#object member of class                            car,auto,bus--->vehicles category


#object:-->properties & methods
#car---->name,color,price----->properties
#car--->start(),run(),stop()--->method












# class cars:
#     def __init__(self,name,price,colour):           
#         self.name
#         self.price
#         self.colour

#     def start(self):
#         print(self.name + "Engine started")
# car1 =cars("maruti swift",10000,"red")                #car1.price = 15000
# car2 =cars("toyota innova",20000,"white")
# print(car1.name,car1.price,car1.colour)
# print(car2.name,car2.price,car2.colour)                #car1.start()






# class

# class students:
#     pass


#class=blueprint
#object= blueprint use cheyth undakkuna actual thing.
#example

# class student:
#     name="diya"    #<-------students data---->attributes
#     age=22

#objects 

# class student:                        #class--->student ,object--->student1
#     name="diya"
#     age=22

# student1 =student() #object creation
# print(student1.name)      #output =diya,22
# print(student1.age)



#methods       

# class student:
#     def study(self):  #------>function but its call method
#         print("student is studying")  #self (ennath ippol use cheyyuna object ne indicate cheyyunath)
# student1 =student()
# student1.study()    #----->output student is studying


#constructor


# class student:
#     def __init__(self,name,age):
#         self.name= name
#         self.age= age
#     def study(self):
#         print(self.name,"is studying")

# student1 =student("diya",22)
# student2 =student("anu",25)
# print(student1.name)
# print(student1.age)

# print(student2.name)
# print(student2.age)


#full program



# class student:
#     def __init__(self,name,age):
#         self.name= name
#         self.age= age

#     def study(self):
#         print(self.name,"is studying")

#     def display(self):
#         print("Name:",self.name)
#         print("Age:",self.age)

# student1 =student("diya",22)
# student2 =student("anu",25)

# student1.display()
# student1.study()

# print()
# student2.display()
# student2.study()



#INHERITANCE AND ENCAPSULATION

#SINGLE INHERITANCE

# class Animal:
#     def eat(self):
#         print("animal is eating")


# class Dog(Animal):
#     def bark(self):
#         print("dog is barking")


# d = Dog()
# d.eat()
# d.bark()


#MULTIPLE INHERITANCE

# class Father:
#     def driving(self):
#         print("driving")

# class Mother:
#     def cooking(self):
#         print("cooking")

# class child(Father,Mother):
#     pass


# c = child()
# c.driving()
# c.cooking()


#MULTILEVEL INHERITANCE

# class Grandfather:
#     def house(self):
#         print("Grandfather as a house")


# class Father(Grandfather):
#     pass

# class son(Father):
#     pass

# s = son()
# s. house()
    

#HIERARCHICAL INHERITANCE

# class Animal:
#     def eat(self):
#         print("animal is eating")


# class Dog(Animal):
#     def bark(self):
#         print("dog is barking")

# class cat(Animal):
#     def meow(self):
#         print("cat is meowing")


# d = Dog()
# c = cat()
# d.eat()
# d.bark()
# c.eat()
# c.meow()

#HYBRID INHERITANCE

# class A:
#     def show_a(self):
#         print("A")

# class B:
#     def show_b(self):
#         print("B")

# class C(A):
#     def show_c(self):
#         print("C")
# class D(B,C):
#     def show_d(self):
#         print("D")

# d = D()
# d.show_a()
# d.show_b()
# d.show_c()
# d.show_d()

#ENCAPSULAATION

# class Student:
#     def __init__(self,mark):
#         self.__marks =mark
#     def get_marks(self):
#         return self.__marks
#     def set_mark(self,mark):
#         self.__marks =mark

# student = Student(90)
# print(student.get_marks())
# student.set_mark(95)
# print(student.get_marks())


#POLYMORPHISM

# class Dog:
#     def action(self):
#         print("dog is running")

# class Cat:
#     def action(self):
#         print("cat is jumping")

# dog = Dog()
# cat =Cat()

# dog.action()
# cat.action()

# types
# 1.method overloading
# 2.method overriding
# 3.operator overrloading
# 4. duck typig

#METHOD OVERRINDING

# class Payment:
#     def pay(self):
#         print("payment")
# class UPI(payment):
#     def pay(self):
#         print("payment using UPI")

# class card:
#     def pay(self):
#         print("payment using card")


# p1= UPI()
# p2= card() 

#method overloading
# class Calculator:

#     def add(self, *numbers):
#         return sum(numbers)


# c = Calculator()

# print(c.add(10, 20))
# print(c.add(10, 20, 30))
# print(c.add(10, 20, 30, 40))

#operator overloading

# class Number:
#     def __init__(self, value):
#         self.value = value

#     def __add__(self, other):
#         return self.value + other.value


# num1 = Number(10)
# num2 = Number(20)

# print(num1 + num2)

#duck typing

# class Car:
#     def start(self):
#         print("Car is starting")


# class Bike:
#     def start(self):
#         print("Bike is starting")


# car = Car()
# bike = Bike()

# def start_vehicle(vehicle):
#     vehicle.start()

# start_vehicle(car)
# start_vehicle(bike)

#abstraction

from abc import ABC,abstractmethod

class Payment(ABC):
    @abstractmethod
    def pay(self):
        pass


class UPI(Payment):

    def pay(self):
        print("Payment using UPI")


payment = UPI()
payment.pay()