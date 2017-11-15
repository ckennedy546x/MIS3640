alphabet = "abcdefghijlmnopqrstuvwxyz"
print(alphabet)
ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def create_moved_dict(move):

    '''
        Creates a dictionary that maps every letter to a
        character moved down the alphabet by the input move. 

        move: an integer, 0 <= move < 26

        Returns: a dictionary

        Example: an_instance_of_Text.create_moved_dict(2) would generate
        {'a': 'c', 'b': 'd', 'c':'e', ...}  
    '''
    dict1 = {}
    str1 = ALPHABET
    for s in str1:
        if (ord(s)+shift-65) < 26 :
             dict1[s] = chr(ord(s)+shift)
        elif (ord(s)+shift-65) >= 26 :
             dict1[s] = chr(ord(s)+shift-26)

    str1 = alphabet
    for s in str1:
        if (ord(s)+shift-97) < 26 :
             dict1[s] = chr(ord(s)+shift)
        elif (ord(s)+shift-97) >= 26 :
             dict1[s] = chr(ord(s)+shift-26)

    return dict1
print(create_moved_dict(8))

if (number < 0) or (number > 999):
        print("Error! Your number must be between 0 and 999")
    else:
        if (number >= 0) and (number < 10):
            print(trans[str(number)])
        elif (number >= 10) and (number < 20):
            print(trans[str(10)], trans[str(number-10)])
        elif (number >= 20) and (number < 100):
            num1 = list(str(number))
            if num1[1] == '0':
                print(trans[str(num1[0])], trans[str(10)])
            else:
                print(trans[str(num1[0])], trans[str(10)], trans[str(num1[1])])
        elif number == 100:
            print(trans[str(100)])
        elif (number >= 101) and (number < 1000):
            num2 = list(str(number)) 
            if (num2[1] == '0') and (num2[2] == '0'): 
                print(trans[str(num2[0])], trans[str(100)])
            elif (num2[1] == '0'):
                print(trans[str(num2[0])], trans[str(100)], trans[str(0)], trans[str(num2[2])])
            elif (num2[2] == '0'):
                print(trans[str(num2[0])], trans[str(100)], trans[str(num2[1])], trans[str(10)])
            else:
                print(trans[str(num2[0])], trans[str(100)], trans[str(num2[1])], trans[str(10)], trans[str(num2[2])])