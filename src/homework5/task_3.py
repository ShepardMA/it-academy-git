def count_it(sequence):
    counts = {}
    for char in sequence:
        num = int(char)
        counts[num] = counts.get(num, 0) + 1
    sorted_counts = sorted(counts.items(), key=lambda x: x[1], reverse=True)
    top_3 = dict(sorted_counts[:3])
    return top_3


sequence = "12345678901234567890"
result = count_it(sequence)
print(result)
