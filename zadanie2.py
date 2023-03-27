# Zadanie 2
import math


def prime(*number):
    is_prime = True
    for n in number:
        if n == 0 or n == 1:
            is_prime = False
        else:
            for i in range(2, int(math.sqrt(n))+1):
                if n % i == 0:
                    is_prime = False
        print(str(n), end="")
        if is_prime is False:
            print(" is not prime")
        else:
            print(" is prime")
        is_prime = True


prime(0, 1, 2, 3, 4, 5)
