text=[3,6,9,10]

text.append(1)            # adding new str or int on the list
text.sort()
text.remove(10)
text_a=text[0:3:2]        # slicing and count every other number on the list
rev_text=text[::-1]       # reversing


print(text)
print(text[0])
print(text[3])
print(text_a)
print(rev_text)



a_list=["David","Tom","Jerry"]
for i in range(len(a_list)):
    print(a_list[i])


# Assigning and slicing

my_list=[1,2,3,4]
my_list[0:0]=[-50,-40]
print(my_list)



my_list=[10,20,30,40,50,60]
my_list[1:4]=[707,777]               # removing [1:4] parts and replacing with 707 and 777
print(my_list)


a_list =[1,3,5,0,2]
b_list=a_list
c_list=a_list[:]
print(b_list)                        # alias and comparing
print(c_list)                        # coping a_list

