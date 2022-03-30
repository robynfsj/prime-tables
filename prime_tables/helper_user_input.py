"""Helper functions that deal with user input."""


def get_num_of_primes():
    """Get and return the required number of primes from user via input.

    Takes user input as a string and converts it to an integer. Handles
    ValueError raised if user enters a character other than a number by
    performing a recursive call. Returns the integer if it is positive
    or performs a recursive call if it is not positive (i.e. zero or
    negative).

    :return: Number of primes to calculate. (Recursive call if invalid
             input.)
    :rtype: int
    """
    n = input("Enter number of primes to calculate (positive integer): ")

    # Handle cases where user inputs characters other than numbers.
    try:
        int_n = int(n)
    except ValueError:
        print("Invalid input. Cannot contain non-numeric characters.\n")
        return get_num_of_primes()
    else:
        # Handle cases where int is not positive.
        if int_n >= 1:
            return int_n
        else:
            print("Invalid input. Integer must be positive.\n")
            return get_num_of_primes()


# POSSIBLE EXTENSION: This is where I would define more functions that
# require user input. For example, I could add a function here to ask if
# the user wants to generate another prime table after they have already
# generated one. If I extended the application to offer sequences other
# than primes, I would add a function here to ask which sequence they
# want to generate.
