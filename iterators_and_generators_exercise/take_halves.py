def solution():
    def integers():
        i = 1
        while True:
            yield i
            i += 1
        # TODO: Implement

    def halves():
        for i in integers():
            yield i / 2
        # TODO: Implement

    def take(n, seq):
        taken_list = []
        for el in range(n):
            taken_list.append(next(seq))
        return taken_list

        # TODO: Implement
    return (take, halves, integers)


take = solution()[0]

halves = solution()[1]

print(take(5, halves()))