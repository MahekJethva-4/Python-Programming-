#Tuple
# A tuple is an immutable, ordered collection of elements

# Creating a tuple
Cars = ("BMW", "Audi", "Swift", "Kia")
print("Original Tuple:", Cars)

# Even Numbers
Even = (2, 4, 6, 8, 10, 12, 14, 16, 20, 22, 24)
print("Even Numbers:", Even)

# Odd Numbers
Odd = (1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23)
print("Odd Numbers:", Odd)

# Creating a tuple with single element (need trailing comma)
Single = (5,)
print("\nSingle Element Tuple:", Single)
print("Type:", type(Single))

# Tuple without parentheses (tuple packing)
Packed = 10, 20, 30
print("\nTuple Packing:", Packed)

# Accessing tuple elements using indexing
print("\n--- Indexing ---")
print("First Element of Cars:", Cars[0])
print("Last Element of Cars:", Cars[-1])
print("Second Element of Cars:", Cars[1])

# Slicing a tuple
print("\n--- Slicing ---")
print("First Two Cars:", Cars[:2])
print("Last Two Cars:", Cars[2:])
print("Middle Elements:", Cars[1:3])
print("Reverse Tuple:", Cars[::-1])

# Tuple immutability (cannot change elements)
print("\n--- Immutability ---")
try:
    Cars[0] = "Mercedes"
except TypeError as e:
    print("Cannot modify tuple:", e)

# Tuple concatenation
print("\n--- Concatenation ---")
Combined = Even + Odd
print("Even + Odd:", Combined)

# Tuple repetition
print("\n--- Repetition ---")
Repeated = ("Hello",) * 3
print("Repeated Tuple:", Repeated)

# Membership test
print("\n--- Membership ---")
print("Is 'Audi' in Cars?", "Audi" in Cars)
print("Is 'Honda' in Cars?", "Honda" in Cars)

# Tuple methods - count()
print("\n--- Tuple Methods ---")
Numbers = (1, 2, 3, 2, 4, 2, 5, 2)
print("Tuple:", Numbers)
print("Count of 2:", Numbers.count(2))
print("Count of 3:", Numbers.count(3))

# Tuple methods - index()
print("\nIndex of 4:", Numbers.index(4))
print("Index of first 2:", Numbers.index(2))

# Finding index with start and end range
print("Index of 2 between index 2 and 5:", Numbers.index(2, 2, 5))

# Length of tuple
print("\n--- Length ---")
print("Length of Cars tuple:", len(Cars))
print("Length of Numbers tuple:", len(Numbers))

# Looping through a tuple
print("\n--- Looping Through Tuple ---")
print("All Cars:")
for car in Cars:
    print("-", car)

# Looping with index using enumerate
print("\nCars with Index:")
for index, car in enumerate(Cars):
    print(f"Index {index}: {car}")

# Nested tuples
print("\n--- Nested Tuple ---")
Nested = (1, 2, (3, 4), 5, (6, 7, 8))
print("Nested Tuple:", Nested)
print("Access Nested Element (index 2):", Nested[2])
print("Access Inner Element Nested[2][0]:", Nested[2][0])
print("Access Inner Element Nested[4][2]:", Nested[4][2])

# Looping through nested tuple
print("\nLooping Through Nested Tuple:")
for item in Nested:
    if isinstance(item, tuple):
        print("Inner Tuple:", item)
        for inner in item:
            print("  -", inner)
    else:
        print("Element:", item)

# Tuple unpacking
print("\n--- Tuple Unpacking ---")
Coordinates = (10, 20, 30)
x, y, z = Coordinates
print(f"Coordinates: x={x}, y={y}, z={z}")

# Swapping variables using tuple unpacking
a, b = 5, 10
print(f"\nBefore Swap: a={a}, b={b}")
a, b = b, a
print(f"After Swap: a={a}, b={b}")

# Using * for extended unpacking
First, *Middle, Last = (1, 2, 3, 4, 5)
print("\nExtended Unpacking:")
print("First:", First)
print("Middle:", Middle)
print("Last:", Last)

# Converting list to tuple
print("\n--- List to Tuple Conversion ---")
ListData = [100, 200, 300]
ConvertedTuple = tuple(ListData)
print("Original List:", ListData)
print("Converted Tuple:", ConvertedTuple)

# Converting tuple to list
TupleData = (400, 500, 600)
ConvertedList = list(TupleData)
print("\nOriginal Tuple:", TupleData)
print("Converted List:", ConvertedList)

# Checking data type
print("\n--- Type Checking ---")
print("Type of Cars:", type(Cars))
print("Type of Numbers:", type(Numbers))

# Using tuple as dictionary key (since tuples are immutable)
print("\n--- Tuple as Dictionary Key ---")
Locations = {
    (28.6139, 77.2090): "New Delhi",
    (19.0760, 72.8777): "Mumbai",
    (22.5726, 88.3639): "Kolkata"
}
print("Locations Dictionary:", Locations)
for coords, city in Locations.items():
    print(f"{city} is at coordinates {coords}")

# Returning multiple values from a function as tuple
print("\n--- Function Returning Tuple ---")
def min_max(numbers):
    return min(numbers), max(numbers)

Result = min_max([45, 12, 78, 34, 89, 23])
print("Min and Max:", Result)
MinVal, MaxVal = Result
print(f"Minimum: {MinVal}, Maximum: {MaxVal}")

# All about tuples summary
print("\n--- Tuple Summary ---")
print("1. Tuples are ordered, immutable collections")
print("2. Created using parentheses () or tuple() constructor")
print("3. Elements can be accessed by index and slicing")
print("4. Tuples can contain mixed data types")
print("5. Tuples are faster than lists for fixed data")
print("6. Use tuples when data should not change")
print("7. Tuples can be used as dictionary keys (lists cannot)")

