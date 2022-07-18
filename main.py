#!/usr/bin/env python

from functools import cmp_to_key
from re import findall
from sys import argv


def get_data(filename):
    """
    Reads data from a file and returns a list of strings.
    :param filename: The name of the file to read.
    :return: The list of strings read from the file.
    """

    with open(filename, 'r') as f:
        lines = f.readlines()
        f.close()

    return [line.strip() for line in lines]


def tokenize(item):
    """
    Tokenizes a string into a list of characters and floating
    point numbers.
    :param item: The string to tokenize.
    :return: The list of tokens.
    """

    regex = r'[a-zA-Z.]|[0-9]+[.]?[0-9]*'
    tokens = findall(regex, item)

    for i in range(len(tokens)):
        if tokens[i].isdigit():
            tokens[i] = float(tokens[i])
        elif len(tokens[i]) > 1 and '.' in tokens[i] or len(tokens[i]) > 1 and '-' in tokens[i]:
            tokens[i] = float(tokens[i])

    return tokens


def compare_strings(left, right):
    """
    Compares two strings and returns an integer indicating
    whether the first string is less than, equal to, or
    greater than the second string.
    :param left: The first string to compare.
    :param right: The second string to compare.
    :return: The result of the comparison.
    """

    if left < right:
        return -1
    elif left > right:
        return 1
    else:
        return 0


def compare_floats(left, right):
    """
    Compares two floats and returns an integer indicating
    whether the first float is less than, equal to, or
    greater than the second float.
    :param left: The first float to compare.
    :param right: The second float to compare.
    :return: The result of the comparison.
    """

    if left < right:
        return -1
    elif left > right:
        return 1
    else:
        return 0


def compare_string_and_float(left, right):
    """
    Handles cases where a floating point number and
    a string are compared.
    :param left: The first token to compare.
    :param right: The second token to compare.
    :return: The result of the comparison.
    """

    if isinstance(left, float):
        return -1
    elif isinstance(right, float):
        return 1
    else:
        return 0


def compare_tokens(left, right):
    """
    Compares two tokens and returns an integer indicating
    whether the first token is less than, equal to, or
    greater than the second token.
    :param left: The first token to compare.
    :param right: The second token to compare.
    :return: The result of the comparison.
    """

    if isinstance(left, float):
        if isinstance(right, float):
            return compare_floats(left, right)
        else:
            return compare_string_and_float(left, right)
    elif isinstance(right, float):
        return compare_string_and_float(left, right)
    else:
        return compare_strings(left, right)


def comparator(left, right):
    """
    Controls the comparison of two inputs.
    :param left: The first input to compare.
    :param right: The second input to compare.
    :return: The result of the comparison.
    """

    left = tokenize(left)
    right = tokenize(right)

    result = 0

    for i in range(min(len(left), len(right))):
        result = compare_tokens(left[i], right[i])
        if result != 0:
            break

    if result == 0:
        return len(left) - len(right)
    return result


def intuitive_sort(collection):
    """
    Lexicographically sorts a list of strings in an intuitive
    order.
    :param collection: The list of strings to sort.
    :return: The sorted list of strings.
    """

    sorted_collection = sorted(collection, key=cmp_to_key(comparator))
    return sorted_collection


if __name__ == '__main__':
    items = get_data(argv[1])
    items = intuitive_sort(items)
    print(items)
