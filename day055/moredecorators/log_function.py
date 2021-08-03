'''A decorator that logs the used function'''

def log_decorator(func):
    def wrapper(*args):
        print(f'You called {func.__name__}{args}')
        print(f'it returned {func(*args)}')
    return wrapper


@log_decorator
def a_function(a, b, c):
    return a * b * c
    
a_function(1, 2, 3)
