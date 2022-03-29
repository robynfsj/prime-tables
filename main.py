# Required functions:
# (1) get user input N
# (2) find primes
# (3) print primes table


# (1) get user input
#   - take input of N from user (must be a positive integer)
#   - the input N provides the size of the primes table (the number of required
#     rows/columns is N + 1)
#   - return positive integer of type int

def get_num_of_primes():
    try:
        n = int(input("Number of primes to calculate: "))
        if n < 1:
            raise ValueError
    except ValueError:
        print("Invalid input. Please enter a positive integer.\n")
        return get_num_of_primes()
    else:
        return n


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

def find_primes(n):
    primes = []
    potential_prime = 2

    while n != 0:
        for divisor in range(2, potential_prime):
            if potential_prime % divisor == 0:
                break
        else:
            primes.append(potential_prime)
            n -= 1
        potential_prime += 1

    return primes


# (3) print primes table
#   - input is a list of N primes from find primes function
#     e.g. [2, 3, 5]
#   - output multiplication table of primes with N+1 columns and N+1 rows
#     e.g. |    |  2 |  3 |  5 |
#          |  2 |  4 |  6 | 10 |
#          |  3 |  6 |  9 | 15 |
#          |  5 | 10 | 15 | 25 |


def padding(num, primes):
    len_num = len(str(num))
    len_max_table_val = len(str(max(primes) ** 2))
    len_padding = len_max_table_val - len_num
    return " " * len_padding
    # return " " * (len(str(max(primes_list) ** 2)) - len(str(num)))


def print_table(primes):

    # Print first value (which is empty).
    print(f"| {padding(0, primes)}  |", end="")

    # Print primes along first row.
    for num in primes:
        print(f" {padding(num, primes)}{num} |", end="")

    # Print subsequent rows (prime followed by multiples).
    print("\n|", end="")
    # Print left prime.
    for left in primes:
        print(f" {padding(left, primes)}{left} |", end="")
        # Print multiples.
        for top in primes:
            print(f" {padding(left*top, primes)}{left*top} |", end="")
            
        # Ensure "|" is only printed on new line if not last row/left prime.
        if left != primes[-1]:
            print("\n|", end="")

# manual test
print_table(find_primes(get_num_of_primes()))
