TheBoard = {'Top-L':'   ','Top-M':'   ','Top-R':'   ',
            'Mid-L':'   ','Mid-M':'   ','Mid-R':'   ',
            'Low-L':'   ','Low-M':'   ','Low-R':'   '}

def PrintBoard(Board):
     print(Board['Top-L'] + '|' + Board['Top-M'] + '|' + Board['Top-R'])
     print('---+---+---')
     print(Board['Mid-L'] + '|' + Board['Mid-M'] + '|' + Board['Mid-R'])
     print('---+---+---')
     print(Board['Low-L'] + '|' + Board['Low-M'] + '|' + Board['Low-R'])


Turn = ' X '
for i in range(9):
    PrintBoard(TheBoard)
    move = input('Turn for Mr.' + Turn + '.Move on which space ? '+ '\n')
    TheBoard[move] = Turn
    if Turn == ' X ':
        Turn = ' O '
    else:
        Turn = ' X '
PrintBoard(TheBoard)