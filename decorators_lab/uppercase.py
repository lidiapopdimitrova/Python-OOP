def uppercase(function):
    def wrapper():
        result = function()
        uppercase_result = result.upper()
        return uppercase_result

    return wrapper

# def say_hi():
#     return 'hello there'
# decorate = uppercase_decorator(say_hi)
# decorate()


@uppercase
def say_hi():
    return 'hello there'


print(say_hi())
