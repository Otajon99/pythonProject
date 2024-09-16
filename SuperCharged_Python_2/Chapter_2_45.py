n=ord("A")
a_lst=[ ]
for i in range(n, n+26):
    a_lst.append(chr(i))

s=",".join(a_lst)     # Showing how to use ~join method
print(s)
print(a_lst)
