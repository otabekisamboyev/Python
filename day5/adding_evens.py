total = 0
for evens in range(0, 101, 2):
    total += evens
print(f"Sum of even numbers in 1 to 100 is {total}")

total2 = 0
for evens in range(1, 101):
    if evens % 2 == 0:
        total2 += evens
print(f"Sum of even numbers in 1 to 100 is {total2}")
