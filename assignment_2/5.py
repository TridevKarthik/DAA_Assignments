
#Implement Knapsack problem for 6 items, using brute force methodology (Use Binary representation to represent items in the sack)

val = [1,5,3,8,9,2]
weight = [2,6,4,9,8,3]

#knapsacks max capacity.
limit = 15
count = len(weight)


max_val = 0
chosen_mask = None

for i in range(1 << count): 
    crnt_val = crnt_weight = 0
    for j in range(count):
        if i & (1 << j): 
            crnt_weight += weight[j]
            crnt_val += val[j]
    if crnt_weight <= limit and crnt_val > max_val:
        max_val = crnt_val
        chosen_mask = i
print ("Best combination found:\n")
print("Best value:", max_val)
print("Selected items:", [j for j in range(count) if chosen_mask & (1 << j)])
