some_iterable = input().split()

# créer un dictionnaire. key: some_iterable[i].upper() | value: some_iterable[i].lower()
dictionary = {word.upper(): word.lower() for word in some_iterable}
print(dictionary)