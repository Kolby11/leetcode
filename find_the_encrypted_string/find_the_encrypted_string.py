import math


def find_the_encrypted_string(s: str, k: int) -> str:
    result = ""
    for i in range(len(s)):
        if i+k >= len(s):
            result += s[(i+k) % len(s)]
        else:
            result += s[i+k]

    return result


# tdar
print(find_the_encrypted_string("dart", 3))

# aaa
print(find_the_encrypted_string("aaa", 3))

# ydb
print(find_the_encrypted_string("byd", 4))
