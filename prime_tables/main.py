"""Generate a table of prime numbers from user input."""

import helper_user_input as inp
import helper_sequence_generator as seq
import helper_table_printer as tbl


def main():
    n = inp.get_num_of_primes()
    sequence = seq.find_primes(n)

    tbl.print_table(sequence)
    print("\n")  # prevents end of line mark when running in terminal


if __name__ == "__main__":
    main()
