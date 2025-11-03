# Convert an integer to binary equivalent, take a random position, check if the position is 0 or 1 and print true or false accordinly.


def Decimal_Binary(num):
    if num == 0:
        return [0]  
    if num == 1:
        return [1] 

    
    binary = Decimal_Binary(num // 2)

    # appending the least significant bit using odd or even.
    if num % 2 == 0:
        binary.append(0)
    else:
        binary.append(1)

    return binary


num = int(input("Enter A Integer To Convert To Binary: "))


Binary_List = Decimal_Binary(num)

# converting each binary digit to true or false.
Binary_Bool = [bool(bit) for bit in Binary_List]

posi_check = int(input("Enter The Position U Want To Check: "))

# Validate the position and print the result
if 1 <= posi_check <= len(Binary_Bool):
    bit_value = Binary_Bool[posi_check - 1]
    print(f"The value at position {posi_check} is {'True' if bit_value else 'False'}")
else:
    print("Invalid position entered")

print("Binary representation (as booleans):", Binary_Bool)