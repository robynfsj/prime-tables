"""Helper functions that generate number sequences."""


def find_primes(n):
    """Find first n prime numbers and return in a list.

    Starting at 2 (the first potential prime number), function assesses
    whether each consecutive number is a prime number. It iterates over
    each divisor between 2 and the square root of the potential prime
    and checks if there is a remainder when the potential prime is
    divided by the divisor. If no divisor yields a remainder, the
    potential prime is appended to the primes list. Function runs until
    the length of the primes list equals n.

    :param n: Number of prime numbers to find.
    :return: First n prime numbers.
    :rtype: list
    """
    primes = []
    potential_prime = 2

    while len(primes) != n:
        for divisor in range(2, int(potential_prime ** (1/2)) + 1):
            if potential_prime % divisor == 0:
                break
        else:
            primes.append(potential_prime)
        potential_prime += 1

    return primes


# POSSIBLE EXTENSION: This is where I would define more functions to calculate 
# other sequences. These could be used as the multipliers in the multiplication 
# table instead of the prime numbers, e.g.
#
# def find_fibonacci(n):
#     ...
#
# def find_arithmetic_seq(n, common_dif):
#     ...
#
# etc.
