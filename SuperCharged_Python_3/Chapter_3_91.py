# Unbalanced matrix

wierd_mat=[[1,2,3,4],[0,5],[9,8,3]]

print(len(wierd_mat))               #  3
print(len(wierd_mat[0]))            #  4
print(len(wierd_mat[1]))            #  2
print(len(wierd_mat[2]))            #  3





big_list=[0]*100
print(big_list)


big_list1=[[1]*100]*10
print(big_list1)






mat=[ ]
for i in range(200):
    mat.append([2]*100)

print(mat)

#  Minimizing above code

mat=[[2]*100 for i in range(200)]
print(mat)





# Multi Dimensional list
mat=[[[ [0]*5  for _ in range(10)]
               for _ in range(10)]
               for _ in range(10)]

print(mat)