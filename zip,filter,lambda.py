#zip
#The `zip` function in Python is a built-in function that allows 
# you to aggregate elements from multiple 
# iterables into a single iterable.
lst1=['sudharhan','reddy','kamakshi']
lst2=[2,27,32]

print(list(zip(lst1,lst2)))

mat=[[1,2,3],[4,5,6],[7,8,9]]
print(list(row for row in zip(mat)))
print(list(row for row in zip(*mat)))



lst2=[2,27,32]
lst3=[1,2,3]

print(sum([i*j for i,j in zip(lst2,lst3)]))


#filter
 #a built-in function that allows you to filter 
 # a sequence (e.g., a list, tuple, or set) based on 
 # a given condition.
lst=[i for i in range(1,10)]
def is_even(n):
    return n%2==0
print(list(filter(is_even,lst)))


#lambda

add_num=lambda x,y :x*y
print(add_num(3,5))
print('*'*60)
num=[i for i in range(1,10)]

print(list(filter(lambda x:x%2==0,num)))

#map
