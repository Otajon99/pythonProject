# A=P(1+n/100)^time
P=input("Enter the amount of borrowing money? ")
while True:
    if float(P)>0:
        print(f"You need ${P} loan ")
        break
    elif float(P)<=0:
        print("Please enter correct amount: ")
        break

n=input("Enter the percentage: ")
print


