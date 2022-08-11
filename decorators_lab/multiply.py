def multiply(times):
    def decorator(function):
        def wrapper(params):
            return times * function(params)
        return wrapper

    return decorator


@multiply(5)
def add_ten(number):
    return number + 10


print(add_ten(3))
