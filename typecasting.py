# s=int(3.14)
# print(s)
# h=int(input("Enter the number"))
# print(h)
# o=float(input("Enter the float number"))
# print(o)
# i=complex(input("Enter the complex number"))
# print(i)
# g=input("Enter the boolena(True/false)")
# g=g.lower()=='true'
# print(g)
# print(int(3.14))
# print(int('10'))
# print(int(True))

# print(float(3))
# print(float(True))
# print(float('408'))


# print(str(123))

# print(str(123.8989))

# print(str(False))

# print(bool(1))
# print(bool(10000))
# print(bool(-123))
# print(bool('su'))
# print(bool('s'))
# print(bool(''))


# a=4
# b=5
# # b=4 and a=5

# k=a
# a=b
# b=a

# a=0
# g=int(input("Enter the number: "))
# while g!=0:
#     g=g//10
#     a=a+1

# print(a)

# a=1
# g=int(input("Enter the number: "))

a=int(input("Enter the number: "))
b=int(input("Enter the number: "))

res=max(a,b)
while(res>0):
    if a%res==0 & b% res==0:
        break

    res=res+1
print(res)