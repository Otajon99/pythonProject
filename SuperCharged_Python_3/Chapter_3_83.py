# method of reducing function using by lambda

my_f=lambda x,y: x+y
sum1=my_f(3,7)
print(sum1)


# insted, we can use this

import functools

t5=functools.reduce(lambda x,y: x+y, [1,2,3,4,5])

print(t5)