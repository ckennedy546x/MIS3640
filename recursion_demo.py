import time

def countdown(n):
    if n <= 0:
        print('To Infinity and Beyond!')
    else:
        print(n)
        time.sleep(1)
        countdown(n-1)


countdown(5)