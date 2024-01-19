SIZE = 8
EMPTY = -1
POSSIBLE_MOVES = [(1, 2), (2, 1), (-1, 2), (-2, 1), (1, -2), (2, -1), (-1, -2), (-2, -1)]

def knight(p1, p2) -> int:

    start = toCoordinates(p1)
    end = toCoordinates(p2)
    board = [ [EMPTY]*SIZE for line in range(SIZE)]
    board[start[0]][start[1]] = 0

    moves = 0
    while board[end[0]][end[1]] == EMPTY:
        for x in range(SIZE):
            for y in range(SIZE):
                if board[x][y] == moves:
                    for delta in POSSIBLE_MOVES:
                        newX = x + delta[0]
                        newY = y + delta[1]
                        if 0 <= newX and newX < SIZE and 0 <= newY and newY < SIZE:
                            board[newX][newY] = moves + 1 

        moves+=1
    return moves

# transforms the algebraic string notation (e.g. 'e4') into numeric, zero based coordinates [4, 3]
def toCoordinates(algebraicNotation: str) -> list:
    return [ord(algebraicNotation[0:1]) - ord('a'), int(algebraicNotation[1:2]) - 1]