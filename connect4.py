# import os library
import os

# Game Board
board=[
  [0,0,0,0,0,0,0],
  [0,0,0,0,0,0,0],
  [0,0,0,0,0,0,0],
  [0,0,0,0,0,0,0],
  [0,0,0,0,0,0,0],
  [0,0,0,0,0,0,0]
]

#function to clear screen
def clear():
  os.system("cls") if os.name=="nt" else os.system("clear")
#function to check player won or not
def draw():
  for row in range(7):
    for col in range(7):
      if board[row][col]==0:
        return False
  return True
def isWin():
  #check row
  for row in range(6):
    for col in range(7-3):
      if board[row][col]==board[row][col+1]==board[row][col+2]==board[row][col+3]!=0:
        return board[row][col]
  #Column
  for row in range(6-3):
    for col in range(7):
      if board[row][col]==board[row+1][col]==board[row+2][col]==board[row+3][col]!=0:
        return board[row][col]
  #digonal/
  for row in range(6-3):
    for col in range(7-3):
      if board[row][col]==board[row-1][col+1]==board[row-2][col+2]==board[row-3][col+3]!=0:
        return board[row][col]
  #digonal\
  for row in range(6-3):
    for col in range(7-3):
      if board[row][col]==board[row+1][col+1]==board[row+2][col+2]==board[row+3][col+3]!=0:
        return board[row][col]
        

#function to print board
def printBoard():
  #this clear screen before printing board
  clear()
  for row in board:
    print(row)
#Check wheather column have empty space or not.
def isColEmpty(col):
  if board[0][col]==0:
    return True
  else:
    return False
#This to make a move i.e to fill column choosen by player 
def makemove(col,player):
  for row in range(len(board)):
    row=len(board)-1-row
    if(board[row][col]==0):
      board[row][col]=player
      break
#this is to take input from first player
def player():
  col= int(input("Column(0-6):"))
  print(col)
  if col>6:                           #invalid if column is not in {0,1,2,3,4,5,6}
    print("Invalid column:(")
    player()
  elif isColEmpty(col):               #make move if column is empty
    makemove(col,1)
  else:
    print("column is not empty:")
    player()
#this is to take input from other player
def opponent():
  col= int(input("Column:(0-6)"))
  print(col)
  if col>6:
    print("Invalid column:(")
    player()
  elif isColEmpty(col):
    makemove(col,2)
  else:
    print("column is not empty:")
    opponent()
if __name__=='__main__':
  printBoard()
  while True:
    player()
    printBoard()
    if isWin()!=None:
      print("You WON")
      break
    if draw(): 
      print("Game Draw")
      break 
    opponent()
    printBoard()
    if isWin()!=None:
      print("You WON")
      break
    if draw(): 
      print("Game Draw")
      break 
