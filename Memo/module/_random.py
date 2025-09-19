################################
### WARNING 
### RANDOM IS ONLY PSEUDO RANDOM
### FOR SECURITY USE SECRET MODULE : https://docs.python.org/3/library/secrets.html

import random

tiny_list = ['Red', 'Green', 'Blue']
random.seed(42) # set the seed for the random number generator

# since the seed is set, random generator will alwaus generate the same "random"
print(f'{random.random() = !s}')                            # print a float between 0 and 1 inclusive
print(f'{random.uniform(1, 2) = !s}')                       # print a float between a and b inclusive
print(f'{random.randint(1, 2) = !s}')                       # print an integer between a and b inclusive
print(f'{random.choice(tiny_list) = !s}')                   # print an item from the list

print(f'{random.randrange(1, 10, 2) = !s}')                 # print an integer between a (inclusive) and b (exclusive) with step c. Default start value = 0
print(f'{random.randrange(1, 10) = !s}')
print(f'{random.randrange(10) = !s}')

random.shuffle(tiny_list)                 # shuffle the list. Not working in print directly, and only work with mutable objects
print(f'{tiny_list = !s}')
print(f'{random.shuffle(tiny_list) = !s}') # None

print(f'{random.sample(range(10), 2) = !s}') # print a list of 2 random items from the range
print(f'{random.sample(tiny_list, 2) = !s}') # print a list of 2 random items from the list


print(f'{random.gammavariate(1, 1) = !s}') # gamma distribution
print(f'{random.gauss(0, 1) = !s}') # gaussian distribution
print(f'{random.lognormvariate(0, 1) = !s}') # lognormal distribution
print(f'{random.normalvariate(0, 1) = !s}') # normal distribution
print(f'{random.vonmisesvariate(0, 1) = !s}') # von mises distribution
print(f'{random.paretovariate(1) = !s}') # pareto distribution
print(f'{random.weibullvariate(1, 1) = !s}') # weibull distribution

string = ''.join(chr(random.randint(97, 122)) for _ in range(3))
print(f'{string = !s}')