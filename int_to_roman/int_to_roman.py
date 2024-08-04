def int_to_roman(num):
    mapping = {1000: "M", 500: "D", 100: "C", 50: "L", 10: "X", 5: "V", 1: "I"}
    roman = []

    for k, v in mapping.items():
        if num / k == 1:
            # If number can fit once
            roman.append(v)
            num -= k

        if num / k > 1:
            if int(str(num)[0]) > 5 and int(str(num)[0]) < 9:
                # 6,7,8 as first num
                roman.append(v)
                num -= k
                for i in range(int(str(num)[0])):
                    roman.append(mapping[k/5])
                    num -= k / 5

            # If number can fit multiple times
            while k <= num:
                # Add the most times it can fit
                roman.append(v)
                num -= k

        if k > num:
            # If number cannot fit
            if str(num)[0] == '9' and not (k - int(str(k)[:-1]) > num):
                # 9 as first num
                roman.append(mapping[k/10])
                roman.append(v)
                num -= int('9' + str(k)[2:])

            elif str(num)[0] == '4' and len(str(int(num))) == len(str(int(k))):
                # 4 as first num
                roman.append(mapping[k / 5])
                num -= (k / 5) * 4
                roman.append(v)

    return ''.join(roman)


print(int_to_roman(65))
