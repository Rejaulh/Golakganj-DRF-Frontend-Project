print("Hello, World")
print("Agomani")
import sys
print(sys.version)
if 5 > 2:
 print("Five is greter than two")
 if 5 > 2:
  print("Five is greater than two")
  if 5>2:
   print("Five is greater than two")
x= 5
y = "Hello, World"
print(x)
print(y)
#The line is comment
print("Hello Rejaul")
#This is a comment
print("Hello Riyan") # This is a comment
# print("Hello, World")
print("Cheers, Mate")
"""
This is a comment
written in
more than just one line

"""
print("Hello, Munni")

# diiscused about python variable
x= 8
y= "Osaidi"
print(x)
print(y)

x = 4       # x is of type int
x = "Sally" # x is now of type str
print(x)
#Casting
x= str(3)
y= int(3)
z= float(3)
print(x)
print(y)
print(z)

#Get the Type
x= 5
y= "Riyan"
print(type(x))
print(type(y))

#Single or double codes are same result
x= "Osaidi"
print(x)
y= 'Wahiba'
print(y)

# Case sensitive
a= 6;
A= "Salary"
print(a)
print(A)

# Variable name
myvar= "Jhon"
my_var= "Jhon"
_my_var= "Jhon"
myVar= "Jhon"
MYVAR= "Jhon"
myvar2= "Jhon"
print(myvar)
print(my_var)
print(_my_var)
print(MYVAR)
print(myvar2)

#Assign multiple variables
x,y,z= "Orange", "Apple", "Banana"
print(x)
print(y)
print(z)

#One value to multiple varables
x=y=z= "Chery"
print(x)
print(y)
print(z)

#Unpack acollection
fruit= ["Pinaple", "Lemon", "Mango"]
x, y, z= fruit
print(x)
print(y)
print(z)

#Output variables
x= "Python"
y= "is"
z= "awesome"
print(x,y,z)
x= "Python "
y= "is "    #one space means sentance separated
z= "awesome"
print(x + y + z)
x= 3
y= 7
#z= x + y
print(x+y)

#Global variable
x = "awesome"
def myfunc():
  print("Python is " + x)
myfunc()

x = "awesome"
def myfunc():
 x = "fantastic"
 print("Python is " + x)
myfunc()
print("Python is " + x)

#Use global keyword inside a function
def myfunc():
 global x
 x= "Fantastic"
myfunc()
print("Python is very " + x)

x = "Guwahati"
def myfunc():
 global x
 x = "Agomani"
myfunc()
print("My native place is " + x)

# DATA TYPES
x = 1j
print(x)
print(type(x))
x= 20.9
print(x)
print(type(x))
x = ["Banana", "Apple", "Orange"]
print(x)
print(type(x))
x= ("Mango", "Lichi", "Guava")
print(x)
print(type(x))
x= range(6)
print(x)
print(type(x))
x = {"name":"Rejaul", "age": 33 }
print(x)
print(type(x))
x = {"class", "pencil", "Boad"}
print(x)
print(type(x))
x = frozenset({"Onion", "Garlic", "chilli" })
print(x)
print(type(x))
x = True
print(x)
print(type(x))
x = b"Hello"
print(x)
print(type(x))
x = bytearray(5)
print(x)
print(type(x))
x= memoryview(bytes(5))
print(x)
print(type(x))
x= None
print(x)
print(type(x))


# Python numbers(int,float,complex)
x= 2e2
print(x)
x= 3 + 5j
print(x)

#cnvert one data type to another data type
x = 5
y = 2.5
z = 1j
# conver data type
a = float(x)
b = int(y)
c = complex(x)
d= str(y)

print(a)
print(b)
print(c)
print(d)

#Random number
import random
print(random.randrange(1,10))

# Python casting int, float, str
x = int(3)
y = int(2.3)
z = int("7")
print(x)
print(y)
print(z)
print("He 'is' a Boy")
print("He "is" Raja")

# Assaign string to avariable
a= "Hello"
print(a)
a = ''' This is a pragraph
discussed about string , to assaign variable
the string are like written in 'str' in assaign
a varable'''
print(a)
# Sting in Array
a = "Hello, World"
print(a[0])
print(a[1])
print(a[6])
print(a[5])
print(a[7])

for x in "Banana":
 print(x)

x= "Hello, World"
print("The length of x is:  " , len(x))

txt = "The best things in life are free!"
print("free" in txt)

txt = "The best things in life are free!"
if "free" in txt:
 print("Yes, free is in the text")

txt = "The best things in life are free!"
print("Ecpensive" not in txt)

txt = "The best things in life are free!"
if "expensive" not in txt:
 print("Expensive not present in the text")

b = "Hello, World"
print(b[2:5])
print(b[2:8])
print(b[:5])
print(b[0:8])
print(b[3:])
print(b[-5:-1])
print(b[-9:-2])
# uppercase
a = "Hello, World"
print(a.upper())
print(a.lower())

