# 1 Write a program to count a number of vowels and consonants
string = "GeekforGeeksaoefdsasgbkvb!"
vowels = "aeiouAEIOU"

count = sum(string.count(vowel) for vowel in vowels)
print(count)




# 2- choice of programming to find of vowels and consonants
def is_lower_case_alphabet(ch):
	return 'a' <= ch <= 'z'

def is_vowel(ch):
	return ch in {'a', 'e', 'i', 'o', 'u'}

word = "programming"
consonant_count = 0

for i in range(len(word)):
	# Convert to lowercase for case-insensitivity
	ch = word[i].lower()
	if is_lower_case_alphabet(ch) and not is_vowel(ch):
		consonant_count += 1

print(f"Number of consonants: {consonant_count} ")


# 2-problem on 2 chapter

main="      Hello       "
print(main.rjust(len(main)+2,"$" ))
print(main.ljust(len(main)+2,"$" ))
