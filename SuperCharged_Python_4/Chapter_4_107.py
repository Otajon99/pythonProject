
test_str=input("Enter test string: ")
a_list=[c.upper() for c in test_str if c.isalnum()]
print(a_list==a_list[::-1])



# replace method
s="    "
s=s.replace(" ","")
a_list=[c for c in s if c not in "aeiou"]
s="".join(a_list)

