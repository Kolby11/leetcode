def add_digits(num: int) -> int:
    if len(str(num)) == 1:
        return num
    else:
        return add_digits(sum([int(x) for x in str(num)]))


# 2
print(add_digits(38))
