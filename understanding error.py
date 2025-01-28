for i in range(65,91):
    print(chr(i),",",sep="",end="")

print()
#error

#1.syntax error
#2.Runtime error
#print(10/0) #logically in correction 
# in compaliation it their wiool be no error

#3, logical error
def sump(a,b):
    return a+b
    
print(sump(5,6))
print()


#4.Name error

print("helloe")

# 6.Index error
# 7.Key error
# 8.Attribute
# 9.Indentation
a=10
b=20
c=10
for i in range(20):
    print(i)
#10.Import error
#11.value error
a=int(float(403.3))
print(a)
#12.module not found error
