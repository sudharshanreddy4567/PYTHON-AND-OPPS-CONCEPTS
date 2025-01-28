import string
print(string.ascii_uppercase)
print(string.ascii_lowercase)
print(string.ascii_letters)

print("A")
print(ord('A'))
print(ord('a'))
print(ord('z'))

l=[string.ascii_lowercase]
print([i for i in  l])

print(chr(5))

for i in range(1,122):
    print(chr(i),sep=",",end=" ")
    
