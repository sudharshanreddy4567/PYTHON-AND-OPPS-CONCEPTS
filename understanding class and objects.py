#OOPS

class Person:
    name="Reddy"
    age=24
    

pi=Person()
print(pi.name)
print(pi.age)

print('-'*60)
pi.age=45
print(pi.age)
print('-'*60)


class maths:
    name='reddy'

    def geek(self):
        print("hello")
        print(self.name)
    

m=maths()
m.geek() 
#As you can see, the self keyword is a very important part
#  of Python classes. It allows you to access the attributes 
# and methods of the class, which is essential for writing 
# object-oriented code.
print('-'*60)
class jio:
    def factorial(self,n):
        f=1
        for i in range(1,n+1):
            f=f*i
        return f
    def ls_mul(self,lst):
        q=1
        for i in lst:
            q=q*i
        return q
    def lst_dot(self,lst_1,lst_2):
        return [lst_1[i]*lst_2[i] for i in range(len(lst_1))]


m=jio()
print(m.factorial(4))

l=[2,4,5,7,7,8]
l2=[3,5,2,5,1,3]
print(m.lst_dot(l,l2))
print(m.ls_mul(l))

print("="*60)