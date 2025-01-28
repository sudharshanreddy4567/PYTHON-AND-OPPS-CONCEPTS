set={1,2,3,4}
set1={6,7,4,8}
# print(set)

#sets are mutable
# set.add(6)
# print(set)
# set.remove(1)
# print(set)
# print(set.pop())
# print(set)

# for i in set:
#     print(i)

# print(2 in set)
print("Union",set | set1)
print("Intersection",set & set1)
print("Difference",set - set1)
print("Difference",set1 - set)
print("Symetric Diff",set1 ^ set)

print("-"*60)

tup=(1,2,3,4)
print(tup)
print(tup[1:3])

tup=(1,2,3,4)
tup1=(6,7,4,8)
print(tup+tup1)
print(len(tup+tup1))

for i in tup1:
    print(i)
print('-'*60)
tup=(1,2,3,4,4,2,1,4,2,3)
print(tup.count(3))
print(tup.index(3))

#multipling the duplicate values
print(tup*3)