from myfunction import *

exit_list = ['quit']
while True:
    n = input("Please insert a value: or enter quit to end the program \n")
    if n.isdigit():
        print('is the entered value plaindeome?',is_palindrome(n),'\n')
        print('is the entered value prime?', is_prime(n), '\n')
        print('Divisors and max divisor', divisors(n))
        print('number of digits = ', len(n))
    elif n in exit_list:
        print('Closing')
        break
