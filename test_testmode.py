from doctest import testmod
from functools import wraps


def is_palindrome(items):
    """
    Check if an iterable (strings included), dictionary or integer is palindrome.

    Iterables:
    >>> is_palindrome([1, 2, 1])
    True
    >>> is_palindrome([1, 2])
    False

    Strings (case insensetive):
    >>> is_palindrome("hello")
    False
    >>> is_palindrome("a")
    True
    >>> is_palindrome("Madam")
    True

    Integers:
    >>> is_palindrome(121)
    True
    >>> is_palindrome(56)
    False

    A dictionary is palindrome if it consists of palindromes (both keys and values)
    >>> is_palindrome({"madam": "Hannah", "level": 121})
    True
    >>> is_palindrome({"madam": "Adam", "level": 10})
    False
    """

    if isinstance(items, int):
        items = str(items)
        return items == items[::-1]
    elif isinstance(items, (str, list)):
        result = [str(item).lower() for item in items]
        return result == result[::-1]
    elif isinstance(items, dict):
        for key, value in items.items():
            key = str(key).lower()
            value = str(value).lower()
            if key != key[::-1] or value != value[::-1]:
                return False
        return True


def filter_palindromes(items):
    """
    Remove palindromes from iterable.
    >>> filter_palindromes(["abc", "abba", 535, "leeroy", {"key": "value"}])
    ['abc', 'leeroy', {'key': 'value'}]
    """
    for item in reversed(items):
        if isinstance(item, dict):
            for key, value in item.items():
                key = str(key).lower()
                value = str(value).lower()
                if key == key[::-1] and value == value[::-1]:
                    del item[key]
        item_check = str(item).lower()
        if item_check == item_check[::-1]:
            items.remove(item)
    return items


class Palindrome:
    """
    Palindrome class

    >>> palindrome1 = Palindrome("ab")
    >>> palindrome1
    Palindrome("abba")
    >>> palindrome2 = Palindrome("madam")
    >>> palindrome2
    Palindrome("madam")
    >>> sum1 = palindrome1 + palindrome2
    >>> sum1
    Palindrome("abbamadamabba")
    >>> sum2 = palindrome1 + "madam"
    >>> sum2
    Palindrome("abbamadamabba")
    >>> sum1 == sum2
    True
    """

    def __init__(self, name):
        self.name = name if name == name[::-1] else f'{name}{name[::-1]}'

    def __repr__(self):
        return f'Palindrome("{self.name}")'

    def __eq__(self, other):
        return self.name == other.name

    def __add__(self, other):
        if isinstance(other, str):
            new_name = f'{self.name}{other}{self.name}'
        else:
            new_name = f'{self.name}{other.name}{self.name}'
        return Palindrome(new_name)


def decor(func):
    @wraps(func)
    def wrapper(number):
        result = func(number)
        return f'Result: {result}'

    return wrapper


@decor
def decorate_me(some_int):
    """
    Decorate (but do not modify) this function so it runs and passes the following doctest:
    >>> decorate_me(25)
    'Result: 50'
    >>> decorate_me(196)
    'Result: 392'
    """
    return some_int * 2


def magic(hat=[]):
    """
    Complete doctest:

    >>> magic()
    ['🕊️']
    >>> magic()
    ['🕊️', '🕊️']
    >>> hat = []
    >>> magic(hat)
    ['🕊️']
    >>> hat = 45
    >>> magic(hat)
    '🕊️'
    >>> hat == _
    False
    """
    dove = '🕊️'
    if hasattr(hat, 'append') and callable(hat.append):
        hat.append(dove)
    elif hasattr(hat, 'add') and callable(hat.add):
        hat.add(dove)
    else:
        hat = dove
    return hat


testmod()
