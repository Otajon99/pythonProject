
def find_divisor(n,m):
        if n%m==0 and m<n:
            print(m,"divides evenly into", n)
        else:
            print("No divisor found!")

find_divisor(28,4)