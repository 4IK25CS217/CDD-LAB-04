numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

evens = []
for num in numbers:
    if num % 2 == 0:
        evens.append(num)

print(evens)  # Output: [2, 4, 6, 8, 10]
