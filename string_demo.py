#team = 'New England Patriots'

#letter = team[0]

# print(len(team))

#index = 0
'''for i  in range(len(team)):
    if team[i] != ' ':
        print(team[i]) 



for letter in team:
    print(letter)'''


prefixes = 'JKLMNOPQ'
suffix = 'ack'

'''for letter in prefixes:
    if letter == 'O' or letter == 'Q':
        print(letter + 'u' + suffix)
    else:
        print(letter + suffix)'''

#print(team[0:11])
#print(team[12:20])

#print(team[ :11])
#print(team[12: ])

#print(team[::-1]) # :: means how many spaces between. Step size

#print(team[::-2])

#print(team[4:3]) #Returns nothing

team = 'New England Patriots'
# team[12:20] = 'Seahawks'

new_team = team[:12] + 'Beavers'
print(new_team)

def find(word, letter):
    index = 0
    while index < len(word):
        if word[index] == letter:
            return index
        index = index + 1
    return -1

#print(find(team, 'e'))

def count(word, letter):
    c = 0
    for x in word:
        if x == letter:
            c = c + 1
    return c
print(count(team, 'e'))

number_of_vowels = count(team, 'a') + count(team, 'e') + count(team, 'i') + count(team, 'o') + count(team, 'u') + count(team, 'y')

print(number_of_vowels)

vowels = 'aeiouy'
number_of_vowels = 0