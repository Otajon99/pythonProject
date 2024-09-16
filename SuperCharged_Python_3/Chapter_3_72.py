########    1-method of reverse list
a_tup=(1,3,5,0)
for i in reversed(a_tup):
    print(i , end=" ")                # output--> 0 5 3 1


##########   2-method
print(""
      "")
print(tuple(reversed(a_tup)))          # output--> (0,5,3,1)



########     list.extend([]) = list.append()

a_list=[1,2,3]
a_list.append(5)
a_list.extend([4])
a_list.extend([8,9,10])

print(a_list)