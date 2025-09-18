### ARITHMETIC FUNCTIONS ###
############################

abs_integer = abs(-10) # 10
print(f"{abs_integer = !s}")
abs_float = abs(-10.0) # 10.0
print(f"{abs_float = !s}")

round_integer = round(10.0) # 10
print(f"{round_integer = !s}")
round_float = round(10.2573, 2) # 10.26
print(f"{round_float = !s}")

pow_integer = pow(2, 10) # 1024
print(f"{pow_integer = !s}")
pow_float = pow(2.0, 10) # 1024.0
print(f"{pow_float = !s}")

smallest = min(1, 2, 3, 4, 5) # 1
print(f"{smallest = !s}")
largest = max(1, 2, 3, 4, 5) # 5
print(f"{largest = !s}")
print("_________________\n")

### MATH FUNCTIONS ###
######################

### abs() and pow() functions have equivalents in the math module. 
### The key difference of math.fabs() and math.pow() is that they always return floats:
import math
x = 2
y = 10

fabs_integer = math.fabs(-10) # 10.0
print(f"{fabs_integer = !s}")
fabs_float = math.fabs(-10.0) # 10.0
print(f"{fabs_float = !s}")

pow_integer = math.pow(x, y) # 1024.0
print(f"{pow_integer = !s}")
pow_float = math.pow(x, y) # 1024.0
print(f"{pow_float = !s}")

### Suppose you raised x to the power y, and then forgot y, you can recover it using the math.log() function:
log = math.log(pow_float, x) # 10.0 != log(1024)
print(f"{log = !s}")
natural_log = math.log(1024) # 6.93147
print(f"{natural_log = !s}")

floor = math.floor(6.931471805599453)  # 6 / returns the nearest integer less than or equal to a
print(f"{floor = !s}")
ceil = math.ceil(6.391471805599453)    # 7 / returns the nearest integer greater than or equal to a
print(f"{ceil = !s}")

result = math.sqrt(100) # 10.0 / return the square root (10*10 = 100)
print(f"{result = !s}")
print("_________________\n")

### TRIGONOMETRIC FUNCTIONS ###
###############################

pi = math.pi
print(f"{pi = !s}")

deg = 60.0
radians = math.radians(deg)  # 1.047... returns angle converted from degrees to radians
print(f"{radians = !s}")
degrees = math.degrees(radians)  # 59.99.. return angle converted from radians to degrees
print(f"{degrees = !s}")
cos = math.cos(radians)  # 0.500... returns the cosine of a radians
print(f"{cos = !s}")
sin = math.sin(radians)  # 0.866... returns the sine of a radians
print(f"{sin = !s}")

euler = math.e  # 2.718281828459045
print(f"{euler = !s}")