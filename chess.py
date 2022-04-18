"""
This is an cli chess. Hopefully. You tell the moves by terminal commands and
yeah.
"""


import createboard as createb


def displayboard(board):
    """
    formats the board nicely for printing to terminal
    """


    # for row in board:
        # print(row)
    # print()
    # print()


    print("a  b  c  d  e  f  g  h ")
    print()
    i = 1

    # iterate through the board dict and print
    # each row one item at a time
    for x in range(8):

        for y in range(8):
            print(f"{board[x][y]:3}", end="")
        print()



def main():
    board = createb.createboard()
    # initboard(board)
    displayboard(board)



if __name__ == '__main__':
    main()
