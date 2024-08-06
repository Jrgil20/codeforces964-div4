
cases = int(input())

if 1 <= cases <= 90:
    for _ in range(cases):
        s = int(input())
        if 10 <= s <= 99:
            a = s // 10
            b = s % 10
            print(a + b)