#Task3-Python Programming

#1. Table of number
n = int(input("Enter a number:"))
print (f"Multiplication table for {n}:")

for i in range(1,11):
 print(f"{n}*{i} = {n*i}")
 
 #2. Swap Two numbers

a= int(input("a="))
b=int(input("b="))

a,b=b, a
print (f"After Swaping: a={a}, b={b}")

#3. check substring

x1= input("Enter the main string: ")
x2=input("Enter the substing string:")

result = x2 in x1
print(result)

#4.Decimal to Binary

def binary(n):
    return bin(n) [2:]

decimal_number= int(input("Enter a decimal number: "))

binary_result =binary(decimal_number)
print(f"{binary_result}")

#5. Matrix Addition

matrix1=[
    [3,2,4],
    [7,4,1],
    [9,6,3]
]

matrix2=[
    [8,5,7],
    [1,2,3],
    [5,4,1]
]

result = []

for i in range(len(matrix1)):
    row=[]
    for j in range(len(matrix1[0])):
        row.append(matrix1[i][j] + matrix2[i][j])
    result.append(row)

print("Resultant satrix:")
for row in result:
    print(row)
    
#6. Matrix Multiplication

matrixA =[
       [9,4],
       [3,6]
]
matrixB = [
       [2,3],
       [6,7]
]

result= [[0,0], [0,0]]

for i in range(len(matrixA)):
    for j in range(len(matrixB[0])):
        for k in range(len(matrixB)):
            result[i][j] += matrixA[i][k] * matrixB[k][j]
print("Resultant Matrix:")
for row in result:
    print(row)
    
#7. Find Second Largest

n = [15,23,47, 65, 28, 98, 54,9,1]

n.sort(reverse=True)

second_largest = n[1]

print("The Second Largest Number is:", second_largest)

#8. check Anagram

str1 =input("Enter a first string: ")
str2 =input("Enter a second string: ")

if sorted(str1) == sorted(str2):
    print("The Strings are Anagrams.")
    
else:
    print("The Strings are not Anagrams.")
    
#9. Al-Based Tic-Tac-Toe

import random
board = [' ' for _ in range(9)]  
PLAYER = 'X'
AI = 'O'

def print_board():
    for i in range(0, 9, 3):
        print('|', board[i], '|', board[i+1], '|', board[i+2], '|')
        if i < 6:
            print('-------------')

def check_winner(board, player):
    win_conditions = [(0, 1, 2), (3, 4, 5), (6, 7, 8),  
                      (0, 3, 6), (1, 4, 7), (2, 5, 8), 
                      (0, 4, 8), (2, 4, 6)]  

    for condition in win_conditions:
        if board[condition[0]] == board[condition[1]] == board[condition[2]] == player:
            return True
    return False

def is_board_full(board):
    return ' ' not in board

def minimax(board, depth, is_maximizing):
    if check_winner(board, AI):  
        return 1
    elif check_winner(board, PLAYER):  
        return -1
    elif is_board_full(board): 
        return 0

    if is_maximizing:
        best = -float('inf')
        for i in range(9):
            if board[i] == ' ':
                board[i] = AI
                best = max(best, minimax(board, depth + 1, False))
                board[i] = ' '
        return best
    else:
        best = float('inf')
        for i in range(9):
            if board[i] == ' ':
                board[i] = PLAYER
                best = min(best, minimax(board, depth + 1, True))
                board[i] = ' '
        return best

def best_move():
    best_value = -float('inf')
    move = -1

    for i in range(9):
        if board[i] == ' ':
            board[i] = AI
            move_value = minimax(board, 0, False)
            board[i] = ' '
            if move_value > best_value:
                best_value = move_value
                move = i

    return move

def play_game():
    print("Welcome to Tic-Tac-Toe!")
    while True:
        print_board()
        
        user_move = int(input("Enter your move (1-9): ")) - 1
        if board[user_move] != ' ':
            print("Invalid move. Try again.")
            continue
        board[user_move] = PLAYER

        if check_winner(board, PLAYER):
            print_board()
            print("You win!")
            break

        if is_board_full(board):
            print_board()
            print("It's a tie!")
            break

        ai_move = best_move()
        board[ai_move] = AI
        print(f"AI's move: {ai_move + 1}")

        if check_winner(board, AI):
            print_board()
            print("AI wins!")
            break

        if is_board_full(board):
            print_board()
            print("It's a tie!")
            break

play_game()


#10.  AI Based Tic-Tac-Toe with Minimax Algorithm

import math
board = [" " for _ in range(9)]  
def print_board():
    for row in range(3):
        print("|".join(board[row * 3:(row + 1) * 3]))
        if row < 2:
            print("-----")
def check_winner(b, player):
    win_conditions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8], 
        [0, 3, 6], [1, 4, 7], [2, 5, 8], 
        [0, 4, 8], [2, 4, 6]            
    ]
    for condition in win_conditions:
        if all(b[i] == player for i in condition):
            return True
    return False

def is_full(b):
    return " " not in b

def evaluate(b):
    if check_winner(b, "O"): 
        return 1
    elif check_winner(b, "X"):  
        return -1
    return 0  
def minimax(b, depth, is_maximizing):
    score = evaluate(b)
 
    if score == 1 or score == -1 or is_full(b):
        return score

    if is_maximizing: 
        best_score = -math.inf
        for i in range(9):
            if b[i] == " ":
                b[i] = "O"
                best_score = max(best_score, minimax(b, depth + 1, False))
                b[i] = " " 
        return best_score
    else:  
        best_score = math.inf
        for i in range(9):
            if b[i] == " ":
                b[i] = "X"
                best_score = min(best_score, minimax(b, depth + 1, True))
                b[i] = " "  
        return best_score

def find_best_move():
    best_score = -math.inf
    best_move = -1
    for i in range(9):
        if board[i] == " ":
            board[i] = "O"  
            move_score = minimax(board, 0, False)
            board[i] = " " 
            if move_score > best_score:
                best_score = move_score
                best_move = i
    return best_move

def play_game():
    print("Welcome to Tic-Tac-Toe!")
    print("You are X. AI is O.")
    print_board()
    
    while True:
        
        human_move = int(input("Enter your move (0-8): "))
        if board[human_move] != " ":
            print("Invalid move! Try again.")
            continue
        board[human_move] = "X"
        print_board()

        
        if check_winner(board, "X"):
            print("Congratulations! You win!")
            break

        if is_full(board):
            print("It's a draw!")
            break

        print("AI is making its move...")
        ai_move = find_best_move()
        board[ai_move] = "O"
        print_board()

        if check_winner(board, "O"):
            print("AI wins! Better luck next time.")
            break

        if is_full(board):
            print("It's a draw!")
            break

play_game()


