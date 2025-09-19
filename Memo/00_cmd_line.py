### SCRIPT AVEC NB DETERMINÉ D'ARGUMENTS
import sys

# args = sys.argv # liste des arguments passés au script

# if len(args) != 3:
#     print("The script should be called with two arguments, the first and the second number to be multiplied")
# else:
#     first_num = float(args[1]) # args[1] est le premier argument passé au script
#     second_num = float(args[2])
#     product = first_num * second_num
#     print(f"{args = !s}")
#     print("The product of " + args[1] + " times " + args[2] + " equals " + str(product))

##########################################################
##########################################################
##########################################################

### SCRIPT AVEC ARGUMENT POSITIONNEL / OPTIONNEL
import argparse

# add_argument(action=""):
#   "store"       / "store_const"
#   "store_true"  / "store_false"   (store_ture = passe à True si l'argument est présent, store_false = passe à False si l'argument est présent)
#   "append"      / "append_const"
#   "count"
#   "help"      (génère l’aide)
#   "version"   (affiche la version et quitte)

parser = argparse.ArgumentParser(description="This is a description for help") # création d'un parser avec description pour help

# parser.add_argument("name")                                 # positionnel (obligatoire)
# parser.add_argument("-s","--surname", metavar="Prenom")     # optionnel, metavar affiche "Prenom" dans help au lieu de "SURNAME"
# parser.add_argument("-a","--age", default="31")             # optionnel avec valeur par défaut
# parser.add_argument("-c","--celib", action="store_false")   # optionnel, action="store_true" signifie que l'argument est un booléen et que la valeur par défaut est False
# parser.add_argument("-m","--married", default=False)        # comme action="store_false", mais avec default MAIS a besoin d'être changé manuellement => --married False/True lors de l'appel
# parser.add_argument("-j","--job", default="None",
#                     choices=["developer", "designer", "manager"],
#                     help="Choose one job")
# args = parser.parse_args()                              # parsing des arguments
# print(f"{args = !s}")
# print(f"{args.job = !s}") # cant use short name (-j not working)
# multiple_print = [args.name, args.job]
# print(f"{multiple_print = !s}")


############################################
### EXEMPLE PRATIQUE : DECODE CAESAR CIPHER
############################################
### input: --word fur!y,px --offset 13
### output: Sherlock

parser.add_argument("--word")
parser.add_argument("--offset", type=int)
args = parser.parse_args()
args.offset = -abs(args.offset)

def decode_caesar_cipher(s, n):
    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz',.?!"
    s = s.strip()
    text = ''
    for c in s:
        text += alpha[(alpha.index(c) + n) % len(alpha)]
    print(text)

decode_caesar_cipher(args.word, args.offset)

#############################################
#############################################
#############################################