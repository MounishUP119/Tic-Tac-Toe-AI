board = [" "]*9

def show():
    for i in range(0,9,3):
        print(board[i:i+3])
    print()

def win(p):
    w = [(0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6)]
    return any(board[a]==board[b]==board[c]==p for a,b,c in w)

def full():
    for row in board:
        if " " in row:
            return False
    return True
    

def minimax(ai):
    if win("O"): return 1
    if win("X"): return -1
    if full(): return 0
    best = -2 if ai else 2
    for i in range(9):
        if board[i]==" ":
            board[i] = "O" if ai else "X"
            score = minimax(not ai)
            board[i] = " "
            best = max(best,score) if ai else min(best,score)
    return best

def ai_move():
    best, move = -2, 0
    for i in range(9):
        if board[i]==" ":
            board[i]="O"
            score=minimax(False)
            board[i]=" "
            if score>best: best,move=score,i
    board[move]="O"

print("You = X, AI = O")
while True:
    show()
    m = int(input("Enter (1-9): ")) - 1
    board[m] = "X"
    if win("X"): show(); print("You win!"); break
    if full(): show(); print("Draw!"); break
    ai_move()
    if win("O"): show(); print("AI wins!"); break