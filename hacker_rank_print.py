if __name__ == '__main__':
    n = int(input())

    i = 1

    a = [0] * 150

    while i <= n:
        a[i - 1] = i
        i += 1

    i = 1

    while i <= n:
        print(a[i - 1], end='')
        i += 1
