
# 1-method

a_list=[1,2,3]
b_list=[]
for i in a_list:
    b_list.append(i*i)
print(b_list,end=" ")

#2-method

b_list=[i*i for i in a_list]
print(b_list)

