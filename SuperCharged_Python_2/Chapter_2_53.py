me_str="Otajon Burkhonov, PHD"
me_str1="Mr, Otajon Burkhonov"
is_doc=me_str.endswith("PHD")         # boolean method (True,False)
is_doc1=me_str.startswith("PHD")
is_doc3=me_str1.endswith("Mr")         # boolean method (True,False)
is_doc4=me_str1.startswith("Mr")
print(is_doc)
print(is_doc1)
print(is_doc3)
print(is_doc4)


frank_str="doo be doo be doo ..."
print(frank_str.find("doo"))      #  0
print(frank_str.index("doo"))     #  0
print(frank_str.rfind("doo"))     #  14   # find the string begin from the end



# Breaking up words using ~split() method

list_1="Otajon Bobur Azamat Jonibek".split()
list_2="Otajon Bobur    Azamat Jonibek".split(" ")
list_3="Otajon Bobur Azamat Jonibek".split(",")
print(list_1)
print(list_2)
print(list_3)



name_str="       Will Gold       "
new_str=name_str.strip()     # removes all white space from start and end
new_str2=name_str.lstrip()    # removes white space from leading(beginning)
new_str3=name_str.rstrip()

print(new_str)
print(new_str2)
print(new_str3)
