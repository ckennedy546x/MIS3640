trans = {'0':'ling', '1':'yi', '2':'er', '3':'san', '4': 'si', '5':'wu', 
         '6':'liu', '7':'qi', '8':'ba', '9':'jiu', '10': 'shi', '100': 'bai'}



def speak_Chinese(number):
    '''
    number: an integer, 0<=number<=999

    Returns: a string that is the number in Chinese
    '''
    if (number < 0) or (number > 999):
        print("Error! Your number must be between 0 and 999")
    else:
        if (number >= 0) and (number < 10):
            return trans[str(number)]
        elif (number >= 10) and (number < 20):
            return trans[str(10)] + " " + trans[str(number-10)]
        elif (number >= 20) and (number < 100):
            num1 = list(str(number))
            if num1[1] == '0':
                return trans[str(num1[0])] + " " + trans[str(10)]
            else:
                return trans[str(num1[0])] + " " + trans[str(10)] + " " + trans[str(num1[1])]
        elif number == 100:
                return trans[str(100)]
        elif (number >= 101) and (number < 1000):
            num2 = list(str(number)) 
            if (num2[1] == '0') and (num2[2] == '0'): 
                return trans[str(num2[0])] + " " + trans[str(100)]
            elif (num2[1] == '0'):
                return trans[str(num2[0])] + " " + trans[str(100)] + " " + trans[str(0)] + " " + trans[str(num2[2])]
            elif (num2[2] == '0'):
                return trans[str(num2[0])] + " " + trans[str(100)] + " " + trans[str(num2[1])] + " " + trans[str(10)]
            else:
                return trans[str(num2[0])] + " " + trans[str(100)] + " " + trans[str(num2[1])] + " " + trans[str(10)] + " " + trans[str(num2[2])]
                
        
            

    


# For testing
def main():
    print(speak_Chinese(36))
    print('In Chinese: 36 = san shi liu')
    print(speak_Chinese(20))
    print('In Chinese: 20 = er shi')
    print(speak_Chinese(16))
    print('In Chinese: 16 = shi liu')
    print(speak_Chinese(200))
    print('In Chinese: 200 = er bai')
    print(speak_Chinese(109))
    print('In Chinese: 109 = yi bai ling jiu')
    print(speak_Chinese(999))
    print('In Chinese: 999 = jiu bai jiu shi jiu')

if __name__ == '__main__':
    main()
