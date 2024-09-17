# 1-method of using "for" operator

mult_list=[]

for i in range(3):                      # 0,1,2
    for j in range(3):                  # 0,1,2
        mult_list.append(i*j)

print(mult_list)


#2-method of using "for" operator

mult_list=[i*j for i in range(3) for j in range(3) ]
print(mult_list)



# 3 method of using "for" and "if" operators

my_list=[10,-10,-1,12,-500,13,15,-3]

new_list=[]

for i in my_list:
    if i>0:
        new_list.append(i)

print(new_list)


# 3- short way of coding
my_list=[10,-10,-1,12,-500,13,15,-3]
new_list=[i for i in my_list if i>0]
print(new_list)


# 3- short way of coding and getting negative values
my_list=[10,-10,-1,12,-500,13,15,-3]
new_list=[i for i in my_list if i<0]
print(new_list)