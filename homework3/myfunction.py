def is_palindrome(n):
    try:
        val = int(n)
        if n == str(n)[:: -1]:
            palindrome = True
        else:
            palindrome = False
    except ValueError:
        print("That's not a valid number, Try Again !")
    return palindrome

def is_prime(n):

    n = int(n)
    if n < 2:
        prime = False

    for i in range(2, n):
        if n % i == 0:
            prime = False
        else:
            prime = True
    return prime

def divisors(n):
    divisors_list = []
    max_divisor = []
    n = int(n)

    for i in range(2, n):
        if n % i == 0:
            divisors_list.append(i)
            max_divisor = [i]
        else:
            max_divisor = [n]
    return divisors_list, max_divisor
