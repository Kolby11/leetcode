def shuffle_string(s: str, indices: list[int]) -> str:
    positions = {}
    result = ""
    for i in range(len(s)):
        positions[indices[i]] = s[i]

    for i in range(len(positions)):
        result += positions[i]

    return result


# leetcode
print(shuffle_string("codeleet", [4, 5, 6, 7, 0, 2, 1, 3]))

# abc
print(shuffle_string("abc", [0, 1, 2]))
