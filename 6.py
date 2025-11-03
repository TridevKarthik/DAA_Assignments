#Implement Knapsack problem for 6 items, using brute force methodology (Use Combinations)


def combos(data, k):
    if k == 0:
        return [[]]
    if len(data) < k:
        return []
    head = data[0]
    tail = data[1:]
    with_head = [[head] + c for c in combos(tail, k - 1)]
    without_head = combos(tail, k)
    return with_head + without_head

goods = [(4, 20), (2, 15), (6, 40), (3, 25), (5, 35), (1, 10)]
limit = 13

max_score = 0
used_weight = 0
chosen_set = []

for size in range(1, len(goods) + 1):
    for group in combos(list(range(len(goods))), size):
        w = sum(goods[i][0] for i in group)
        v = sum(goods[i][1] for i in group)
        if w <= limit and v > max_score:
            max_score = v
            used_weight = w
            chosen_set = group

print("Selected group:")
for i in chosen_set:
    print(f"  Item {i}: {goods[i]}")
print(f"Total value: {max_score}\nTotal weight: {used_weight}\nCapacity: {limit}")