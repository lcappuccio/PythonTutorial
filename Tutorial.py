__author__ = 'leo'

# A classic
print("Hello world")

# Some variables and print them
x = 3
f = 3.14159
name = "Python"
bigNumber = 313459L

print x
print f
print x * f
print name

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
list = ['Pippo','Pluto','Paperino','Paperone']
print list
list.append("ShouldNotBeHere")
print list
list.remove("ShouldNotBeHere")
print list
list.sort()
print list
list.reverse()
print list

# Tuples
dataTuple = (999,111,222,333)
print dataTuple
print dataTuple[1]
