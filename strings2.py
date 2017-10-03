# Exercise 3

print('    spacious    '.strip())

print('1,2,3'.split(',', maxsplit=1))

print('Chris'.replace('Chris','Stephanie'))

# Exercise 4

#1

word = 'bananas'
count = 0
for letter in word:
    print(ord(str(letter))-96)
        
word1 = 'rice'
count = 0
for letter in word1:
    print(ord(str(letter))-96)

word2 = 'paprika'
count = 0
for letter in word2:
    print(ord(str(letter))-96)

word3 = 'potato chips'
count = 0
for letter in word3:
    print(ord(str(letter))-96)

#2

word = 'bananas'
count = 0
for letter in word:
    print(float(ord(str(letter))-96))

word1 = 'rice'
count = 0
for letter in word1:
    print(float(ord(str(letter))-96))

word2 = 'paprika'
count = 0
for letter in word2:
    print(float(ord(str(letter))-96))

word3 = 'potato chips'
count = 0
for letter in word3:
    print(float(ord(str(letter))-96))



