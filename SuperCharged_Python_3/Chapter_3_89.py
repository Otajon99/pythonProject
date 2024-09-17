# Important! Remember! 2 different results

def set_list_vals(list_arg):
    list_arg[0]=100
    list_arg[1] = 200
    list_arg[2] = 150

a_list=[0,0,0]
set_list_vals(a_list)
print(a_list)                            #[100,200,300]





# Important! Remember! 2 different results

def set_list_vals(list_arg):
    list_arg=[100,200,300]

a_list=[0,0,0]
set_list_vals(a_list)
print(a_list)                              # result: [0,0,0]




# Multidimensional Lists

mat=[
     [10,11,21],
     [20,21,22],
     [25,15,15]
     ]
print(mat)
print(mat[0][0])