a = "  Hello, World  "
print(a)
print(a.strip())
print(a.replace("H", "J"))
print(a.split(","))

# concatenate
a = "Hello"
b = "World"
c = a + b
print(c)
d = a + " " + b
print(d)

#  string format
age = 34
txt = f"My name is Jhon, my age is {age}"
print(txt)

price = 40
txt = f"The price is {price} doller"
print(txt)

price = 40
txt = f"The price is {price:.2f} doller"
print(txt)

txt = f"The price is {20 * 59} dollars"
print(txt)

# Escape characters
txt = "My home town is \"Agomani\""
print(txt)
txt = "It\'s alright"
print(txt)
txt = "This is inser one \\ backslash"
print(txt)
txt = "Rejaul\nHoque"
print(txt)
txt = "Riyan\tWasif"
print(txt)
txt = "Riyan \bWasif"
print(txt)
txt = "My name is\fRejaul Hoque"
print(txt)
txt= "\100\000"
print(txt)
txt = "\x48\x65\x6c\x6c\x6f"
print(txt)

# Python String
txt = "hello, and welcome to my world."
x = txt.capitalize()
print(x)
txt = "python is FUN!"
x= txt.capitalize()
print(x)

txt = "36 is my age."

x = txt.capitalize()

print (x)

txt = "My home town is 'Agomani'"
x = txt.casefold()
print(x)

txt = "My home town is 'Agomani'"
x = txt.center(100)
print(x)
txt = "My home town is 'Agomani'"
x = txt.center(100,"-")
print(x)
txt = "I love apples, apple are my favorite fruit, apple is the state fruil of Kashmir"
x = txt.count("apple")
print(x)
txt = "I love apples, apple are my favorite fruit, apple is the state fruil of Kashmir"
x = txt.count("apple", 10, 49)
print(x)
txt = "My name is Ståle"
x = txt.encode()
print(x)
print(txt.encode(encoding="ascii", errors="backslashreplace"))
print(txt.encode(encoding="ascii",errors="ignore"))
print(txt.encode(encoding="ascii",errors="namereplace"))
print(txt.encode(encoding="ascii",errors="replace"))
print(txt.encode(encoding="ascii",errors="xmlcharrefreplace"))

txt = "Hello, welcome to my World"
x = txt.endswith("d")
print(x)
y = txt.endswith("my World")
print(y)
z = txt.endswith("my world", 5, 10)
print(z)

txt = "H\te\tl\tl\to"
print(txt.expandtabs())
print(txt.expandtabs(1))
print(txt.expandtabs(2))
print(txt.expandtabs(3))
print(txt.expandtabs(4))
print(txt.expandtabs(5))
print(txt.expandtabs(10))

txt = "Hello, welcome to my World"
x = txt.find("e")
print(x)
print(txt.find("w",1,5))
print(txt.find("e",5,10))
print(txt.find("q"))
# print(txt.index("q"))

txt = "If one kg apple price is {price:.2f} ruppes"
x = txt.format(price = 50)
print(x)
txt1 = "My name is {fname} , I'am {age} ."
print(txt1.format(fname="Rejaul", age= 34))
txt2 = "My name is {0} , I'am {1}"
print(txt2.format("Rejaul", 24))
txt3 = "My name is {} , I'am {}."
print(txt3.format("Rejaul", 34))
txt4 = "My name is {}, I'm {}".format("John",36)
print(txt4)

txt = "Company12"
x = txt.isalnum()
print(x)
txt = "Company 12"
x = txt.isalnum()
print(x)

# BOOLEANS
A = 300
B = 33
if B>A:
 print("A is greater than B")
else:
 print("B is greater than A")
 print(bool("Hello"))
 print(bool(45))
 print(bool(False))
 print(bool(None))
 print(bool(0))
 print(bool({}))
 print(bool(""))

class myclass():
  def _len_(Self):
   return 0
myobj = myclass()
print(bool(myobj))

class myclass():
  def __len__(self):
    return 0
myobj = myclass()
print(bool(myobj))

def myfunc():
 return True
print(myfunc())

def myfunction():
 return True
if myfunction():
 print("Yes!")
else:
 print("No!")

def myfunction():
 return False
if myfunction():
 print("Yes!")
else:
 print("No!")

x = 200
print(isinstance(x,int))

