def isPalindrome(string):
    '''The fucntion will return True if a string is a palindrome
    and False if it is not a palindrome'''
    
    if len(string) < 2: #if the length of the inputted string is less than 2 (aka 1 letter), the function will return true because 1 letter words are classified as palindromes
        return True
    if string[0] != string[-1]: #if the first letter in the palindrome is not the same as the last letter, the function will return false because the word will not be a palindrome if the first and last letter are different
        return False
    return isPalindrome(string[1:-1]) #Calls function again but remove first and last items. If they are the same, call function on what's left of string. If first and last are not the same, item is not a palindrome.


inputStr = input("Enter a string: ") #allows user to input a string
print(isPalindrome(inputStr)) #runs function
