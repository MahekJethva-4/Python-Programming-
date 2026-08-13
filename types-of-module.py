# 1. Import the entire module
import math
print("Using import module:")
print(math.sqrt(25))

# 2. Import a specific function
from math import factorial
print("\nUsing from module import:")
print(factorial(5))

# 3. Import with an alias
import math as m
print("\nUsing import with alias:")
print(m.pi)

# 4. Import multiple functions
from math import pow, floor
print("\nImporting multiple functions:")
print(pow(2, 3))
print(floor(5.8))

# 5. Import everything from a module
from math import *
print("\nUsing import *:")
print(sin(0))