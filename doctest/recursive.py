'''
>>> recursive = Recursive()
>>> recursive.factorial(0)
1

>>> recursive.factorial(6)
720
'''
class Recursive:
    def factorial(self, number):
        if number == 0: return 1
        else: return number * self.factorial(number-1)


if __name__ == '__main__':
    import doctest
    doctest.testmod()