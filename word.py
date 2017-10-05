'''
fin = open('words.txt')
line = fin.readline()
print(line)
'''

# Exercise 1

#1

'''
line = fin.readline()
def twenty():
    fin = open('words.txt')
    for line in fin:
        word = line
        if len(word) > 20:
            print(word, len(word))

twenty()'''

#2

'''def has_no_e(word):
    returns True if the given word doesn’t have the letter “e” in it.
    for letter in word:
        if letter == 'e':
            return False
    return True
print(has_no_e('Babson'))'''

def has_no_e(word):
    '''returns True if the given word doesn’t have the letter “e” in it.'''
    return not 'e' in word.lower()
#print(has_no_e('Babson'))

def find_words_no_e():
    fin = open('words.txt')
    counter_no_e = 0
    counter_total = 0
    for line in fin:
        counter_total +=1
        word = line.strip()
        if has_no_e(word):
            #print(word)
            counter_no_e +=1
    return counter_no_e/counter_total


print(find_words_no_e()*100)

# 3

def avoids(word, forbidden):
    for letter in word:
        if letter in forbidden:
            return False
    return True


#print(avoids('Babson', 'e'))
#print(avoids('College', 'e'))

# 4

def uses_only(word, available):
    for letter in word:
        if letter not in available:
            return False
    return True

#print(uses_only('a hole face', ' acefhlo'))

# 5

def uses_all(word, required):
    for letter in required:
        if letter in word:
            return True
    return False

#print(uses_all('tomot', 'mot'))

def uses_all(word, required):
    return uses_only(required, word)

# 6

def is_abecedarian(word):
    previous = [0]
    for c in word:
        if c < previous:
            return False
        previous = c
    return True

# Exercise 2

def is_abecedarian1(word):
    previous = [0]
    iteration = 1
    while iteration > previous:
        for letter in word:
            return True
            iteration += 1
            previous += 1    
    return False

print(is_abecedarian1('alry'))
