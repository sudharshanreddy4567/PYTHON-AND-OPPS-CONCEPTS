lst=[['sudharshan',"reddy","kamakshi","poi"],[2,5,3,5,7,4,7,4,7,4,7,3,5,6]]
print(lst[0][3])
mat=["T","F"]
print(mat[0][0:3])
mat=[1,2,3,4,["ankit","reddy"]]
print(mat[4][1])
print(mat[1])
mat[2][2]=6
print(mat[2][2])
print(mat)
mat[4][1]="loi"
print(mat)
mat.append([3,5,4])
# print(mat)
del mat[0]
mat.append(["lio,jio"])
mat[0]=["de","kjh"]
# print(mat)
# # print(len(mat[0]))1
# print(mat[::-1])
for i in range(len(mat)-1,-1,-1):
    print(i,mat[i])

print(mat)
import string 
h=string.ascii_uppercase[:6]
print(h,end=" ")
for i in mat:
    for j in i:
        print(i,j)
n = int(input("Enter the number: "))

if n == 2:
    for i in range(n):
        for j in range(n):
            print("T", "F")
            
elif n == 3:
    for i in range(n):
        for j in range(n):
            for k in range(n):
                print("T", "F", "T")


mat=[[0,0,0],
     [0,0,0],
     [0,0,0]]
for i in range(3):
    for j in range(3):
        mat[i][j]=int(input("Enter the value of ({i+1},{j+1}): "))
mat=[[1, 2, 3],
[3, 4, 5],
[56, 7, 7]]

for r in mat:
    print(r)

for k in mat:
    if k==1:
         row=sum(k)
         
mat=[[1, 2, 3],
[4, 5, 6],
[7, 8, 9]]
# # for i in range(3):
# #     for j in range(3):
# #         mat[i][j]=int(input(f"Enter the number in ({i+1},{j+1}): "))

# for i in mat:
#     print(i)


# for i in mat:
#     row=sum(i)
#     print("Sum of elements in is row: ",row)

# fist_mat=sum(mat[0])
# print("1st row sum is: ",fist_mat)
# second=sum(mat[1])
# print("2nd row sum is: ",second)
# third_row=sum(mat[2])
# print("3rd row sum is: ",third_row)

# #to add 1st colom sum
# f=0
# for i in mat:
#     f+=i[0]

# print("1st colomn sum is",f)

# s=0
# for i in mat:
#     s+=i[1]
# print("for the 2nd colomn sum is: ",s)

# h=0
# for i in mat:
#     h+=i[2]
# print("for 3rd colomn sum is: ",h)

# b=0
# for i in range(len(mat)):
#     b+=mat[i][i]
# print("diagobal sum is",b)

# e=0
# n=len(mat)
# for i in range(n):
#     e+=mat[i][n-i-1]
# print("diagobal sum is",b)

# to make sqare of the elemnets in ths list
# f=[1,2,3,4,5,6]
# si=[i**2 for i in f]
# print(si)
# ki=[i for i in range(20) if i%2==0]
# print(ki)

# hi=[]
# for i in range(20):
#     if i%2==0:
#         hi.append(i)

# print(hi)

# j=[i**5 for i in range(50)]
# print(j)

# h=[]
# for i in range(20):
#     for j in range(10):
#     print(i,j)
# print([[j for j in range(5)]for i in range(3)])
# print(mat)
# for i in mat:
#     for j in i:
#         print(j)

mat=[[5, 7,5],
     [6, 3,9],
     [2,6,4]]

# for i in range(2):
#     for j in range(2):
#         mat[i][j]=int(input(f"Enter the number({i+1},{j+1}): "))
# k=0
# for i in mat[0]:
#     for j in i:
#         k=sum(mat)
# print(k)
print(mat,sep="\n")
k1=sum(mat[0])
k2=sum(mat[1])
k3=sum(mat[2])
print("sum of the first colomn is: ",k1)
print("sum od the second colomn is:",k2)
print("sum of the third colomn is: ",k3)

k=0
for i in mat:
    k=k+i[0]
print("sum od the row is: ",k)

d=0
for i in mat:
    d=d+i[1]
print("sum of the second row is: ",d)

j=0
for i in mat:
    j=j+i[2]
print("sum of the third row is: ",j)

v=0
p=len(mat)
for i in range(p):
    v=v+mat[i][i]
print("diagonal sum is: ",v)

t=0
for i in range(p):
    t=t+mat[i][i-n-1]
print("reverse diagonal sum is: ",t)


flaot