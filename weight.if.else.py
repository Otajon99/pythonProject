weight=input('what is your weight? ')
A=input('Is it in Kilograms? Y/N ')
result1=2.2* float(weight)
result2=0.45* float(weight)
if A=='Y' or A=='y':
    print(f'Great, your weight is {result1} in pounds')

elif A=='N' or A=='n':
    print(f'Great, your weight is {result2} in kilograms')
else:
    print('Choose correct!')


