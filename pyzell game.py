import random

def shuffle_puzzle():
    # Pazl bloklari
    puzzle = [[1, 2, 3], [4, 5, 6], [7, 8, " "]]
    
    # Blokni tasodifiy ravishda almashtirish
    for _ in range(100):
        row, col = find_blank(puzzle)
        moves = get_valid_moves(row, col)
        random_move = random.choice(moves)
        move_block(puzzle, row, col, random_move)
    
    return puzzle

def find_blank(puzzle):
    # " " bo'sh joyning indeksi (qator, ustun)
    for row in range(len(puzzle)):
        for col in range(len(puzzle[row])):
            if puzzle[row][col] == " ":
                return row, col

def get_valid_moves(row, col):
    # Berilgan pozitsiyadagi to'g'ri turdagi o'rnatuvchilarning ro'yxati
    valid_moves = []
    if row > 0:
        valid_moves.append("up")
    if row < 2:
        valid_moves.append("down")
    if col > 0:
        valid_moves.append("left")
    if col < 2:
        valid_moves.append("right")
    return valid_moves

def move_block(puzzle, row, col, move):
    # Blokni berilgan yo'nalishda almashtirish
    if move == "up":
        puzzle[row][col], puzzle[row-1][col] = puzzle[row-1][col], puzzle[row][col]
    elif move == "down":
        puzzle[row][col], puzzle[row+1][col] = puzzle[row+1][col], puzzle[row][col]
    elif move == "left":
        puzzle[row][col], puzzle[row][col-1] = puzzle[row][col-1], puzzle[row][col]
    elif move == "right":
        puzzle[row][col], puzzle[row][col+1] = puzzle[row][col+1], puzzle[row][col]

def print_puzzle(puzzle):
    # Pazlni ekranga chiqarish
    for row in puzzle:
        print(" ".join(map(str, row)))

def play_puzzle_game():
    puzzle = shuffle_puzzle()
    moves = 0
    
    while True:
        print_puzzle(puzzle)
        print("Hareketlar soni:", moves)
        move = input("Yuqori (U), Pastga (D), Chapga (L), O'ngga (R) harakat qiling (Chiqish uchun Q): ")
        
        if move.upper() == "Q":
            print("O'yin tugadi.")
            break
        
        row, col = find_blank(puzzle)
        valid_moves = get_valid_moves(row, col)
        
        if move.upper() in valid_moves:
            move_block(puzzle, row, col, move.lower())
            moves += 1
        else:
            print("Noto'g'ri harakat. Boshqa harakatni kiriting.")

play_puzzle_game()
