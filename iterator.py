# Iterable
numbers = [10, 20, 30, 40, 50]

# Create an iterator
it = iter(numbers)

# Get values using next()
a = next(it)
b = next(it)
c = next(it)
d = next(it)
e = next(it)
f = next(it)
print("Numbers:", a, b, c, d, e)

# Mathematical operations
total = a + b + c + d + e
average = total / 5
maximum = max(a, b, c, d, e)
minimum = min(a, b, c, d, e)

print("Sum =", total)
print("Average =", average)
print("Maximum =", maximum)
print("Minimum =", minimum)
print("Maximum=", maximum)
