def decode_string(s: str) -> str:
    pass


# aaabcbc
print(decode_string("3[a]2[bc]"))

# accaccacc
print(decode_string("3[a2[c]]"))

# abcabccdcdcdef
print(decode_string("2[abc]3[cd]ef"))
