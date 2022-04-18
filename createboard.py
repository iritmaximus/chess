"""
module to init the baord.
TODO support for fen
TODO read init from file
"""

# TODO explicit file for init template
EXAMPLE_FEN = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1"
TEST_FEN = "6rr/2pbk3/1p1p4/p2Pp2p/P1P1Pp1P/1P3P2/3K1B2/6RR w - - 7 31"




def createboard(cmd="init", fen=EXAMPLE_FEN):
    """
    creates board with given fen notation, if not
    it falls back to the default beginning of chess
    :params cmd: str, what command is wanted, fallback normal new match
    :params fen: str, given fen for the board creation
    """


    fen = TEST_FEN


    match cmd:
        case "init":
            boardtemplate = initboard()
            readyboard = applyfen(fen, boardtemplate)
        case "file":
            print("board creation with a file :)")
        case _:
            print("Err, no commands")


    return readyboard


def initboard():
    """
    a function that creates the board and initializes
    it with a given fen notation
    the board is formatted like nested list:
    [           a   b   c   ...
        8 row [ 1,  2,  3,  ...],
        7 row [ 1,  2,  3,  ...],
    ]
    """

    # { a: { 1: -, 2: k, 3: Q }}

    board = []

    for x in range(8):
        row = []

        for y in range(8):
            row.append("-")

        board.append(row)

    return board


def parsefen(fen):
    """
    reads the given fen notation and parses it
    """

    fenrows = fen.split("/")

    gamedata = fenrows[-1].split()
    gamedata.pop(0)

    fenrows[-1] = fenrows[-1].split()[0]

    return fenrows, gamedata




def applyfen(fen, board):
    """
    takes fen, applies it to the board template
    """
    parsedfen, gamedata = parsefen(fen)

    print("fen:", parsedfen)
    print("gd:",gamedata)
    print()


    # iterate through indexes of our board template
    # so we can inject the fen template to it
    for x in range(8):

        boardrow = board[x]
        fenrow = parsedfen[x]

        # for skipping empty squares
        i = 0
        # for keeping the index while skipping
        j = 0


        # iterate through the board rows and fen rows
        for y in range(8):

            # skips if there are empty spaces on the fen ex. 6k1
            if i > 0:
                i -= 1
                continue

            else:
                # check if next item on the current row of fen
                # is a number
                if fenrow[j].isdigit():
                    # if true, set j (skipping index) to the amount of to-be-skipped squares
                    i = int(fenrow[j]) - 1
                    j += 1
                    continue

                # if item is char ie piece, add it to the board
                else:
                    boardrow[y] = fenrow[j]
                    j += 1

        # add new row to the board
        board[x] = boardrow


    return board



def main():
    createboard()

if __name__ == "__main__":
    main()
