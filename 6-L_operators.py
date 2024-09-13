name=str(input('What is your name? '))
Length=int(len(name[:]))

if Length<3:
    print('Name should be at least 3 characters ')
elif Length>50:
    print('Name should be less than 50 characters ')
else:
    print('Name looks good!')