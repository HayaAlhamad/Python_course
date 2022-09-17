#tema 1
#question 1

my_list = [7, 8, 9, 2, 3, 1, 4, 10, 5, 6]
print('\n Original List:',my_list)

#Sort the List of numbers in Ascending Order

#using sorted() function

ascending_ordered_list = sorted(my_list)

print('\n Ascending ordered List:', ascending_ordered_list)

print('\n Original List:',my_list)



#Sort the List of numbers in descending order

#using sorted() function

descending_ordered_list = sorted(my_list, reverse=True)

print('\n Descending ordered List:', descending_ordered_list)

print('\n Original List:',my_list)



#display a list containing even numbers from the ordered list (using slice)

even_numbers_list = ascending_ordered_list [1::2]

print('\n Even numbers list:', even_numbers_list)



#display a list containing the odd numbers in the ordered list (using slice)

odd_numbers_list = ascending_ordered_list[0::2]

print('\n Odd numbers list:', odd_numbers_list)


#display a list containing the numbers that are multiples of 3 (using slice)

muliples_of_3_list = ascending_ordered_list[2::3]

print('\n Number 3 multipliers', muliples_of_3_list)


print('\n ----------------------------------------------------------------------------------------------------------')

#TEMA2


#Write a function that takes an undefined number of parameters and calculate the sum of the parameters that represent integers or real numbers.


print('function that takes an undefined number of parameters ')
def my_sum(*args):
    total = 0
    for argument in args:
        if type(argument) != int  and  type(argument)!= float:
            print('not a number:',argument)
        else:
            total += argument
    print('The sum of numbers in this function is',total)




my_sum(1,444,8,'hello')

print('\n')
print('---------------------------------------------------------------------------------------------------')

#Write a recursive function that receives an integer as a parameter and returns:


# sum of all numbers from [0, n]

n = int(input("Please insert an int value:"))
def sum_of_all_numbers(n):

        if n == 0:
            return 0
        return n + sum_of_all_numbers(n - 1)




print('Sum of all numbers from 0 to n =',sum_of_all_numbers(n))



#sum of even numbers from [0, n]

def sum_of_even_numbers(n):
    total_even = 0
    for i in range(n):
        if i%2 == 0:
            total_even += i
    return total_even

print('Sum of EVEN numbers from 0 to n =',sum_of_even_numbers(n))


#sum of odd numbers from [0. n]
def sum_of_odd_numbers(n):
    total_odd = 0
    for i in range(n+1):
        if i%2 != 0:
            total_odd += i
    return total_odd

print('Sum of ODD numbers from 0 to n =',sum_of_odd_numbers(n))


print('\n')
print('------------------------------------------------------------------------------------------------')

#Write a function that reads from the keyboard and returns the value if it is an integer, otherwise it returns value 0.

my_variable = input("insert a value:")


def my_check(my_variable):
    try:
        val = int(my_variable)
        return my_variable
    except ValueError:
        print("That's not an int!")
        return 0


print('the value of user input is',my_check(my_variable))

