import json

# Object Oriented Programming

    # OOP Basics
from csv import list_dialects


print("OOP Basics")
print("")
        #Dog Example
print("Dog Example:")
print("")
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        print("bark")

    def add_one(self, x):
        return x + 1   
    
    def get_name(self):
        return self.name
    def get_age(self):
        return self.age
    def set_age(self, age):
        self.age = age

d = Dog("Leo", 34)
print("Name: " + d.get_name())
print("Age: " + str(d.get_age()))
d.set_age(25)
print("New Age: " + str(d.get_age()))
d2 = Dog("Bill", 12)
print("Name: " + d2.get_name())
print("Age: " + str(d2.get_age()))
d.set_age(10)
print("New Age: " + str(d2.get_age()))
d.bark()
print(d.add_one(5))
print(type(d))
print("")
print("")


        # Class Manager Example
print("Class Manager Example:")
print("")
print("No Printed Messages")
class Student: 
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age 
        self.grade = grade # 0 - 100

    def get_grade(self):
        return self.grade

class Course:
    def __init__(self, name, max_students):
        self.name = name 
        self.max_students = max_students 
        self.students = []
    
    def add_student(self, student):
        if len(self.students) < self.max_students:
            self.students.append(student)
            return True
        return False
    
    def get_average_grade(self):
        value = 0
        for student in self.students:
            value += student.get_grade()

            return value / len(self.students)

s1 = Student("Tim", 19, 95)
s2 = Student("Bill", 19, 75)
s3 = Student("Jill", 19, 65)

course = Course("Science", 2)
course.add_student(s1)
course.add_student(s2)
print("")
print("")

    # Inheritance 
print("Inheritance")
print("")
class Organism:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        print(f"I am {self.name} and I am {self.age} years old")

    def speak(self):
        print("I can't talk")

class Human(Organism):
    def speak(self):
        print("Hello")

class Cat(Organism): 
    def __init__(self, name, age, color):
        super().__init__(name, age)
        self.color = color 
        
    def show(self):
        print(f"I am {self.name} and I am {self.age} years old and I am {self.color}")

    def speak(self):
        print("Meow")
        
class Dog(Organism): 
    def speak(self):
        print("Bark")

class Mute(Organism):
    pass

h = Human("Leo", 19)
h.show()
h.speak()
c = Cat("Bill", 34, "Brown")
c.show()
c.speak()
d = Dog("Jill", 25)
d.show()
d.speak()
m = Mute("Bob", 42)
m.show()
m.speak()
print("")
print("")
print("")

    # Static and Class Methods and Attributes
print("Static and Class Methods and Attributes")
print("")

#Class Methods
print("Class Methods:")
print("")

class Person:
    #Class Attribute 
    number_of_people = 0


    def __init__(self, name):
        self.name = name
        Person.add_person()
    #Class Methods
    @classmethod
    def number_of_people_(cls):
        return cls.number_of_people()
    @classmethod 
    def add_person(cls):
        cls.number_of_people += 1
p1 = Person("Leo")
p2 = Person("Jill")
print(Person.number_of_people)
print("")
print("")

#Static Methods
print("Static Methods:")
print("")

class Math:
    @staticmethod 
    def  add5(x):
        return x + 5

    @staticmethod
    def add10(x):
        return x + 10

    @staticmethod 
    def pr():
        print("run")

print(Math.add5(5))
print(Math.add10(5))
Math.pr()
print("")
print("")
print("")


#Introduction to Software Design
print("Introduction to Software Design")
print("")

# Example 1  - Common Design Mistakes
print("Example 1 - Common Design Mistakes")
print("")
# Program Goal: Print a list of words delimited my commas

#Solution 1 (WRONG)
print("Wrong Solution:")
print("")

list_of_words = ["hello", "yes", "goodbye", "last"]
print(list_of_words[0] + "," + list_of_words[1] + "," + list_of_words[2] + "," + list_of_words[3])
print("")
print("")

#Solution 2 (Not as Bad)

print("Not as Bad:")
print("")

list_of_words = ["hello", "yes", "goodbye", "last"]
to_print = ""

for i in range(4):
    to_print += list_of_words[i]
    if i != 3:
        to_print += ","
print(to_print)
print("")
print("")

#Solution 3 (Slightly Better)
print("Slightly Better:")
print("")

list_of_words = ["hello", "yes", "goodbye", "last"]
to_print = ""

for i in range(len(list_of_words)):
    to_print += list_of_words[i]
    if i != len(list_of_words) - 1:
        to_print += ","
print(to_print)
print("")
print("")

#Solution 4 (Acceptable)
print("Acceptable Solution:")
print("")
list_of_words = ["hello", "yes", "goodbye", "last"]
print(",".join(list_of_words))
print("")
print("")

#Solution 5 (BEST)
print("Best Solution:")
print("")
DELIMITER = ","
list_of_words = ["hello", "yes", "goodbye", "last"]
print(DELIMITER.join(list_of_words))
print("")
print("")
print("")

#Random Stuff
print("Random stuff section:")
print("")
def func(x=3, text='2'):
    print(x)
    if text == '1':
        print('Text is 1')
    else:
        print(text)

func(text=5)

def func(word, add=5, freq=1):
    print(word*(freq+add))
    # For Debugging Purposes
    print(f"The word variable is {word}")
    print(f"The freq variable is {freq}")
    print(f"The add variable is {add}")
call = func('hello', freq=3)


test_str =  '{"Studying": "1", "Gaming": 2}'
dictionary = {"Studying": 1, "Gaming": 2}
#dictionary2 = dict(test_str)
print(test_str, dictionary, json.loads(test_str))

i = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
for i in i:
    if i %2 != 0:
        print(f"Odd Number: {i}")
    elif i % 2 == 0:
        print(f"Even Number: {i}")
    else: 
        print(f"Unknown Number: {i}")