import unittest

from os import getenv

from main import get_data
from main import tokenize
from main import compare_strings
from main import compare_floats
from main import compare_string_and_float
from main import compare_tokens
from main import comparator
from main import intuitive_sort


class IntuitiveSortTests(unittest.TestCase):
    """
    This class contains the unit tests for the Intuitive Sort module.
    """

    def test_get_input(self):
        """
        This test checks that the get_data function returns the
        correct data.
        :return: The list of data found in the input file.
        """

        data = get_data(getenv('TEST_DATA_FILE'))
        self.assertEqual(len(data), 45)

    def test_compare_strings_less_than(self):
        """
        This test checks that the compare_strings function returns the
        correct value when the first string is less than the second.
        :return: The result of the comparison (-1).
        """

        self.assertEqual(compare_strings('a', 'b'), -1)

    def test_compare_strings_equal(self):
        """
        This test checks that the compare_strings function returns the
        correct value when the first string is equal to the second.
        :return: The result of the comparison (0).
        """

        self.assertEqual(compare_strings('a', 'a'), 0)

    def test_compare_strings_greater_than(self):
        """
        This test checks that the compare_strings function returns the
        correct value when the first string is greater than the second.
        :return: The result of the comparison (1).
        """

        self.assertEqual(compare_strings('b', 'a'), 1)

    def test_compare_floats_less_than(self):
        """
        This test checks that the compare_floats function returns the
        correct value when the first float is less than the second.
        :return: The result of the comparison (-1).
        """

        self.assertEqual(compare_floats(1.0, 2.0), -1)

    def test_compare_floats_equal(self):
        """
        This test checks that the compare_floats function returns the
        correct value when the first float is equal to the second.
        :return: The result of the comparison (0).
        """
        self.assertEqual(compare_floats(1.0, 1.0), 0)

    def test_compare_floats_greater_than(self):
        """
        This test checks that the compare_floats function returns the
        correct value when the first float is greater than the second.
        :return: The result of the comparison (1).
        """

        self.assertEqual(compare_floats(2.0, 1.0), 1)

    def test_compare_string_and_float_less_than(self):
        """
        This test checks that the compare_string_and_float function
        returns the correct value when the first input is less than
        the second.
        :return: The result of the comparison (-1).
        """

        self.assertEqual(compare_string_and_float(1.0, 'a'), -1)

    def test_compare_string_and_float_equal(self):
        """
        This test checks that the compare_string_and_float function
        returns the correct value when the first input is equal to
        the second.
        :return: The result of the comparison (0).
        """

        self.assertEqual(compare_string_and_float('a', 'a'), 0)

    def test_compare_string_and_float_greater_than(self):
        """
        This test checks that the compare_string_and_float function
        returns the correct value when the first input is greater than
        the second.
        :return: The result of the comparison (1).
        """

        self.assertEqual(compare_string_and_float('a', 1.0), 1)

    def test_compare_tokens_lower_value_first(self):
        """
        This test checks that the compare_tokens function returns the
        correct value when the first token is less than the second.
        :return: The result of the comparison (-1).
        """

        self.assertEqual(compare_tokens('a', 'b'), -1)

    def test_compare_tokens_identical_values(self):
        """
        This test checks that the compare_tokens function returns the
        correct value when the first token is equal to the second.
        :return: The result of the comparison (0).
        """

        self.assertEqual(compare_tokens('a', 'a'), 0)

    def test_compare_tokens_higher_value_first(self):
        """
        This test checks that the compare_tokens function returns the
        correct value when the first token is greater than the second.
        :return: The result of the comparison (1).
        """

        self.assertEqual(compare_tokens('b', 'a'), 1)

    def test_compare_tokens_not_comparable_less_than(self):
        """
        This test checks that the compare_tokens function returns the
        correct value when the first token is a number and the second
        token is a string.
        :return: The result of the comparison (-1).
        """

        self.assertEqual(comparator('1', 'a'), -1)

    def test_compare_tokens_not_comparable_greater_than(self):
        """
        This test checks that the compare_tokens function returns the
        correct value when the first token is a string and the second
        token is a number.
        :return: The result of the comparison (1).
        """

        self.assertEqual(comparator('a', '1'), 1)

    def test_comparator_less_than(self):
        """
        This test checks that the comparator function returns the
        correct value when the first input is less than the second.
        :return: The result of the comparison (-1).
        """

        self.assertEqual(comparator('a', 'b'), -1)

    def test_comparator_equal(self):
        """
        This test checks that the comparator function returns the
        correct value when the first input is equal to the second.
        :return: The result of the comparison (0).
        """

        self.assertEqual(comparator('a', 'a'), 0)

    def test_comparator_greater_than(self):
        """
        This test checks that the comparator function returns the
        correct value when the first input is greater than the second.
        :return: The result of the comparison (1).
        """

        self.assertEqual(comparator('b', 'a'), 1)

    def test_comparator_not_comparable_less_than(self):
        """
        This test checks that the comparator function returns the
        correct value when the first input contains a number and the
        second input does not.
        :return: The result of the comparison (-1).
        """

        self.assertEqual(comparator('a12d', 'abcd'), -1)

    def test_comparator_not_comparable_greater_than(self):
        """
        This test checks that the comparator function returns the
        correct value when the first input does not contain a number
        and the second input does.
        :return: The result of the comparison (1).
        """

        self.assertEqual(comparator('abcd', 'a12d'), 1)

    def test_tokenize_string(self):
        """
        This test checks that the tokenize function returns the
        correct value when the input is a string.
        :return: The tokenized result (['a', 'b', 'c']).
        """

        self.assertEqual(tokenize('abc'), ['a', 'b', 'c'])

    def test_tokenize_float(self):
        """
        This test checks that the tokenize function returns the
        correct value when the input is a float.
        :return: The tokenized result ([3.14]).
        """

        self.assertEqual(tokenize('3.14'), [3.14])

    def test_tokenize_integer(self):
        """
        This test checks that the tokenize function returns the
        correct value when the input is an integer.
        :return: The tokenized result ([315]).
        """

        self.assertEqual(tokenize('315'), [315])

    def test_tokenize_mixed_values(self):
        """
        This test checks that the tokenize function returns the
        correct value when the input contains mixed values.
        :return: The tokenized result ([3.14, 'a', 'b', 'c']).
        """
        self.assertEqual(tokenize('3.14abc'), [3.14, 'a', 'b', 'c'])

    def test_intuitive_sort_less_than(self):
        """
        This test checks that the intuitive_sort function returns the
        correct value when the larger value is earlier in the list.
        :return: The sorted result (['a', 'b']).
        """

        self.assertEqual(intuitive_sort(['b', 'a']), ['a', 'b'])

    def test_intuitive_sort_equal(self):
        """
        This test checks that the intuitive_sort function returns the
        correct value when the values are equal.
        :return: The sorted result (['a', 'a']).
        """

        self.assertEqual(intuitive_sort(['a', 'a']), ['a', 'a'])

    def test_intuitive_sort_greater_than(self):
        """
        This test checks that the intuitive_sort function returns the
        correct value when the smaller value is earlier in the list.
        :return: The sorted result (['a', 'b']).
        """

        self.assertEqual(intuitive_sort(['a', 'b']), ['a', 'b'])

    def test_intuitive_sort_not_comparable(self):
        """
        This test checks that the intuitive_sort function returns the
        correct value when the values are not comparable.
        :return: The sorted result (['a12d', 'abcd']).
        """

        self.assertEqual(intuitive_sort(['abcd', 'a12d']), ['a12d', 'abcd'])


if __name__ == '__main__':
    unittest.main()
