def padding(num, primes):
    len_num = len(str(num))
    len_max_table_val = len(str(primes[-1] ** 2))
    len_padding = len_max_table_val - len_num
    return " " * len_padding


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
            print(f" {padding(left * top, primes)}{left * top} |", end="")

        # Ensure "|" is only printed on new line if not last row/left prime.
        if left != primes[-1]:
            print("\n|", end="")
            