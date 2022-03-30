"""Helper functions for printing multiplication tables."""


def padding(num, primes):
    """Calculates length of padding required to align value in table.

    Calculates the largest value that will be printed in the table and
    converts this to a string so that the number of digits can be
    retrieved with len(). Does the same for the number to be printed
    then calculates the difference in order to return a string of spaces
    of the required length.

    :param num: Value to be printed in table
    :param primes: Prime numbers to be used as multipliers in the table.
    :type num: int
    :type primes: list
    :return: A string containing the required number of spaces.
    :rtype: str
    """
    len_num = len(str(num))
    len_max_table_val = len(str(primes[-1] ** 2))
    len_padding = len_max_table_val - len_num
    return " " * len_padding


def print_table(primes):
    """Prints multiplication table of primes to console.

    Prints empty first value then iterates over list of primes, printing
    each one on the same line. For each subsequent row, prints prime
    then multiples.
    
    :param primes: Prime numbers to be used as multipliers in the table.
    :type primes: list
    :return: None (prints to console).
    ":rtype: NoneType
    """
    # Print first value (which is empty).
    # Setting end="" overrides default of starting a new line.
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
            print(f" {padding(left * top, primes)}{left * top} |", end="")

        # Ensure "|" is only printed on new line if not last row/left prime.
        if left != primes[-1]:
            print("\n|", end="")
