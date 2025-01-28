def geek():
    print("hello")
    

for i in range(10):
    geek()
print()
j=5
while(j>0):
    geek()
    j=j-1

print('-'*60)

j=20
def geek():
    k=9
    print(j,k)

geek()
geek()
print('-'*60)

def geek(n):
    print("hi",n)
    k=1
    for i in range(10):
        print(k,"I am from ",n)
        k=k+1
geek("jio")
print('-'*60)
print(("|")*60)

def sumb(a=0,b=0):
    print(a+b,a-b)

sumb(5,10)
sumb(a=5,b=10)
sumb()
sumb(b=8)
print('-'*60)
def jio(a,b):
    return a*b

a=jio(5,6)
print(a)
print('-'*60)
print()
print('-'*60)

lst=[1,2,3,4,5]

def one_s(lst):
    return [i**2 for i in lst]

def two_c(lst):
    return [i**3 for i in lst]

def sumb(lst):
    k=one_s(lst)
    n=two_c(lst)
    return [k[i]+n[i] for i in range(len(lst))]

print(one_s(lst))
print('-'*60)
print(two_c(lst))
print('-'*60)
print(sumb(lst))
print('-'*60)