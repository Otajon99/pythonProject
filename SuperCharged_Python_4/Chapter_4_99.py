# join method on a list

str_list=[]
n=ord("a")
for i in range(n,n+26):
    str_list+=chr(i)
    alph_str="".join(str_list)
print(str_list)


# Fibonacci- Generating function

def fibo(n):
    a,b=1,0
    while a<=n:
        print(a,end=" ")
        a,b=a+b,a
fibo(3)
