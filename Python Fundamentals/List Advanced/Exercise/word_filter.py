text = input().split()
even_text = [el for el in text if len(el) % 2 == 0]
print(*even_text, sep='\n')