# Python Operator
x = 2
y = 3
z = x**y
print(z)
print(x//y)
print(y//x)

x = 6
x += 7
print(x)
x = 6
x %= 4
print(x)

a= 5
a &= 3
print(a)
print(a:=9)

x = 5
y = x>3 and x<6
print(y)
x = 5

print(not(x > 2 and x < 10))

#  Identity Operator
x = ["apple", "banana"]
y = ["apple", "banana"]
z = x
print(x is z)
print(x is y)
print(x == y)
print(x is not y)
print(x is not z)
print(x != y)

x = ["apple", "banana"]

print("banana" in x)
print("banana" not in x)

print(6 & 3)
"""
The & operator compares each bit and set it to 1 if both are 1, otherwise it is set to 0:

6 = 0000000000000110
3 = 0000000000000011
--------------------
2 = 0000000000000010
====================
"""
print(6 | 3)
"""
The | operator compares each bit and set it to 1 if one or both is 1, otherwise it is set to 0:

6 = 0000000000000110
3 = 0000000000000011
--------------------
7 = 0000000000000111
====================
"""
print(6 ^ 3)
"""
The ^ operator compares each bit and set it to 1 if only one is 1, otherwise (if both are 1 or both are 0) it is set to 0:

6 = 0000000000000110
3 = 0000000000000011
--------------------
5 = 0000000000000101
====================
"""
print(~3)
"""
The ~ operator inverts each bit (0 becomes 1 and 1 becomes 0).

Inverted 3 becomes -4:
 3 = 0000000000000011
-4 = 1111111111111100

Decimal numbers and their binary values:
 4 = 0000000000000100
 3 = 0000000000000011
 2 = 0000000000000010
 1 = 0000000000000001
 0 = 0000000000000000
-1 = 1111111111111111
-2 = 1111111111111110
-3 = 1111111111111101
-4 = 1111111111111100
"""
print(3 << 2)
"""
The << operator inserts the specified number of 0's (in this case 2) from the right and let the same amount of leftmost bits fall off:

If you push 00 in from the left:
 3 = 0000000000000011
becomes     (3*2**2)
12 = 0000000000001100"""
print(8 >> 2)
"""
The >> operator moves each bit the specified number of times to the right. Empty holes at the left are filled with 0's.

If you move each bit 2 times to the right, 8 becomes 2:
 8 = 0000000000001000
becomes  (8/2**2)
 2 = 0000000000000010

Decimal numbers and their binary values:
 0 = 0000000000000000
 1 = 0000000000000001
 2 = 0000000000000010
 3 = 0000000000000011
 4 = 0000000000000100
 5 = 0000000000000101
 6 = 0000000000000110
 7 = 0000000000000111
 8 = 0000000000001000
 9 = 0000000000001001
10 = 0000000000001010
11 = 0000000000001011
12 = 0000000000001100
"""
#  Python List
thislist = ["Apple","Mango","Orange","Cherry"]
print(thislist[1:3])
print(thislist[-3:-1])
print(thislist[-2:])
print(thislist[:-3])
print(thislist[3])
print(thislist[-3])
# Change list
thislist = ["Apple","Mango","Orange","Cherry","Jackfruit","Lichi"]
thislist[2] = "Olive"
print(thislist)
thislist = ["Apple","Mango","Orange","Cherry","Jackfruit","Lichi"]
thislist[3:5] = ["Apple", "Mango", "Orange", "Olive"]
print(thislist)
thislist = ["Apple","Mango","Orange","Cherry","Jackfruit","Lichi"]
thislist[1:6] = ["Watermelon"]
print(thislist)
thislist = ["Apple","Mango","Orange","Cherry"]
thislist.insert(2, "Watermelon")
print(thislist)
# Add list
thislist = ["Apple","Mango","Orange","Cherry"]
thislist.append("Lichi")
print(thislist)
thislist = list(("Apple","Mango","Orange","Cherry"))
thislist.append("Jackfruit")
print(thislist)
thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)
print(len(thislist))
# Remove Items
thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)
thislist.pop(0)
print(thislist)
thislist.insert(1,"Orange")
print(thislist)
thislist.extend(tropical)
print(thislist)
del thislist[1]
print(thislist)
thislist.clear()
print(thislist)

# Loop List
thislist = ["apple", "banana", "cherry"]
for x in thislist:
 print(x)
thislist = list(("Apple","Mango","Orange","Cherry"))
for i in range(len(thislist)):
  print(thislist[i])

thislist = ["Jackfruit", "Olive", "Dalim"]
i = 0
while i < len(thislist):
 print(thislist[i])
 i = i + 1

thislist = ["Jackfruit", "Olive", "Dalim"]
[print(x) for x in thislist] 

# List Comprehenssion
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []
for x in fruits:
 if 'a' in x:
  newlist.append(x)
print(newlist)

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if 'a' in x]
print(newlist)

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if x != "apple"]
print(newlist)

newlist = [x for x in range(10)]
print(newlist)
newlist = [x for x in range(10) if x<6]
print(newlist)

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x.upper() for x in fruits]
print(newlist)

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = ['hello' for x in fruits]
print(newlist)

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x if x != "cherry" else "orange" for x in fruits]
print(newlist)
