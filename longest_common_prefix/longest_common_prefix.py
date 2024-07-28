def longest_common_prefix(strs: list[str]) -> str:
  prefix = strs[0]
  for word in strs:
    a = prefix[:len(word)]
    for i in range(len(a)):
      if a == word[:len(a)]:
        break
      a = a[:-1]
    prefix = a
  

  return prefix

print(longest_common_prefix(["flower","flow","flight"]))
print(longest_common_prefix(["dog","racecar","car"]))