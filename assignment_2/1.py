#Implement Permutation from scratch (do not use inbuilt methods) - For any data type.
def permuation (arr): # using a function to seperate the values and go to the last value of the list.
    num = list(arr)
    if len(num) <=1:
        return [num]
    
    Display = [] # Final List To Print All Lists.

    temp = num[0] # having temp variable so can go back to the temp after the perm loop is done.

    currentperm = permuation(num[1:])

    for perm in currentperm:
        for i in range (len(perm) + 1):
            calcperm = perm[:i] + [temp] + perm[i:]
            Display.append(calcperm) #goes back to currentperm and updates then gets the temp var.

    return Display
        
print ("List Used For Permutation [1,2,3,4]:\n")
print(permuation([1,2,3,4]))  #calls the list to print all the permutation
