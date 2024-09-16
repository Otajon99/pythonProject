# shallow coping/ deep copying
# 1- method

a_list=[1,2,[5,10]]
b_list=a_list[:]

b_list[0]=0
b_list[1]=0
b_list[2][0]=0
b_list[2][1]=0

print(a_list)                     # copy



# 2-method
import copy
a_list=[1,2,[5,10]]
c_list=copy.deepcopy(a_list)        # Deep copy
print(c_list)