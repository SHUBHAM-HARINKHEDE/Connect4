
board=[
  [0,0,0,0,0,0,0],
  [0,0,0,0,0,0,0],
  [0,0,0,0,0,0,0],
  [0,0,0,0,0,0,0],
  [0,0,0,0,0,0,0],
  [0,0,0,0,0,0,0]
]

def isWin():
  #check row
  for row in range(6):
    for col in range(7-3):
      #print(row,col)
      if board[row][col]==board[row][col+1]==board[row][col+2]==board[row][col+3]!=0:
        return board[row][col]
  #Column
  for row in range(6-3):
    for col in range(7):
      #print(row,col)
      if board[row][col]==board[row+1][col]==board[row+2][col]==board[row+3][col]!=0:
        return board[row][col]
  #digonal/
  for row in range(6-3):
    for col in range(7-3):
      #print(row,col)
      if board[row][col]==board[row-1][col+1]==board[row-2][col+2]==board[row-3][col+3]!=0:
        return board[row][col]
  #digonal\
  for row in range(6-3):
    for col in range(7-3):
      if board[row][col]==board[row+1][col+1]==board[row+2][col+2]==board[row+3][col+3]!=0:
        return board[row][col]
        


def printBoard():
  for row in board:
    print(row)

def isColEmpty(col):
  if board[0][col]==0:
    return True
  else:
    return False
def makemove(col,player):
  for row in range(len(board)):
    row=len(board)-1-row
    if(board[row][col]==0):
      board[row][col]=player
      break

def player():
  col= int(input("Column:"))
  print(col)
  if isColEmpty(col):
    makemove(col,1)
  else:
    print("column is not empty:")
    player()
def opponent():
  col= int(input("Column:"))
  print(col)
  if isColEmpty(col):
    makemove(col,2)
  else:
    print("column is not empty:")
    opponent()
if __name__=='__main__':
  while True:
    player()
    printBoard()
    if isWin()!=None:
      print("You WON")
      break
      
    opponent()
    printBoard()
    if isWin()!=None:
      print("You WON")
      break
