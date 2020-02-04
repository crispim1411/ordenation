from counter import Counter


def bubble(a: list):
    length = len(a)
    count = 0
    for i in range(0, length):
        for j in range(0, length):
            if a[i] < a[j]:
                print(a)
                print(f'swap({a[i]},{a[j]})')
                a[j], a[i] = a[i], a[j]
                Counter.plus()


def bubble2(a: list):
    length = len(a)
    count = 0
    for i in range(0, length):
        for j in range(i, length):
            if a[i] > a[j]:
                print(a)
                print(f'swap({a[i]},{a[j]})')
                a[j], a[i] = a[i], a[j]
                Counter.plus()


def straight(a: list):
    length = len(a)
    count = 0
    for i in range(0, length):
        p = i
        for j in range(i+1, length):
            if a[j] < a[p]:
                p = j
        if p != i:
            print(a)
            print(f'swap({a[p]},{a[i]})')
            a[i], a[p] = a[p], a[i]
            Counter.plus()


def insertion(a: list):
    lenght = len(a)
    count = 0
    for i in range(1, lenght):
        aux = a[i]
        p = i
        print(a)
        print(f'insertion({aux})')
        while p >= 1 and aux < a[p-1]:
            a[p] = a[p-1]
            print(a)
            p -= 1
        a[p] = aux
        Counter.plus()


def shell(a: list):
    length = len(a)
    inc = length//2
    count = 0
    while inc:
        current = inc
        while current < length:
            aux = a[current]
            i = current - inc
            print(a)
            print(f'aux:{aux} i:{i}')
            while i >= 0 and aux < a[i]:
                a[i+inc] = a[i]
                print(a)
                i -= inc
            a[i+inc] = aux
            Counter.plus()
            current += 1
        inc //= 2


def quicksort(a: list):
    _quicksort(a, 0, len(a) - 1)


def _quicksort(a: list, left, right):
    if right > left:
        pivot = partition(a, left, right)
        _quicksort(a, left, pivot - 1)
        _quicksort(a, pivot + 1, right)


def partition(a: list, left, right):
    pivot = a[right]
    p_left = left
    p_right = right - 1
    done = False

    while not done:
        while a[p_left] < pivot:
            p_left += 1
        while a[p_right] > pivot:
            print(f"{a[p_right]}>{pivot}")
            p_right -= 1
        if p_left > p_right:
            done = True
        else:
            print(f"troca {a[p_left]} com {a[p_right]}")
            print(a)
            Counter.plus()
            a[p_left], a[p_right] = a[p_right], a[p_left]
            p_left += 1
            p_right -= 1
            if p_left > p_right:
                done = True
    print(f"fim troca {a[p_left]} com {a[right]}")
    print(a)
    Counter.plus()
    a[p_left], a[right] = a[right], a[p_left]
    return p_left
