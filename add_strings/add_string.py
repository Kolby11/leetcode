def add_strings(num1: str, num2: str) -> str:
  sum1 = 0
  sum2 = 0
  for i, val in enumerate(num1):
    sum1 += (ord(val)-48) * 10 ** (len(num1) - i-1)
  for i, val in enumerate(num2):
     sum2 += (ord(val)-48) * 10 ** (len(num2) - i-1)

  return str(sum1+sum2)


# 53
print(add_strings("32", "21"))

# 134
print(add_strings("11", "123"))

# 10000000000000000000000000000000000
print(add_strings("1", "9999999999999999999999999999999999"))