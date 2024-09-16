# 1 Write a program to count a number of vowels and consonants


messages=["Otajon wake up at 7 in the morning!"]
while True:
    for message in messages[:]:
        i = 0
        if message == "a" or "o" or "u" or "e" or "i":
            i += 1
        print(f"Number of vowels is {i} and {message[i]}")

