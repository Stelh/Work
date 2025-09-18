print("=== 1. Seulement *args (arguments dynamiques) ===")
def somme(*args):
    print(f"args: {args}")
    return f"  return sum(args): {sum(args)}"

print(somme(10))
print(somme(1, 2, 3, 4, 5))
print(somme())
print("_________________\n")

print("=== 2. Seulement **kwargs (arguments nommés dynamiques) ===")
def affiche_info(**kwargs):
    print(f"kwargs: {kwargs}")
    for cle, valeur in kwargs.items():
        print(f"  {cle}: {valeur}")

affiche_info(nom="Jean", age=25)
affiche_info(ville="Paris", pays="France", code=75001)
print("_________________\n")

print("=== 3. Les deux ensemble *args + **kwargs ===")
def fonction_complete(*args, **kwargs):
    print(f"args: {args}")
    print(f"kwargs: {kwargs}")

fonction_complete(1, 2, 3, nom="Pierre", age=30)
fonction_complete("hello", "world", x=1, y=2, z=3)
print("_________________\n")

print("=== 4. Paramètres fixes + dynamiques ===")
def calcul(operation, *args):
    print(f"Opération: {operation}, Nombres: {args}")
    
    if operation == "add":
        return sum(args)
    elif operation == "multiply":
        result = 1
        for num in args:
            result *= num
        return result
    else:
        return "Opération non reconnue"

print(calcul("add", 1, 2, 3, 4))
print(calcul("multiply", 2, 3, 4))
print(calcul("divide", 10, 2))
print("_________________\n")
print("_________________\n")
print("_________________\n")

##########################################################
##########################################################
print("=== 5. Exemple pratique : calculatrice simple ===")
def calculatrice(operation="add", *args, **options):
    if not args:
        return "Aucun nombre fourni"
    
    result = 0
    if operation == "add":
        result = sum(args)
    elif operation == "multiply":
        result = 1
        for num in args:
            result *= num
    
    # Options supplémentaires via **kwargs
    if options.get("afficher_detaille"):
        print(f"Calcul: {' + '.join(map(str, args))} = {result}")
    
    if options.get("arrondir"):
        result = round(result, options["arrondir"])
    
    return result

print(calculatrice("add", 1, 2, 3, 4, afficher_detaille=True))
print(calculatrice("multiply", 1.1, 2.2, 3.3, arrondir=2))

print("\n=== 6. Exemple avec votre fonction test modifiée ===")

def test_simple(*args):
    """Version simple avec seulement *args"""
    if not args:
        return "Aucun nombre fourni"
    
    total = sum(args)
    return f"La somme de {args} = {total}"

def test_avance(*args, **kwargs):
    """Version avancée avec *args et **kwargs"""
    if not args:
        return "Aucun nombre fourni"
    
    # Calcul de base
    total = sum(args)
    
    # Options via kwargs
    if kwargs.get("start"):
        total += kwargs["start"]
    
    if kwargs.get("multiply"):
        total *= kwargs["multiply"]
    
    return f"Résultat: {total}"

# Tests
print(test_simple(1, 2, 3, 4))
print(test_simple(10, 20, 30))
print(test_simple())  # Cas vide

print(test_avance(1, 2, 3, start=10))        # (1+2+3) + 10 = 16
print(test_avance(2, 3, multiply=5))         # (2+3) * 5 = 25
print(test_avance(1, 2, 3, start=5, multiply=2))  # ((1+2+3) + 5) * 2 = 22

print("\n=== FIN DES EXEMPLES ===")
