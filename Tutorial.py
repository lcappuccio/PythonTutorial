import random

__author__ = 'leo'

# A classic
print("Hello world")

# Some variables and print them
x = 3
f = 3.14159
aString = "Python"
bigNumber = 313459L

print x
print f
print x * f
print aString

# Strings manipulation
sentence = "This is a python tutorial"

print sentence
print sentence[0]
print sentence[0:5]
print sentence + ", I repeat,  " + sentence
print sentence.replace('tutorial', 'beginner\'s guide')

# String comparison
name1 = "Pippo"
name2 = "Pluto"
if name1 == name2:
    print "They are equal"
else:
    print "Not equal"

# Some string methods
print len(name1)
print name1.upper()

# Lists
listDisney = ['Pippo', 'Pluto', 'Paperino', 'Paperone']
print listDisney
listDisney.append("ShouldNotBeHere")
print listDisney
listDisney.remove("ShouldNotBeHere")
print listDisney
listDisney.sort()
print listDisney
listDisney.reverse()
print listDisney

# Tuples
dataTuple = (999, 111, 222, 333)
print dataTuple
print dataTuple[1]

# Dictionaries
dictionaryData = {}
dictionaryData["Hello"] = "Ciao"
dictionaryData["Yes"] = "Si"
dictionaryData["No"] = "No"
dictionaryData["Goodbye"] = "Arrivederci"
dictionaryData[76] = "Settantasei"

print dictionaryData["Hello"]
print dictionaryData["Goodbye"]
print dictionaryData[76]

# Casting
x = 3
y = 3.14159
print str(x) + ", " + str(y)
print str(x + y)
z = "111"
print int(x)
# This will fail!
# w = "1a1"
# print int(w)

# Conditional Statements
x = 3
y = 10
if x < y:
    print "X is smaller than y"
else:
    print "X is bigger than y"

# A simple game
import _random
# randomNumber = random.randint(0,10)
# print randomNumber
# userGuess = int(raw_input("Guess number from 0:10 : "))
# while userGuess != randomNumber:
#     userGuess = int(raw_input("Guess again: "))
# print "Guessed"

# Functions
def returnsString():
    return "A string"
print returnsString()

def pow(x):
    return x**x
print pow(2)

# Loops
for item in listDisney:
    print item

for i in range(0,50):
    print i

# A simple class
class Person:
    name = ""

    def __init__(self, name):
        self.name = name

    def sayGreeting(self):
        # The "self" is necessary beacause "name" is already defined in the namespace in line 11
        print "Hello, my name is " + self.name

pippo = Person("Pippo")
pluto = Person("Pluto")
paperino = Person("Paperino")

pippo.sayGreeting()
pluto.sayGreeting()
paperino.sayGreeting()

# Inheritance
class Programmer(Person):

    def __init__(self, name):
        self.name = name

    def doing(self):
        print "Learning python"

programmer = Programmer("Nerd")
programmer.sayGreeting()
programmer.doing()

# Polymorphism with function
class Bear(object):
    def sound(self):
        print "Groarrr"

class Dog(object):
    def sound(self):
        print "Woof woof!"

def makeSound(animalType):
    animalType.sound()


bearObj = Bear()
dogObj = Dog()

makeSound(bearObj)
makeSound(dogObj)

# Polymorphism with class
class Document:

    def __init__(self, type):
        self.type = type

    def show(self):
        raise NotImplementedError("Subclass must implement")

class documentPdf(Document):
    def show(self):
        return "PDF content"

class documentRtf(Document):
    def show(self):
        return "RTF content"

documents = [documentPdf("PDF"), documentRtf("RTF"), documentPdf("Other PDF")]

for document in documents:
    print document.type + ": " + document.show()