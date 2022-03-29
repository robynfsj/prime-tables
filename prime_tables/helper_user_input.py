def get_num_of_primes():
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
        