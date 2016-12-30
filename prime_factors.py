

"""
Provides factors and prime numbers
"""

from itertools import combinations


class PrimeNumbers(object):
    """
    To initialize it with an number pass an integer as argument or not
    """
    number = None

    def __init__(self, number):
        self.number = number

    def prime_factors(self, number=None):
        """
        Returns Array of Prime Factors of the number
        """
        arr = []
        if number is None:
            number = self.number
        while True:
            leastprime = self.least_prime_factor(number)
            if leastprime == number:
                arr.append(leastprime)
                break
            arr.append(leastprime)
            number = number / leastprime
        arr.sort()
        return arr

    def least_prime_factor(self, number=None):
        """
        Returns the least prime factor of the number
        """
        if number is None:
            number = self.number
        for i in xrange(2, int(number**0.5) + 1):
            if number % i == 0:
                return i
        return number

    def is_prime(self, number=None):
        """
        Checks if number is prime
        """
        if number is None:
            number = self.number
        for i in xrange(2, int(number**0.5) + 1):
            if number % i == 0:
                return False
        return True

    def common_primes(self, number_to_compare, number_to_compare_with=None):
        """
        Returns an array of common primes
        """
        if number_to_compare_with is None:
            number_to_compare_with = self.number
        arr1 = self.prime_factors(number_to_compare)
        arr2 = self.prime_factors(number_to_compare_with)
        return list(set(arr1).intersection(arr2))

    def highest_prime_factor(self, number=None):
        """
        Returns the highest Prime factor
        """
        if number is None:
            number = self.number
        arr = self.prime_factors(number)
        return arr[-1]

    def product(self, array):
        """
        Returns the product of all elements in an array
        """
        product = 1
        for elem in array:
            product *= elem
        return product

    def all_factors(self, number=None):
        """
        Returns the list of all factors
        """
        if number is None:
            number = self.number
        arr = self.prime_factors(number)
        elem = [1]
        for length in xrange(1, len(arr)):
            for subset in combinations(arr, length):
                elem.append(self.product(list(subset)))
        elem.append(number)
        elem.sort()
        return list(set(elem))

