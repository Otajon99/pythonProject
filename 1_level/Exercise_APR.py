# A=P(1+n/100)^time
P=float(input("Enter the amount of borrowing money? "))
time=36
while True:
    if float(P)>0:
        print(f"You need ${P} loan ")
        break
    elif float(P)<=0:
        print("Please enter correct amount: ")
        break

n=float(input("Enter the percentage: "))
A=1+n/100
B=P*pow(A,2)
print(B)

