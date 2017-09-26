
# Question 1
import math
def crazy_about_9(a, b):

    """

    a, b: two integers

    

    Returns True if either one is 9, or if their sum or difference is 9. 

    """
    
    if a or b == 9:
        return True
    elif a + b == 9:
        return True
    elif b - a == 9:
        return True
    elif a - b == 9:
        return True
    else:
        return False





    





# When you've completed your function, uncomment the

# following lines and run this file to test!



print(crazy_about_9(2, 9))

print(crazy_about_9(4, 5))

print(crazy_about_9(3, 8))

# Question 2
def leap_year(year):

    """

    year(int): a year



    Returns True if year is a leap_year, False if year is not a leap_year.

    """

    if year / 4 == int():
        return True
    elif year / 400 == int():
        return True
    elif year / 100 == int():
        return False
    else:
        return False





# When you've completed your function, uncomment the

# following lines and run this file to test!



print(leap_year(1900))

print(leap_year(2016))

print(leap_year(2017))

print(leap_year(2000))

#Question 3


"""

-----------------------------------------------------------------------

Question 3:



Write a function with loops that computes The sum of all squares between

1 and n (inclusive).



"""
def sum_squares(n):
    for i in range(101):
        print(math.sqrt(n))


    





# When you've completed your function, uncomment the

# following lines and run this file to test!



# print(sum_squares(1))

# print(sum_squares(100))