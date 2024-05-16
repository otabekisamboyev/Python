# Teacher's Solution
def prime_checker(number):
    is_prime = True
    for num in range(2, number):
        if number % num == 0:
            is_prime = False

    if is_prime:
        print("This is prime number")
    else:
        print("This is not prime number")


'''My Solution
def prime_checker(number):
    count = 0
    for num in range(1, number + 1):
        if number % num == 0:
            count += 1

    if count == 2:  # count == 2
        print("This is prime number")
    else:
        print("This is not prime number")
'''

n = int(input("Check this number: "))
prime_checker(number=n)
