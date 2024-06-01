# Sort List
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)

thisl = [100, 9, 50, 30, 60, 102]
thisl.sort()
print(thisl)

thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort(reverse=True)
print(thislist)
thisl = [100, 9, 50, 30, 60, 102]
thisl.sort( reverse= True)
print(thisl)

def myfunction(n):
  return abs(n-65)
thislist = [100, 50, 65, 82, 23]
thislist.sort(key = myfunction)
print(thislist)

thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort()
print(thislist)

thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort(key = str.lower)
print(thislist)

thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.reverse()
print(thislist)
# Copy the list
thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)

thislist = ["apple", "banana", "cherry"]
mylist = list(thislist)
print(mylist)

# Join the list or concanated
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]
list3 = list1 + list2
print(list3)

list1 = ["a", "b", "c"]
list2 = [1, 2, 3]
for x in list2:
  list1.append(x)
print(list1)

list1 = ["a", "b", "c"]
list2 = [1, 2, 3]
list1.extend(list2)
print(list1)

# Tuple unchangable
thistuple = ("apple", "banana", "cherry", "apple", "cherry")
print(thistuple)
print(len(thistuple))

thistuple = ("apple",)
print(type(thistuple))
thistuple = ("apple")
print(type(thistuple))

tuple1 = ("apple", "banana", "cherry")
tuple2 = (1, 5, 7, 9, 3)
tuple3 = (True, False, False)
print(tuple1)
print(tuple2)
print(tuple3)

thistuple = tuple(("apple", "mango", "orange"))
print(thistuple)

thistuple = ("apple", "banana", "chery")
if "apple" in thistuple:
  print("Yes, apple is in the fruits tuple")

# Updating tuple / tuple convert to list after than change
x = ("apple", "banana", "orange")
y = list(x)
y[1] = "kiwi" 
x = tuple(y)
print(x)

thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.append("orange")
thistuple = tuple(y)
print(thistuple)

thistuple = ("apple", "banana", "cherry")
y = ("orange",)
thistuple += y
print(thistuple)

thistuple = ("apple", "banana", "cherry")
(green, red, yellow) = thistuple
print(green)
print(red)
print(yellow)

fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")
(green, red, *yellow) = fruits
print(green)
print(red)
print(yellow)

fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")
(green, *red, yellow) = fruits
print(green)
print(red)
print(yellow)

fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")
for x in fruits:
  print(x)

thistuple = ("apple", "banana", "cherry")
for i in range(len(thistuple)):
  print(thistuple[i])

tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)

tuple3 = tuple1 + tuple2
print(tuple3) 

tuple1 = ("a", "b" , "c")
multiply = tuple1 * 2
print(multiply)

# Python set

thisset = {"apple", "banana", "chery"}
print(thisset)

thisset = {"apple", "banana", "cherry", "apple"}
print(thisset)

thisset = {"apple", "banana", "chery",True,1,2}
print(thisset)

thisset = {"apple", "banana", "cherry", False, True, 0}
print(thisset)

thisset = {"apple", "orange", "apple", "lici"}
print(thisset)
print(len(thisset))
print(type(thisset))

thisset = set(("apple", "orange", "apple", "lici"))
print(thisset)

thisset = {"apple", "orange", "apple", "lici"}
for x in thisset:
  print(x)

thisset = {"apple", "banana", "cherry"}
print("apple" in thisset)
print("banana" not in thisset)

thisset = {"apple", "banana", "cherry"}
thisset.add("orange")
print(thisset)

thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}
thisset.update(tropical)
print(thisset)

thisset = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]
thisset.update(mylist)
print(thisset)

thisset = {"apple", "banana", "cherry"}
thisset.remove("apple")
print(thisset)

thisset = {"apple", "banana", "cherry"}
thisset.discard("banana")
print(thisset)

thisset = {"apple", "banana", "cherry"}
x = thisset.pop()
print(x)
print(thisset)
y = thisset.clear()
print(y)

thisset = {"apple", "banana", "cherry"}
thisset.clear()
print(thisset) 

set1 = {"apple", "orange", "banana"}
set2 = {1, 2, 3, 4}
set3 = set1.union(set2)
print(set3)

set1 = {"apple", "orange", "banana"}
set2 = {1, 2, 3, 4}
set3 = set1 | (set2)
print(set3)

set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = {"John", "Elena"}
set4 = {"apple", "bananas", "cherry"}
set5 = set1.union(set2,set3,set4)
print(set5)

