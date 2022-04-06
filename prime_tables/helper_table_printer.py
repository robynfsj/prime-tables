"""Helper functions for printing multiplication tables."""


def generate_multiplication_table(sequence):
    """Generate a multiplication table from the given sequence.

    :param sequence: Integers to be used as multipliers in the table.
    :type sequence: list
    :return: Multiplication table of provided sequence.
    :rtype: list of lists
    """
    row1 = [[""] + sequence]
    subsequent_rows = [
        [i] +  # first value in row (a number in the sequence)
        [i*j for j in sequence] for i in sequence  # multiples
    ]
    return row1 + subsequent_rows


def print_table(table):
    """Prints multiplication table of a sequence to the console.
    
    :param table: Integers to be used as multipliers in the table.
    :type table: list of lists
    :return: None (prints to console).
    ":rtype: NoneType
    """
    padding = len(str(table[0][-1] ** 2))

    for row in table:
        for val in row:
            print(str(val).rjust(padding), end=" ")
        print()
