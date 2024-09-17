# 1 -Exercise to calculate average value of list
import functools

def add_func(a,b):
    return a+b
my_list=[12,4,7,1]
t=functools.reduce(add_func,my_list)
n=len(my_list)
print(t/n)





# 2- Median number
# [2,4,6,9,10]  -->  6
# [1,3,6,8,3,8]  --> (6+8)/2= 7
my_list=[12,4,5,15,6,23,56]
if len(my_list)%2==0:
    i=int(len(my_list)/2)-1
    print((my_list[i]+my_list[i+1])/2)

elif len(my_list)%2==1:
    i = int((len(my_list)+1) / 2) - 1
    print(my_list[i])
