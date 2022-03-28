# Required functions:
# (1) get user input N
# (2) find primes
# (3) print primes table


# (1) get user input
#   - take input of N from user (must be a positive integer)
#   - the input N provides the size of the primes table (the number of required
#     rows/columns is N + 1)
#   - return positive integer of type int


# (2) find primes
#   - create empty list to which primes will be appended
#   - while the length of primes list is less than N
#       - for each potential prime, check if there is a remainder after
#         dividing by each divisor between 2 and the potential prime
#           - if there is no remainder, potential prime is not a prime -> stop
#             loop and continue to next potential prime (potential prime + 1)
#           - if there is a remainder, potential prime is still a potential
#             prime -> continue to next divisor (divisor + 1)
#               - if no divisors result in a remainder of 0, number is a prime
#                 -> append to primes list and continue to next potential prime
#   - return primes list


# (3) print primes table
#   - input is a list of N primes from find primes function
#     e.g. [2, 3, 5]
#   - output multiplication table of primes with N+1 columns and N+1 rows
#     e.g. |    |  2 |  3 |  5 |
#          |  2 |  4 |  6 | 10 |
#          |  3 |  6 |  9 | 15 |
#          |  5 | 10 | 15 | 25 |
#   - for number in primes list
#       -

