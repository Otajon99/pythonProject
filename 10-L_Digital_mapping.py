phone=input("Phone: ")
digits_mapping= {
    "1":"One",
    "2":"Two",
    "3":'Tree',
}
output=''
for ch in phone:
     output+=digits_mapping.get(ch,'!')+ ' '

print(output)