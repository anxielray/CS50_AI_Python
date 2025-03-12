import math

# Define the Minimax function
def minimax(board, depth, is_maximizing):
    if check_winner(board) == "X":
        return 1  # M   aximizing player wins
    elif check_winner(board) == "O":
        return -1  # Minimizing player wins
    elif is_draw(board):
        return 0  # Draw

    if is_maximizing:
        best_score = -math.inf
        for move in get_available_moves(board):
            board[move] = "X"
            score = minimax(board, depth + 1, False)
            board[move] = " "  # Undo move
            best_score = max(score, best_score)
        return best_score
    else:
        best_score = math.inf
        for move in get_available_moves(board):
            board[move] = "O"
            score = minimax(board, depth + 1, True)
            board[move] = " "  # Undo move
            best_score = min(score, best_score)
        return best_score

# Function to get available moves
def get_available_moves(board):
    return [i for i in range(len(board)) if board[i] == " "]

# Function to check for a winner
def check_winner(board):
    win_patterns = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),  # Rows
        (0, 3, 6), (1, 4, 7), (2, 5, 8),  # Columns
        (0, 4, 8), (2, 4, 6)  # Diagonals
    ]
    for a, b, c in win_patterns:
        if board[a] == board[b] == board[c] and board[a] != " ":
            return board[a]
    return None

# Function to check if the game is a draw
def is_draw(board):
    return " " not in board

# Function to find the best move
def find_best_move(board):
    best_score = -math.inf
    best_move = None
    for move in get_available_moves(board):
        board[move] = "X"
        score = minimax(board, 0, False)
        board[move] = " "  # Undo move
        if score > best_score:
            best_score = score
            best_move = move
    return best_move

# Example usage with a Tic-Tac-Toe board
board = ["X", "O", "X",
         " ", "O", " ",
         " ", " ", "X"]

best_move = find_best_move(board)

import sys
from PIL import Image, ImageDraw, ImageFont

def read_board(filename):
    """Reads a Tic-Tac-Toe board from a file."""
    with open(filename, 'r') as file:
        board = [list(line.strip()) for line in file.readlines()]
    return board

def maximin_move(board):
    """Implements a simple Maximin strategy to choose a move."""
    best_move = None
    min_value = float('inf')
    
    for i in range(3):
        for j in range(3):
            if board[i][j] == '.':  # Empty spot
                # Assign a dummy evaluation for now
                value = i * j  # Replace with actual evaluation function
                if value < min_value:
                    min_value = value
                    best_move = (i, j)
    
    return best_move

def draw_board(board, move=None, output_file='tic_tac_toe.png'):
    """Draws a Tic-Tac-Toe board and saves it as an image."""
    cell_size = 100
    img_size = cell_size * 3
    img = Image.new("RGB", (img_size, img_size), "white")
    draw = ImageDraw.Draw(img)
    
    # Draw grid
    for i in range(1, 3):
        draw.line([(0, i * cell_size), (img_size, i * cell_size)], fill="black", width=5)
        draw.line([(i * cell_size, 0), (i * cell_size, img_size)], fill="black", width=5)
    
    # Draw X and O
    font = ImageFont.load_default()
    for i in range(3):
        for j in range(3):
            x, y = j * cell_size + 30, i * cell_size + 30
            if board[i][j] == 'X':
                draw.text((x, y), 'X', fill="blue", font=font)
            elif board[i][j] == 'O':
                draw.text((x, y), 'O', fill="red", font=font)
    
    # Highlight chosen move
    if move:
        i, j = move
        draw.rectangle([
            (j * cell_size, i * cell_size),
            ((j + 1) * cell_size, (i + 1) * cell_size)
        ], outline="green", width=5)
    
    img.save(output_file)
    print(f"Saved board to {output_file}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 script.py game.txt")
        sys.exit(1)
    
    board = read_board(sys.argv[1])
    move = maximin_move(board)
    draw_board(board, move)
