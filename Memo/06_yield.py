import sys
import time

# FONCTION NORMALE - retourne TOUT d'un coup
def get_all_numbers(n):
    result = []
    for i in range(n):
        result.append(i)
    return result  # Retourne la liste complète

# FONCTION AVEC YIELD - retourne un par un
def get_numbers_yield(n):
    for i in range(n):
        yield i  # Retourne un élément et pause

print("=== COMPARAISON MÉMOIRE ===")

# Test avec 1 million de nombres
n = 1000000

# Fonction normale
numbers_list = get_all_numbers(n)
print(f"Mémoire liste complète: {sys.getsizeof(numbers_list)} bytes")

# Fonction avec yield
numbers_gen = get_numbers_yield(n)
print(f"Mémoire générateur: {sys.getsizeof(numbers_gen)} bytes")

print("\n=== UTILISATION ===")

# Avec la liste - tout est déjà en mémoire
print("Avec liste:")
for num in numbers_list[:5]:  # On prend que les 5 premiers
    print(num)

# Avec le générateur - génère à la demande
print("Avec yield:")
for num in numbers_gen:
    print(num)
    if num >= 4:  # On s'arrête après 5 éléments
        break

print("\n=== MESURE DU TEMPS D'EXÉCUTION ===")

# Exemple avec deux boucles différentes
print("Boucle 1 - Liste normale:")
start_time = time.time()
result1 = []
for i in range(100000):
    result1.append(i * 2)
end_time = time.time()
print(f"Temps d'exécution: {end_time - start_time:.4f} secondes")

print("\nBoucle 2 - Avec yield:")
start_time = time.time()
def double_numbers(n):
    for i in range(n):
        yield i * 2

result2 = list(double_numbers(100000))
end_time = time.time()
print(f"Temps d'exécution: {end_time - start_time:.4f} secondes")

print("\n=== VOTRE EXEMPLE DICT 2GO ===")

# Simulation d'un gros dict
def process_big_dict_normal():
    big_data = {}
    for i in range(100000):  # Simule un gros dict
        big_data[i] = f"valeur_{i}"
    return big_data  # Retourne TOUT (2GO)

def process_big_dict_yield():
    for i in range(100000):  # Simule un gros dict
        yield (i, f"valeur_{i}")  # Retourne UN élément à la fois

# Normal: tout en mémoire
# big_dict = process_big_dict_normal()  # 2GO en mémoire !

# Avec yield: un élément à la fois
for key, value in process_big_dict_yield():
    print(f"{key}: {value}")
    if key >= 2:  # On s'arrête après 3 éléments
        break
