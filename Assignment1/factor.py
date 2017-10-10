def factor(n):
    '''This function will ask
    the user for an integer and 
    then print out all its factors'''

    print("The factors of", n,"are:")
    for i in range(1, n + 1): #will continue the loop until each number (or i) from 1 to the inputted number + 1 is ran
        if n % i == 0: #if the if the inputted number is divisible by the current number (or i),that means it is in fact a factor and it will be printed
            print(i) 
            # after the number (or i) is checked, the function will then proceed to check the next number in the range


num = int(input("Please enter a number: ")) #This will allow user to input a number

print(factor(num)) #This will run the function with the inputted number
    