import sys
import time
#############################################
### Test yield vs range ###

def count_up_to(n):
    i = 1
    while i <= n:
        yield i
        i += 1

def count_up_to_range(n):
    for i in range(n):
        print(i)

def start_up_to(n):
    for i in count_up_to(n):
        print(i)

n = 100
memory_usage1 = sys.getsizeof(start_up_to(n))
start_time1 = time.time()
start_up_to(n)
end_time1 = time.time() - start_time1

start_time2 = time.time()
memory_usage2 = sys.getsizeof(count_up_to_range(n))
count_up_to_range(n)
end_time2 = time.time() - start_time2

print(f"Temps d'exécution start_up_to: {end_time1:.6f} secondes")
print(f"Mémoire utilisée start_up_to: {memory_usage1} bytes")
print(f"Temps d'exécution count_up_to_range: {end_time2:.6f} secondes")
print(f"Mémoire utilisée count_up_to_range: {memory_usage2} bytes")

############################################
### Test list vs for in ###

def test_range():
    start_time1 = time.time()
    n1 = list(range(1000))
    print(n1)
    print("test_range:_________________")
    return time.time() - start_time1

def test_for_in():
    start_time2 = time.time()
    n2 = [_ for _ in range(1000)]
    print("test_for_in:_________________")
    return time.time() - start_time2

time1 = test_range()
time2 = test_for_in()

print(f"test_range: {time1:.6f} secondes")
print(f"test_for_in: {time2:.6f} secondes")

print(f"""Print log:_________________
{'n1' if time1 < time2 else 'n2'} plus rapide de {(abs(time2 - time1) if time1 < time2 else abs(time1 - time2)):.6f} secondes
""")

#############################################

for i in range (10):
    print(i)
for i in range(10,-1,-1):
    print(i)

#############################################

names = ['Alice', 'Bob', 'Charlie', 'David', 'Eve']
ages = [25, 30, 35, 40, 45]
for name, age in zip(names, ages):
    print(f"{name} is {age} years old")
    print("_________________")
for i in range(len(names)):
    print(f"{names[i]} is {ages[i]} years old")
print("_________________")

squares = {i: i*i for i in range(10)}
print(squares)

list = ["a","b","c"]
for i in range(len(list)-1,-1,-1):
    print(list[i])