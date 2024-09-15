# Lists and For loop
a_list=[]
while True:
    s=input("Enter name: ")
    if not s:
        break
    a_list.append(s)

a_list.sort()
print(a_list)

for name in a_list:
    print(name)