def find_primes(n):
    primes = []
    potential_prime = 2

    while n != 0:
        for divisor in range(2, int(potential_prime ** (1/2)) + 1):
            if potential_prime % divisor == 0:
                break
        else:
            primes.append(potential_prime)
            n -= 1
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
