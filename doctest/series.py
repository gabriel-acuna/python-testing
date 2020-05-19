def fibonacci(num):
    if num == 0: return 0
    elif num ==1: return 1
    else: return fibonacci(num -1) + fibonacci(num -2)

def palindromo(sentence):
    ''' @param sentence String | Integer
        @return boolean
    >>> palindromo('anita lava la tina')
    True
    
    >>> palindromo(12321)
    True

    >>> palindromo('Gabriel')
    False
    '''
    sentence = str(sentence).lower().replace(' ', '')
    return sentence == sentence[::-1]


if __name__ ==  '__main__':
    import doctest
    doctest.testmod()
    doctest.testfile("test2.txt")

