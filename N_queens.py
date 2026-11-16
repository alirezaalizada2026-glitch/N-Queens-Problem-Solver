board = [[0 for col in range(8)] for row in range(8)]

solutions = []

def is_safe(row, col):
    for i in range(row):
        for j in range(8):
            
            if board[i][j] == 1:
                
                if j == col:
                    return False
                
                if abs(row - i) == abs(col - j):
                    return False
    
    return True

def n_queens(row):
    
    if row == 8:
        solutions.append([r[:] for r in board])
        return
    for col in range(8):
        
        if is_safe(row, col):
            
            board[row][col] = 1
            
            n_queens(row + 1)
            
            board[row][col] = 0
            
n_queens(0)
print('Total Solutions : ', len(solutions))

for index, solution in enumerate(solutions, start=1):
    print(f"\nsolution {index}")
    
    for row in solution:
        for cell in row:
            if cell == 1:
                print("Q", end=" ")
            else:
                print("•", end=" ")
        print()
# if n_queens(0):
#     for row in board:
#         for cell in row:
#             if cell == 1:
#                 print("Q", end=" ")
#             else:
#                 print("•", end=" ")
#         print()
# else:
#     print('No solution found!')