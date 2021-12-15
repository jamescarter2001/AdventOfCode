class Board:
    def __init__(self, id, data):
        self.id = id
        self.contents = []
        self.won = False

        for line in data:
            row = list(filter(lambda x: x != '',line.split(' ')))
            row = list(map(lambda x: int(x), row))
            self.contents.append(row)

bingo = open('bingo.txt', 'r')
file = bingo.read()

boards = file.split('\n\n')

board_array = []

count = 0
for board in boards:
    fragments = board.split('\n')
    board = Board(count, fragments)

    board_array.append(board)
    count+=1

#for board in board_array:
    #print(board.contents)

print(len(board_array))
draw = [30,35,8,2,39,37,72,7,81,41,25,46,56,18,89,70,0,15,84,75,88,67,42,44,94,71,79,65,58,52,96,83,54,29,14,95,66,61,97,68,57,90,55,32,17,47,20,98,1,69,63,62,31,86,77,85,87,93,26,40,24,19,48,76,73,49,34,45,82,22,80,78,23,6,59,91,64,43,21,51,13,3,53,99,4,28,33,74,12,9,36,50,60,11,27,10,5,16,92,38]

picked_nums = []

def get_score(board):
    score = 0
    for row in board.contents:
        for num in row:
            if num not in picked_nums:
                score+=num
    return score * picked_nums[-1]

def check_rows(board):
    for row in board.contents:
                if set(row).issubset(picked_nums):
                    print(f'Winner: {board.id} (ROW) -> {get_score(board)}')
                    return True
    return False

def check_columns(board):
    for i in range(5):
        column = list(map(lambda x: x[i], board.contents))

        if set(column).issubset(picked_nums):
            print(f'Winner: {board.id} (COLUMN) -> {get_score(board)}')
            return True
    
    return False

def draw_nums():
    last_winner = None
    for num in draw:
        winners = []
        picked_nums.append(num)

        for board in board_array:
            row_status = check_rows(board)
            if row_status != True:
                col_status = check_columns(board)
            if row_status == True or col_status == True:
                winners.append(board)
                last_winner = board
        
        for winner in winners:
            board_array.remove(winner)

        if len(board_array) == 0:
            return last_winner

winner = draw_nums()

print(f'Total: {get_score(winner)}')