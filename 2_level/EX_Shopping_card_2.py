fruits=[]
prices=[]
total=0

while True:
    fruit=input("Input your fruit: (q to quit) ")
    if fruit.lower()=="q":
        break
    else:
        price=input(f"Input the price of {fruit}: $")
        fruits.append(fruit)
        prices.append(price)

print("------Your Card-------")
for fruit in fruits:
    print(fruit, end=" ")

for price in prices:
    total+=float(price)

print('')
print(f"Your total price is ${total}")
