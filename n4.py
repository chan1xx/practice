text = input().lower()

counts = {}
for c in text:
    if c in counts:
        counts[c] = counts[c] + 1
    else:
        counts[c] = 1
max1 = ""
for c in counts:
    if max1 == "" or counts[c] > counts[max1]:
        max1 = c
max2 = ""
for c in counts:
    if c != max1:
        if max2 == "" or counts[c] > counts[max2]:
            max2 = c
max3 = ""
for c in counts:
    if c != max1 and c != max2:
        if max3 == "" or counts[c] > counts[max3]:
            max3 = c
print(max1, counts[max1])
print(max2, counts[max2])
print(max3, counts[max3])