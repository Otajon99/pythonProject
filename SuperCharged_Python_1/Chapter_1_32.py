# 1-Test Question/Answer

def test_func():
    name=input("What is your name? ")
    age=int(input("What is your age? "))
    address=input("What is your address ")
    print(f"Great! You are {name}, {age} years old and you are from {address}")

test_func()


# 2-Test Question/Answer
def sphere_volume():
    pi=3.14
    r=int(input("Enter the radius of Sphere: "))
    v=4/3 * pi * pow(r, 3)
    print(v)

sphere_volume()