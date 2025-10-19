import json

# Object Oriented Programming

    # OOP Basics
from csv import list_dialects
from unicodedata import decimal


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

#factorial function
def factorial(x):
  total = 1
  numbers = [i for i in range(x, 0, -1)]
  for i in numbers:
    total *= i
  print(total)
  return total
factorial(5)

#prime function
def is_prime(x):
    if x < 2:
        return False
    else:
        for n in range(2, x-1):
            if x % n == 0:
                return False
        return True

print(is_prime(13))
print(is_prime(10))

#text reverser
def reverse(text):
  letters = []
  reversed_letters = []
  for i in text:
    letters.append(i)
  diff = 0
  #print(letters)
  index = len(letters) - 1
  #print(index)
  while(index >= 0):
      reversed_letters.append(letters[index])
      #print(reversed_letters)
      diff += 1
      index = len(letters) - 1 - diff
  string = "".join(reversed_letters)
  print(string)
  return string
reverse("thistextisreversed!")

#Vowel removal

print("Doesn't Work:")
def anti_vowel(text):
  char_list = []
  for char in text:
    char_list.append(char)
  print(char_list)
  for i in char_list:
    print(i)
    print("")
    if i.lower() in ['a', 'e', 'i', 'o','u']:
      char_list.remove(i)
      print("Removed: " + i)
      print(char_list)
      print("")
    else:
      print("Kept: " + i)
      print(char_list)
      print("")
  print("".join(char_list))
  return "".join(char_list)
anti_vowel('Hey look Words!')

print("Works:")
def anti_vowel(text):
    result = ""
    vowels = "ieaou"
    for char in text:
          if char.lower() not in vowels:
            result += char
    return result
print(anti_vowel('Hey look Words!'))
print("")

#Scrabble Score
score = {"a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2, 
         "f": 4, "i": 1, "h": 4, "k": 5, "j": 8, "m": 3, 
         "l": 1, "o": 1, "n": 1, "q": 10, "p": 3, "s": 1, 
         "r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4, 
         "x": 8, "z": 10}
def scrabble_score(word):
  print(word)
  letters = [i for i in score]
  points = []
  for char in word:
    if(char.lower() in letters):
      #print(char.lower())
      points.append(score[char.lower()])
 # print(points)
  total = 0
  for i in points:
    total += i
  print(total)
  return total
scrabble_score('test')
print("")
scrabble_score('ABC')
print("")

#Censor Word
def censor(text, word):
  #print(text)
  #print(word)
  
  censored = text.replace(word, "*" * len(word))
  #print(censored)
  return censored

print(censor("My password is 1234", str(1234)))
print("")

#Frequency in Lists
def count(sequence, item):
  total = 0
  for i in sequence.split():
    if i.replace(".", "") == item:
      total += 1
  return total
print(count("Hello my name is Leo. I'm Leo. Leo is my name!", 'Leo'))
print("")

#Remove even/odd numbers
def purify(numbers, method):
  purified = []
  for i in numbers:
    if(method.lower() == 'even'):
        if(i % 2 == 0):
            purified.append(i)
    elif(method.lower() == 'odd'):
        if(i % 2 != 0):
            purified.append(i)
  return purified
print(f"1-5 Odd: {purify([1, 2, 3, 4, 5], 'odd')}")
print(f"1-5 Even: {purify([1, 2, 3, 4, 5], 'even')}")
print("")

#Multiplies numbers in list
def product(numbers):
  total = 1
  for i in numbers:
    total *= i
  return total
print(product([1,5,2]))
print("")
#Remove Duplicates
def remove_duplicates(lst):
  print(f"Original List: {lst}")
  edited_lst = []
  for i in lst:
    if i not in edited_lst:
      edited_lst.append(i)
  return edited_lst
print(f"Edited List: {remove_duplicates([1, 5, 5, 3, 3, 2, 2, 1, 1, 'hi', 'hi'])}")
print("")

