from unittest import TestCase, main
from prime_tables.helper_table_printer import padding, print_table


class TestPadding(TestCase):

    def test_correct_padding(self):
        num = 2
        primes = [2, 3, 5]
        # Largest value in table is 25 so expect a string of one space
        # when printing the number 2.
        self.assertEqual(padding(num, primes), " ")

    def test_incorrect_padding(self):
        self.assertNotEqual(padding(1, [2, 3, 5]), "")


if __name__ == '__main__':
    main()
