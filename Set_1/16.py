fruits_name = input()
if fruits_name.casefold().startswith(('a', 'e', 'i', 'o', 'u','A','E','I','O','U')):
    print(f"This is an {fruits_name}")
else:
    print(f"This is a {fruits_name}")
