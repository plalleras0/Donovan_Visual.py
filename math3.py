import math
import time
import random
#this porgram calculates the factorial of these numbers 6/11/15/22
print("these program select a number in order to make it factorial")
print("the chosen numbers are 6,11,15,22")
print(" ")
time.sleep(2)
select=[6, 11, 15, 22]
randsc=random.choice(select)
x=randsc
def seld1(x):
ed=1
for i in range(1,x+1):
    ed*=i
print(f"these is the result of {x} is {ed}")
print(f"this is to check if the result above is corect, "+ str(math.factorial(x)))
time.sleep(1)
print(" ")
for elem in select:
    seld1(elem)
    print("now your time select a number")
    choice=int(input("enter your number:"))
    y=choice
def seld2(y):
    ed=1
for i in range(1,y+1):
    ed*=i
    print(f"these is the result of {y} is {ed}")
print(f"this is to check if the result above is correct, "+str(math.factorial(y)))
print(" ")
seld2(y)