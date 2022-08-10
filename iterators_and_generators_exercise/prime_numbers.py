def is_prime(n):
    if n <= 1:
        return False
    result = True
    for i in range(2, n):
        if n % i == 0:
            result = False
            break
    return result


def get_primes(numbers):
    for n in numbers:
        if is_prime(n):
            yield n


print(list(get_primes([2, 4, 3, 5, 6, 9, 1, 0])))