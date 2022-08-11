def repeat(n):
    def decorator(function):
        def wrapper():
            for _ in range(n):
                function()
        return wrapper
    return decorator


@repeat(4)
def say_hi():
    print("Hello")


say_hi()