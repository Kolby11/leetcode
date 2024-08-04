def rotate_string(s: str, goal: str) -> str:
    for c in range(len(s)):
        s = s[1:] + s[0]
        if s == goal:
            return True
    return False


# true
print(rotate_string("abcde", "cdeab"))

# false
print(rotate_string("abcde", "abced"))
