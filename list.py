lst=['sudharshan',"reddy","kamakshi","poi"]
print(lst)
list1=[1,"reddy","poi"]
print(lst[0][7:9])
print(lst[-1])

#modify the values
lst[1]='ram'
print(lst[0:2])
print(lst[::-1])
h="iopori"
print(h[::-1])
print('-'*50)
#append
lst.append("kavitha")
print(lst)
#removine
lst.remove("ram")
print(lst)
lst.append("reddy")
#only first dulpilcatte value only remove if i remove any thing in the list
lst.remove("reddy")
print(lst)
print(len(lst))
o=lst.pop(1)
k=lst.reverse(2)
print(lst[::-1])
print(lst.index("reddy"))
print('*'*20)
print(lst.count("reddy"))
print('*'*20)
lst.extend('hio','leo','lion')
print(lst)
lst=[2,5,3,5,7,4,7,4,7,4,7,3,5,6]
print(sorted(lst))
print(min(lst))
print(max(lst))
print(lst.count(3))
# print(lst.sort())
# for i in range(1,len(lst)):
#     print(i,lst[i],end=" ")

# for i in range(len(lst)-1,-1,-1):
#     print(i,lst[i],end=" ")
 

# for i in range(len(lst)-1,-1,-1):
#     print(i,lst[i],end=" ")

for i in range(len(lst)-1,-1,-1):
    print(i,lst[i],end=" ")