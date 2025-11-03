#Get input from user on 2 matrix and multiply them.
def Matrix_Multiply(Matrix_A, Matrix_B):
    Product = [[0,0], [0,0]] # initializing the result matrix it to zero for now
    for i in range(len(Matrix_A)):
        current_row = [Matrix_A[i][0], Matrix_A[i][1]] 
        print(f"Multiplying Row {i + 1} {current_row}")
        for j in range(len(Matrix_A[i])):
            current_collumn = [Matrix_B[0][j], Matrix_B[1][j]]
            print(f"and Column {j + 1} {current_collumn}")
            Product[i][j] = (current_row[0] * current_collumn[0]) + (current_row[1] * current_collumn[1])
    return Product
Matrix_A = [[4, -2], [1, 5]]
Matrix_B = [[3, 7], [-6, 2]]
result_matrix = Matrix_Multiply(Matrix_A, Matrix_B)
print("Product Of Two Matrix:")
print(result_matrix)
