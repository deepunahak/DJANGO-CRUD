x = 4
y = 5
if (x == 3):
    print ("This is it")
elif (y<12):
    print ("South")
elif (y>12):
    print ("North")
elif (x == 4):
    print ("East")
else:
    print ("West")

x = abs(26) + abs(-1) - abs(-0)
print(x)

def hose():
  try:
    tree = 2
    return 22
  finally:
    return 24

r =hose()
print(r)


#What is the output from this Python code?
if 1 < 3 < 3:
    print(1);
    print (2);
    print (3);

a={1, 2, 3, 4}
b={3, 4, 5, 6}

c = a ^ b
print(c)

for i in range(0,5):
  if i == 2:
    continue
  print(i)

def goat(b):
    b.append("wolf")

sheep = []
goat(sheep)
print (sheep)
""""
Write a Python function that returns a boolean result based on whether the string parameter passed in is an integer.
 For example 123 = True but 123.0 = False.

"""
import re

value = input("Enter any value: ")

result = re.match("[-+]?\d+$", value)

if result is not None:
    print("User input is an Integer")
else:
    print("User Input is not an integer")

str = input("Enter any value: ")

if str.isdigit():
    print("User input is an Integer ")
else:
    print("User input is string ")


string = "poll coll"
res = ' '.join(elem.capitalize() for elem in string.split())
print(res)