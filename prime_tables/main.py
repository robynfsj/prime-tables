import helper_user_input as inp
import helper_sequence_generator as seq
import helper_table_printer as tbl


def main():
    n = inp.get_num_of_primes()
    sequence = seq.find_primes(n)

    return tbl.print_table(sequence)


if __name__ == "__main__":
    main()
