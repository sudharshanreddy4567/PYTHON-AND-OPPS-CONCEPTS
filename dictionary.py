# #in dictionary every value willl have own pair
# # #the shouls not be duolicated
# # dict={1:"sud",2:"har",3:"shan",4:" reddy",5:"lip",3:"lh",'k': "ugu"}
# # print(dict)

# #accesing the elements:
# # print(dict['k'])
# # print(dict[1])
# # print(dict[2])
# # print(dict.get(1))
# # dict[6]="kuryer"
# # print(dict)



# print(dict.keys())
# print(dict.values())

# # # to accsesing the things
# for i in dict.keys():
#     print(i,dict[i])


# print(dict.items(),sep=" ")


# for k,v in dict.items():
#     print(k,v)



print(1 in dict) # itt will the the was present are not in the dictainary


# for update the dictinary

dc_1={1:'A',2:'B',3:'C',4:'D'}
dc_2={9:'j',8:'op',7:"hgfd"}

dc_1.update(dc_2)
print(dc_1)
print(dc_2)


d={1:{"name":"reddy","phone":"12345"},
   2:{"name":"dio","phone":"4567"},
   3:{"name":"ram","phone":"672783"}}
print(d)
print('-'*50)
print(d)
print('-'*50)
print(d[1])
print(d[1]['name'])
print(d[3]['phone'])

#adding ,updating and deleting the values
d[3]['name']="sudharshan"
print(d[3])
print('*'*50)
d[1]={"name":"prakesh","phone":"12345"}
print(d)
print("-"*50)
del d[1]['name']
print(d)

# for i in d.keys():
#     print(i,d[i]['name'],d[i]['phone'])


print('-'*60)
d={1:{"name":"reddy","phone":"12345","marks":{'mat':40,'tel':50,'sci':45}},
   2:{"name":"dio","phone":"4567","marks":{'mat':43,'tel':42,'sci':35}},
   3:{"name":"ram","phone":"672783","marks":{'mat':43,'tel':24,'sci':36}}}

print(len(d[1]['marks']))
print("-"*60)
print(d)
print("-"*60)

for i in d.keys():
    print(i,d[i]['name'],d[i]['marks']['tel'])
    print("-"*60)


