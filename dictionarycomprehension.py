# print([i for i in range(20)])
# print([i for i in range(20)])

# print([i**2 for i  in range(1,20)])
# print("-"*60)


# for i in range(20):
#     print('(',i**2,',',i%2,')')

for i in range(5):
    for j in range(5):
        print("*",end=" ")
    print()

# print('-'*60)

# for i in range(1,6):
#     for j in range(i):
#         print("*",end=' ')
#     print()
# print("-"*50)
# 
# for i in range(5,0,-1):
#     for j in range(i):
#         print("*",end=" ")
#     print()
# print('-'*60)

# k=1
# for i in range(1,5):
#     for j in range(i):
#         print(k,end=" ")
#         k=k+1
#     print()

# print('-'*60)

# # for i in range(5):
# #     for j in range(5):
# #         print("*",end=" ")
# #     print()

# for i in range(5,0,-1):
#     for j in range(i):
#         print("*",end=" ")
#     print()

# print("-"*60)

# n=5
# for i in range(1,n+1):
#     for j in range(n-i):
#         print(" ",end=" ")
#     for k in range(2*i-1):
#             print("*",end=" ")
#     print()
# for i in range(n-1,0,-1):
#     for j in range(n-i):
#         print(" ",end=" ")
#     for k in range(2*i-1):
#         print("*",end=" ")
#     print()
# for i in range(1,n+1):
#     for j in range(n-i):
#         print(" ",end=" ")
#     for k in range(2*i-1):
#             print("*",end=" ")
#     print()
# for i in range(n-1,0,-1):
#     for j in range(n-i):
#         print(" ",end=" ")
#     for k in range(2*i-1):
#         print("*",end=" ")
#     print()   

# print("*"*60)

# dct={i:i**2 for i in range(1,50) if i%2==0}
# print(dct)

# #converting the dictionary to list
# print('-'*60)
d=["Apple","bannan","grapes"]
k={len(i):i for i in d} # their shold no same lenght in the dictinary then it will take only final value

print(k)


# #special keys with strings
# dct={"num_"+str(i):i for i in range(1,12)}
# dct={k:v for k,v in dct.items() if v%3==0}
# print(dct)

# print('*'*60)
# # dct={'a','b','c','d'}
# # dct1={i for i in range(1,5)}
# # dct2={dct[i]:dct1[i] for i in range(len(dct1))}
# # print(dct2)
# # mat=[[0,0,0],[0,0,0],[0,0,0]]
# # for i in range(3):
# #     for j in range(3):
# #         mat[i][j]=int(input("Enter the number: "))

# # for i in mat:
# #     print(i)
# mat=[[1, 2, 3],
# [4, 5, 5],
# [6, 7, 8]]
# final={(i,j):mat[i][j] for i in range(3) for j in range(3)}
# print(final)