import random

numbers = [random.randint(1, 100) for _ in range(5)]

print("Generated numbers:", numbers)
print("Maximum number:", max(numbers))
