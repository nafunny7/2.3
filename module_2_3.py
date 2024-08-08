numbers = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
a = 0
while a < len(numbers) and numbers[a] >= 0:
    print(numbers[a])
    a += 1
    if numbers[a] == 0:
        continue
        numbers = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
        a = 0
        while a < len(numbers) and numbers[a] >= 0:
            print(numbers[a])
            a += 1
            if numbers[a] == 0:
                continue
