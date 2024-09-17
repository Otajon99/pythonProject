# Dictionaries and Set Comprehension

a_list=[5,5,5,-20,2,-1,2]
my_set=set()
for i in a_list:
    if i>0:
        my_set.add(i)
print(my_set)



# 2-method

a_list=[5,5,5,-20,2,-1,2]
my_set={i for i in a_list if i>0}
print(my_set)



# Dictionary comprehension      key:value

vals_list=[("pi",3.14),("phi", 1.618)]
my_dict={i[0]:i[1] for i in vals_list}
print(my_dict["pi"])


# Another example

keys=["Bob","Carol","Ted"]
vals=[4.0, 4.0, 3.75, 3.9]
grade_dict={keys[i]:vals[i] for i in range(len(keys))}
print(grade_dict)


# Function method same result like before

keys=["Bob","Carol","Ted","Alice"]
vals=[4.0, 4.1, 3.75, 3.9]
grade_dict={keys:vals for keys,vals in zip(keys,vals)}
print(grade_dict)

