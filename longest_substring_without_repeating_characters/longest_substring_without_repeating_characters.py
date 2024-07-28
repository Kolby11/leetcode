def longest_substring_without_repeating_characters(s: str) -> int:
  longest_substr = ""
  substr = ""
  for i in range(len(s)):
    while s[i] not in substr:
      substr += s[i]
    if len(longest_substr) < len(substr):
      longest_substr = substr
    substr = ""

  return len(longest_substr)

# 3
print(longest_substring_without_repeating_characters("abcabcbb"))

# 3
print(longest_substring_without_repeating_characters("pwwkew"))