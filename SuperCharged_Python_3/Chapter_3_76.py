def main():
    my_list=[]
    while True:
        s=input("Enter next name: ")
        if len(s)==0:
            break
        my_list.append(s)
    my_list.sort()
    print("Here is the sorted list ")
    for a_word in my_list:
        print(a_word,end=" ")

main()