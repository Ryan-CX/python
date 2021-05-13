from functools import cache


@cache
def factorial(n):
    print (n * factorial(n-1))
factorial(5)