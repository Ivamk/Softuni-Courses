text = input().split()
palindrome = input()

print([el for el in text if el == el[::-1]])
print(f"Found palindrome {text.count(palindrome)} times")
