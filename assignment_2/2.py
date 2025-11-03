#Implement Cominations from scratch (do not use inbuilt methods) ) - For any data type.

def Combinations(arr, Size_of_list):
    if Size_of_list == 0:
        return [[]]
    
    if not arr or Size_of_list > len(arr):
        return []

    head = arr[0]
    Rest_of_the_list = arr[1:]

    #including the head in the combination.
    Including_Head = [[head] + combo for combo in Combinations]
    #exluding head so that it doesnt cause repetition.
    Excluding_Head = Combinations(Rest_of_the_list, Size_of_list)

    return Including_Head + Excluding_Head

print(Combinations([1, 2, 3, 4], 3))
