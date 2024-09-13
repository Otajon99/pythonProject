message=input('>')
words=message.split(' ')
emojis={
    ":)":'\U0001F604',
    "(:":'\U0001F614'
}
output=''
for word in words:
    output+=emojis.get(word, word)+' '

print(output)