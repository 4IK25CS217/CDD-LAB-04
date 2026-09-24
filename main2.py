numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

evens = []
i = 0
while i < len(numbers):
    if numbers[i] % 2 == 0:
        evens.append(numbers[i])
    i += 1

print(evens)  # Output: [2, 4, 6, 8, 10]
