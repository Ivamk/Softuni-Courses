text = input()
vowels = ['a', 'o', 'e', 'i', 'u']
print(''.join([el for el in text if el.lower() not in vowels]))
