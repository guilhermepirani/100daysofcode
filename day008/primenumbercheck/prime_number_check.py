'''Write a function that checks whether if the number passed into it is a prime number or not.'''

#Write your code below this line 👇

def prime_checker(number):
    flag = True

    # range excludes 1 and number
    for denominator in range(2, (number)):
        # Any whole division proves the number isn't prime
        if (number % denominator) == 0:
            flag = False
            break

    if flag == True:
        print("It's a prime number.")
    else:
        print("It's not a prime number.")


#Write your code above this line 👆
    
#Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)