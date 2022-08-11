def vowel_filter(function):
    def wrapper():
        letters = function()
        return [letter for letter in letters if letter.lower() in "aeuoi"]
    return wrapper


@vowel_filter
def get_letters():
    return ["a", "b", "c", "d", "e"]


@vowel_filter
def get_other_letters():
    return ['a', 'k', 'l', 'o']


print(get_other_letters())