set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = {"John", "Elena"}
set4 = {"apple", "bananas", "cherry"}
set5 = set1 | set2 | set3 | set4
print(set5)

set1 = {"apple", "banana", "orange"}
set2 = {"google", "micrisoft", "apple"}
set3 = set1.intersection(set2)
print(set3)

set1 = {"apple", "banana", "orange"}
set2 = {"google", "micrisoft", "apple"}
set3 = set1 & set2
print(set3)

set1 = {"apple", 1,  "banana", 0, "cherry"}
set2 = {False, "google", 1, "apple", 2, True}
set3 = set1.intersection(set2)
print(set3)

set1 = {"apple", "banana", "orange"}
set2 = {"google", "micrisoft", "apple"}
set3 = set1.difference(set2)
print(set3)
set4  = set2.difference(set1)
print(set4)
set5 = set1 - set2
print(set5)
set1.difference_update(set2)
print(set1)

set1 = {"apple", "banana", "orange"}
set2 = {"google", "micrisoft", "apple"}
set3 = set1.symmetric_difference(set2)
print(set3)
set4 = set1 ^ set2
print(set4)
set1.symmetric_difference_update(set2)
print(set1)

# Python Dictionary
# Dict
thisdict = {
  "brand" : "Ford",
  "model" : "mustang",
  "year" : 1964
  }
print(thisdict)
print(thisdict["brand"])

thisdict = {
  "brand" : "Ford",
  "model" : "mustang",
  "year" : 1964,
  "year" : 2024
  }
print(thisdict)
print(len( thisdict))

thisdict = {
  "brand" : "Ford",
  "electric" : False,
  "year" : 2023,
  "colors" : ["red", "green", "yellow"]
}
print(thisdict)
print(type(thisdict))

thisdict = dict(anme = "Rejaul", age = 33, country = "India")
print(thisdict)

thisdict = {
  "brand" : "Ford",
  "electric" : False,
  "year" : 2023,
  "colors" : ["red", "green", "yellow"]
}
print(thisdict["year"])
x = thisdict["colors"]
print(x)
print(thisdict.get("electric"))
y = thisdict.keys()
print(y)

car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}
x = car.keys()
print(x)
car["color"] = "Whaite"
print(x)
y = car.values()
print(y)

car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}
car["model"] = "Verna"
z = car.values()
print(z)

car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}
x = car.items()
print(x)

car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}
if "model" in car:
  print("yes,'model' is present in ythis Dictionaries")

car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}
car["year"] = 2024
print(car)
car.update({"year" : 2000})
print(car)
car.update({"color" : "red"})
print(car)

thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.pop("model")
print(thisdict)
thisdict.popitem()
print(thisdict)

thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
del thisdict["model"]
print(thisdict)
# del thisdict
# print(thisdict)
thisdict.clear()
print(thisdict)

# Looping Dictionaries
thisdict = {
  "brand" : "Ford",
  "model" : "Musting",
  "year" : 2019
}
for x in thisdict:
  print(x)
  print(thisdict[x])

thisdict = {
  "brand" : "Ford",
  "model" : "Musting",
  "year" : 2019
}
for x in thisdict.values():
  print(x)
for x in thisdict.keys()  :
  print(x)
for x , y in thisdict.items():
  print(x, y)

thisdict = {
  "brand" : "Ford",
  "model" : "Musting",
  "year" : 2019
}
mydict = thisdict.copy()
print(mydict)
mydict1 = dict(mydict)
print(mydict1)
print(thisdict)

# Nested dictionary
myfamily = {
  "child1" : {
    "name" : "Riyan",
    "age" : 3
  },
  "child2" : {
     "name" : "Osaidi",
     "age" : 8
   },
   "child3" : {
     "name" : "Wahiba",
     "age" : 12
   }
}
print(myfamily)
print(myfamily["child1"]["name"])
print(myfamily["child2"]["name"])


child1 = {
  "name" : "Emil",
  "year" : 2004
}
child2 = {
  "name" : "Tobias",
  "year" : 2007
}
child3 = {
  "name" : "Linus",
  "year" : 2011
}

myfamily = {
  "child1" : {
    "name" : "Riyan",
    "age" : 3
  },
  "child2" : {
     "name" : "Osaidi",
     "age" : 8
   },
   "child3" : {
     "name" : "Wahiba",
     "age" : 12
   }
}
for x, obj in myfamily.items():
  print(x)

myfamily = {
  "child1" : child1,
  "child2" : child2,
  "child3" : child3
}

print(myfamily)
