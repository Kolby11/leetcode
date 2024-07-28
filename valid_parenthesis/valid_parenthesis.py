def valid_parenthesis(s: str) -> bool:
  pairs = {"]": "[", ")": "(", "}": "{"}
  stack = []
  for char in s:
    if char in pairs and stack and stack[-1] == pairs[char]:
      stack.pop()
      continue
    stack.append(char)

  if len(stack) == 0:
    return True
  return False


# False
print(valid_parenthesis("()[]{([])}[(}]"))
# True
print(valid_parenthesis("()[]{([])}[()]"))