print("_________________\n")
raw_string = r'Hellow \n World' # raw string does not execute special characters
fstring = f'Hellow \n World' # fstring execute special characters
uniicode = '\u12FF'
nb = 1.01548616478
emoji = "💔"
string = "Little emoji"

print(f"0: {nb:.2f}")
print(f"0: {1.01548616478:.2f}")
print(f"0: {string}{emoji}")
print(f'0: Unicode = {uniicode}') # Unicode = ዿ
print(f'1: Alias = \N{LATIN CAPITAL LETTER GHA}') # Alias = Ƣ
print(f'2: !s: {uniicode = !s}') #  Ƣ   => !s string representation, execute special character
print(f'3: !r: {uniicode = !r}') # 'ዿ' => !r raw representation, does not execute special character
print("_________________\n")

print(f'4: {raw_string}') # Hellow \n World
print(f'5: {fstring}')
print(f'6: !s: {raw_string = !s}') # => YEP
print(f'7: !r: {raw_string = !r}') # => NOP
print("_________________\n")

print("8: A,\bB") # Backspace
print("9: A\tB") # Tabulation
print("10: A\rB ab") # Supprime tout ce qui à avant le \r
print("11: A\N{DEGREE SIGN}B") # UNICODE Alias
print("_________________\n")

string = "paSSwOrd"
print(string)
print(f"12: capitalize: {string.capitalize()}")
print(f"13: casefold: {string.casefold()}")
print(f"14: lower: {string.lower()}")
print(f"15: swapcase: {string.swapcase()}")
print(f"16: title: {string.title()}")
print(f"17: upper: {string.upper()}")
print("_________________\n")

print(f"18: isalnum: {string.isalnum()}")
print(f"19: isalpha: {string.isalpha()}")
print(f"20: isascii: {string.isascii()}")
print(f"20: isdecimal: {string.isdecimal()}")
print(f"21: isdigit: {string.isdigit()}")
print(f"22: isidentifier: {string.isidentifier()}")
print(f"23: islower: {string.islower()}")
print("_________________\n")

string = " s p a c e s "
print(f"24: {string}")
print(f"25: {string.strip()}")
print(f"26: {string.lstrip()}")
print(f"27: {string.rstrip()}")
print(f"28: {string.lstrip(' sp')}")
print(f"29: {string.rstrip(' es')}")
print("_________________\n")

string = "One. Two. Three."
print(f'30: {string}')
print(f'31: {string.split()} len: {len(string.split())}')
print(f'32: {string.split(".")} len: {len(string.split("."))}')
print(f'33: {string.split(".,")} len: {len(string.split(".,"))}')
print("_________________\n")

import random
random.seed(42)
string = ''.join(chr(random.randint(97, 122)) for _ in range(3))
print(f'34: {string}') # uda
print("_________________\n")

str1 = "Hello, world"
str2 = "Hello, world"
str3 = "12345, 12345"
string = "Hi"
print(f"35: str1 != str2: {str1 != str2}")
print(f"36: str1 > str2: {str1 > str2}")
print(f"37: str1 == str3: {str1 == str3}")
print(f"38: str1 >= str3: {str1 >= str3}")
print(f"39: 'some' in 'something': {'some' in 'something'}")
print("_________________\n")

objs = ['1', None, 0b10101, str, 'Hello, world']
for obj in objs:
    print(f'40: The type of {obj!r} is {type(obj)}')
print("_________________")

for i in range(len(string)):
    if ' ' in string[i]:
        print(f'41: Space found at index {i}')
    else:
        print(f'41: The character at index {i} is {string[i]}')
print("_________________")

for char in string:
    print(f"42: Looking at character: {char}")
print("_________________\n")

print("slicing [A:B:C] : [Starting Index (inclusive):End Index (excluding):Step]")
print("_________________")
string = '0123456789' 
print("::2",string[::2])
print("::-1",string[::-1]) # Only way for reverse a string or :
print(ord("A")) # 65: Unicode code point
print(chr(65))  #   A: Unicode character. Note that the valid range for the "chr" function is from 0 through 1_114_111.
print("_________________\n")

from datetime import datetime
current_time = datetime.now()
print(f"current_time: {current_time}")
print(f"{current_time:%d-%m-%Y %H:%M:%S}") # 24 hours format
print(f"Current time is: {current_time:%Y-%m-%d %I:%M %p}") # 12 hours format
print("_________________\n")

print('Gadget','Hawk', sep=',', end='!\n') # \n or no new line
list_ = ['Gadget','Hawk']
print(list_)
print(*list_,sep=',') #f format does not work with unpacking
word = 'ward'
print(*word, sep=' ' * 3) # unpacking


# def test(*args, **kwargs) -> str:
#     """This is a test function
#     :param args: number
#     :param kwargs: som magic
#     :return: result in string
#     """
#     print(f"args = {args}")
#     print(f"kwargs = {kwargs}")
#     print(f"result = {sum(*args, **kwargs)}")
#     return f"The result is: {sum(*args, **kwargs)}"

# print(test(range(10), start=-1))
# help(test)

# class Test:
#     """
#     This is a test class
#     """
# help(Test)
# print("_________________\n")

# class Entity:
#     def __init__(self, name, age, skillset=None):
#         self.name = name
#         self.age = age
#         self.skillset = skillset
    
#     def __str__(self):
#         return f"My name is {self.name}. I'm {self.age} years old. My skillset is {", ".join(self.skillset)}."
    
#     def __repr__(self):
#         return f"Entity(name={self.name}, age={self.age}, skillset={self.skillset})"

# entity = Entity("John", 25, ["Python", "Java", "C++"])
# print(entity) # My name is John. I'm 25 years old. My skillset is Python, Java, C++.
# print(repr(entity)) # Entity(name=John, age=25, skillset=['Python', 'Java', 'C++'])
# print("_________________\n")