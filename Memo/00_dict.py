my_pets = {
    'dog': {'name': 'Dolly', 'breed': 'collie'},
    'cat': {'name': 'Fluffy', 'breed': 'maine coon'}
    }
my_pets_copy = {key: value for key, value in my_pets.items()} # copy new dict

# correct but long way
my_pet_copy_2 = {}
for key, value in my_pets.items():
    my_pet_copy_2[key] = value

# or more convenient and short!
my_pet_copy_3 = {(key+'s' if key == 'dog' else key): value for (key, value) in my_pets.items()}
test_dict = {key + 5: 'some value' for key in range(3)} # {5: 'some value', 6: 'some value', 7: 'some value'}
test_dict = {n + 10: n + 100 for n in range(3)}         # {10: 100, 11: 101, 12: 102}

##########################################################

my_pets = {
    'dog': {'name': 'Dolly', 'breed': 'collie'},
    'cat': {'name': 'Fluffy', 'breed': 'maine coon'}
    }

print(f"_____\n1: {my_pets = !s}")          # my_pets = {'dog': {'name': 'Dolly', 'breed': 'collie'}, 'cat': {'name': 'Fluffy', 'breed': 'maine coon'}}
print(f"1: {my_pets['cat'] = !s}")          # {'name': 'Fluffy', 'breed': 'maine coon'}
print(f"1: {my_pets['cat']['breed'] = !s}") # maine coon
print('1: ','dog' in my_pets)               # True. Only work with key
print("_________________\n")

tiny_dict   = {'a': 1, 'b': 2, 'c': 3}
tiny_dict_2 = {'d': 1, 'e': 2, 'f': 3}
tiny_dict_3 = {'d': 10, 'g': 20, 'h': 4}    # d in common
tiny_dict_4 = {'d': 10, 'g': 20, 'k': 4}    # d and g in common

for obj in tiny_dict:
    print(f"2: {obj = !s}")                                 # a b c
print(f"2: {tiny_dict.keys() = !s}")                        # dict_keys(['a', 'b', 'c'])
print(f"2: {tiny_dict.keys() & tiny_dict_2.keys() = !s}")   # set()
print(f"2: {tiny_dict_2.keys() & tiny_dict_3.keys() = !s}") # d
print(f"2: {tiny_dict_3.keys() & tiny_dict_4.keys() = !s}") # d g
print("_________________\n")

for obj in tiny_dict.keys():
    print(f"3 key: {obj}")      # a b c
print("_________________")
for obj in tiny_dict.values():
    print(f"3 value: {obj}")    # 1 2 3
print("_________________")
for obj in tiny_dict.items():
    print(f"3 items: {obj}")    # ('a', 1) ('b', 2) ('c', 3)
print("_________________")
for key, value in tiny_dict.items():
    print(f"3: {key = !s} : {value = !s}") # a: 1 b: 2 c: 3
print("_________________\n")

my_pet = {}
my_pet['name'] = 'Dolly'
my_pet['animal'] = 'dog'
my_pet['breed'] = 'collie'
print(f"4: {my_pet = !s}")           # {'name': 'Dolly', 'animal': 'dog', 'breed': 'collie'}
print(f"4: {my_pet['name'] = !s}")   # Dolly
print("_________________\n")

my_pet = dict(a=1, b=2, c=3)
print(f"5: {my_pet = !s}")
my_pet = dict(zip(['a', 'b', 'c'], [1, 2, 3]))
print(f"5: {my_pet = !s}")
my_pet = dict([('a', 1), ('b', 2), ('c', 3)])
print(f"5: {my_pet = !s}")
my_pet = dict({'a': 1, 'b': 2, 'c': 3}) # Avec un autre dictionnaire
print(f"5: {my_pet = !s}")
my_pet = dict({'a': 1}, b=2, c=3) # Dictionnaire + arguments nommés
print(f"5: {my_pet = !s}")

##########################################
### need review syntax
my_pet = dict((i, i*2) for i in range(3)) # Avec un générateur
print(f"5: {my_pet = !s}")
print("_________________\n")

##########################################################

planets = {'Venus', 'Earth', 'Jupiter'}
value = "planet"
planets_dict = dict.fromkeys(planets)
print(f"6: {planets_dict = !s}")
planets_dict = dict.fromkeys(planets, value)
print(f"6: {planets_dict = !s}")
planets_dict["Jupiter"] = "giant " + planets_dict["Jupiter"]
print(f"6: {planets_dict = !s}")
print("_________________\n")

satellites = ["Moon", "Phobos", "Deimos"]
planets_dict = dict.fromkeys(planets, [])
print(f"7: {planets_dict = !s}")
planets_dict['Earth'].append(satellites[0])
print(f"7: {planets_dict = !s}")
planets_dict['Jupiter'].append(satellites[1])
print(f"7: {planets_dict = !s}")
planets_dict['Jupiter'].append(satellites[2])
print(f"7: {planets_dict = !s}")
print("_________________\n")

testable = {'September': '16°C', "October": '12°C'} 
another_dictionary = {'November': '8°C'}
print(f"8: {testable = !s}")
testable.update(another_dictionary)
print(f"8: {testable = !s}")
testable.update(December = '10°C')
print(f"8: {testable = !s}")
testable.update(December = "20°C")
print(f"8: {testable = !s}")
print("_________________\n")

dict1 = {'a': 1, 'b': 2}
dict2 = {'a': 3, 'c': 4}
merged_dict = dict1 | dict2
print(f"9: {merged_dict = !s}")
print("_________________\n")

##########################################################
### Sorting a dictionary

import operator

catalog = {'green table': 5000, 'brown chair': 1500, 'blue sofa': 15000, 'wardrobe': 10000}
print(f"10: {catalog = !s}")
catalog_sorted_by_key = dict(sorted(catalog.items(), key=operator.itemgetter(0)))
print(f"10: {catalog_sorted_by_key = !s}")
catalog_sorted_by_value = dict(sorted(catalog.items(), key=operator.itemgetter(1)))
print(f"10: {catalog_sorted_by_value = !s}")
catalog_sorted_by_value_reverse = dict(sorted(catalog.items(), key=operator.itemgetter(1), reverse=True))
print(f"10: {catalog_sorted_by_value_reverse = !s}")
