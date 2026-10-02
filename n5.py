numbers = [int(x) for x in range(1, 50)]
for i in range(2, 50):
    new_numbers = []
    for x in numbers:
        if x == i or x % i != 0:
            new_numbers.append(x)
    numbers = new_numbers

print(numbers)