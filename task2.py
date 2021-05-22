def task1(x):
    if x == 1:
        return 1

    else:
        return x * task1(x - 1)


def task2(a):
    if a == 0:
        return 0
    if a % 2 == 0:
        return task2(a - 1)

    else:
        return a + task2(a - 1)


def task3(c):
    if c % 3 != 0:
        return task3(c - 1)
    else:
        return c + task3(c - 1)


def task4(d):
    if d == 0:
        return 0
    return 2 * d + 3 + task4(d - 1);


def task5(e):
    if e == 0:
        return 0
    if e == 1:
        return 1
    return 3 * task5(e - 1) - task5(e - 2)
