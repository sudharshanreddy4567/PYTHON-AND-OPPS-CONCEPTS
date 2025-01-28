import math
x=56.6445657783
print(math.floor(x))
print(math.trunc(x))
print(math.ceil(x))

print("-"*60)

b=5
print(math.factorial(b))

print(math.pi)
print(math.e)

print('-'*60)
n=34
print(math.sin(n))
print(math.cos(n))
print(math.tan(n))

print('-'*60)


# random numbers
import random


print(random.random())
print(random.randint(1,9))
print(random.choice([1,2,4,4,6]))
print(random.sample([1,2,4,4,6],2))
print(random.uniform(1.0,5.0))

print('-'*60)

# Date and time
import datetime
print("DATE AND TIME")
print(datetime.datetime.now())
print(datetime.datetime(2023,10,28,10,30,0))
print(datetime.datetime.now().strftime("%d/%m/%y %H:%M:%S"))

date1=datetime.datetime.now()
date2=datetime.datetime(2023,10,28,10,30,0)
print(date2-date1)
print('-'*60)


#collections

from collections import Counter
lst=[i for i in range(1,8)]

print(Counter(lst))

print('-'*60)


#Strings 
import string

print(string.ascii_letters)
print(string.ascii_lowercase)
print(string.ascii_uppercase)
print('-'*60)
print(string.digits)
print(string.hexdigits)
print(string.octdigits)
print('-'*60)
print(string.punctuation)