#Gets Median of List
def median(lst):
  print(lst)
  sorted_lst = sorted(lst)
  print(sorted_lst)
  if(len(sorted_lst) % 2 == 0):
    isEven = True
  else:
    isEven = False
  if(isEven):
    index = int((len(sorted_lst) / 2) - 1)
    index2 = int(index + 1)
    median = (sorted_lst[index] + sorted_lst[index2]) /2
  else: 
    index = int(round((len(sorted_lst) / 2) - 1))
    median = (sorted_lst[index])
  return median
print(median([24, 33, 11, 33]))
  
#Bitwise Operators
#binary numbers are prefaced by 0b


# bin() input: either decimal or binary; output: binary

print(bin(0b100)) #Output 0b100
print(bin(4)) #Output 0b100

print(int("200", 12))
print(bin(int("200", 12)))

def base_to_base(init_number, init_base, conv_base):
    num_digits = -1
    ind_digits = []
    mult_digits = []
    decimal_conv = 0
    for i in str(init_number):
        num_digits += 1
        ind_digits.append(int(i))
    for i in ind_digits:
       mult_digits.append(i * (init_base ** num_digits))
       num_digits -=1;
    for i in mult_digits:
        decimal_conv += i;
    #if(conv_base == 10):
    #   return decimal_conv
    
    quotients_list = []
    remainders_list = []
    q = int(decimal_conv / conv_base)
    r = int(decimal_conv % conv_base)
    quotients_list.append(q)
    remainders_list.append(r)
    #print(quotients_list, remainders_list)
    while q != 0:
        r =  q % conv_base
        q /= conv_base
        quotients_list.append(int(q))
        remainders_list.append(int(r))
        #print(quotients_list, remainders_list)
    
    conv_factor = 1
    remainder_total = 0
    #test_lst = [8,4,2, 1]
    for  i in remainders_list:
        remainder_total += i * conv_factor
        conv_factor *= 10
    #print(remainder_total)

    if(conv_base == 10):
        return decimal_conv
    else:
        return remainder_total
print(f" 200 (base 11) to base 10: {base_to_base(10, 2, 16)}")


def slopeProgram():
    pointlst = []
    #intlst = []
    #floatlst = []
    numlst = []
    def calcSlopePoints(y2, y1, x2, x1):
        pointlst.append(y2)
        pointlst.append(y1)
        pointlst.append(x2)
        pointlst.append(x1)
        for i in pointlst:
            if(i.lower() == "r"):
                print("Restarting Program...")
                #restartProgram(2, 'start')
            elif(i.lower() == 'b'):
                print("Restarting Subprogram...")
                #restartProgram(2, 'slope')
            elif(i.replace('.', '').replace('-', '').isnumeric() == False):
                print("Invalid user input, please only use integers or decimals. \nRestarting Subprogram...")
                #restartProgram(2, 'slope')
            elif(i.count('.') == 0):
                #print("int")
                numlst.append(int(i))
            elif(i.count('.') == 1):
                #print("float")
                numlst.append(float(i))
        return (numlst[0] - numlst[1]) / (numlst[2] - numlst[3])
    def calcSlopeCoords(coord1, coord2):
        init_coordlst= []
        coordlst = []
        init_coordlst.append(coord1)
        init_coordlst.append(coord2)
        for i in init_coordlst:
          print(i)
          coordv1=  i.replace('(', '')
          coordv2=  coordv1.replace(')', '')
          coordv3 = coordv2.split(", ")
          coordlst.extend(coordv3)
          print(coordlst)
        return calcSlopePoints(coordlst[3], coordlst[1], coordlst[2], coordlst[0])

    global user_input
    user_input = input("Do you want to input \n1. 2 coordinates \n2. The values of y2, y1, x2, and x1?")
    if(user_input == "1"):
        coord1 = input("First coordinate in the following form (x, y): ")
        coord2 = input("Second coordinate in the following form (x, y): ")
        print(f"The slope of your inputted coordinates is: {calcSlopeCoords(coord1, coord2)}")
    elif(user_input == "2"):
        y2 = input("Value of y2: ")
        y1 = input("Value of y1: ")
        x2 = input("Value of x2: ")
        x1 = input("Value of x1: ")
        print(f"The slope of your inputted points is: {calcSlopePoints(y2, y1, x2, x1)}")
#slopeProgram()
