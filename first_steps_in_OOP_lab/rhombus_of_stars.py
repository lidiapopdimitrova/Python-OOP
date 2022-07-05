
def get_line(i, n):
    spaces_count = n - i - 1
    stars_count = i + 1
    return ' ' * spaces_count + ('* ' * stars_count)


def print_rhombus(n):
    for i in range(0, n, 1):
        print(get_line(i, n))

    for i in range(n - 2, - 1, -1):
        print(get_line(i, n))


print_rhombus(3)