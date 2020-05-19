def fibonacci(num):
    if num == 0: return 0
    elif num ==1: return 1
    else: return fibonacci(num -1) + fibonacci(num -2)

def palindrome(sentence):
    sentence = str(sentence).lower().replace(' ', '')
    return sentence == sentence[::-1]

def factorial(number):
    if number == 0: return 1
    else: return number * factorial(number-1)