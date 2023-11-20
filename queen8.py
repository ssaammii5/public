import random

def generate_random_board():
    return [random.randint(0, 7) for _ in range(8)]

def calculate_attacks(board):
    attacks = 0
    for i in range(len(board)):
        for j in range(i + 1, len(board)):
            if board[i] == board[j] or abs(board[i] - board[j]) == abs(i - j):
                attacks += 1
    return attacks

def hill_climbing():
    current_board = generate_random_board()
    current_attacks = calculate_attacks(current_board)

    while current_attacks > 0:
        neighbor_boards = []
        for i in range(8):
            for j in range(8):
                if current_board[i] != j:
                    neighbor_board = list(current_board)
                    neighbor_board[i] = j
                    neighbor_boards.append((neighbor_board, calculate_attacks(neighbor_board)))

        neighbor_boards.sort(key=lambda x: x[1])
        best_neighbor, best_attacks = neighbor_boards[0]

        if best_attacks < current_attacks:
            current_board = best_neighbor
            current_attacks = best_attacks
        else:
            # Local minimum reached
            break

    return current_board

def print_board(board):
    for i in range(8):
        row = ['Q' if j == board[i] else '.' for j in range(8)]
        print(' '.join(row))

if __name__ == "__main__":
    solution = hill_climbing()
    print("Solution:")
    print_board(solution)
