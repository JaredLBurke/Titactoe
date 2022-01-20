
#GLOBAL VARIABLES
global winner
#Will only be off once a result has been determined
game_still_going =True

#Game Results (won or tied)
winner = None

#whose turn is it
current_player = "X"

#The Board the game will be played on
board = ["-", "-", "-", 
         "-", "-", "-", 
        "-", "-", "-"]

def display_board():
  #displays board + example 
  print("\n")
  print(board[0] + " | " + board[1] + " | " + board[2] + "     1 | 2 | 3")
  print(board[3] + " | " + board[4] + " | " + board[5] + "     4 | 5 | 6")
  print(board[6] + " | " + board[7] + " | " + board[8] + "     7 | 8 | 9")
  print("\n")

def play_game(): 
  #Displays the initial board 
  display_board()

  while game_still_going: 


    handle_turn(current_player)

  
    check_if_game_over()
    #flips to opposite player
    flip_player()
  
  #The game has ended
  if winner == "X" or winner == "O":
    print(winner + " won!")
  elif winner == None:
   print("The game is a tie.")



def handle_turn(current_player):
  print(current_player + "'s turn")
  position=input("Choose a number between 1 - 9:  ")

  valid = False
  while not valid:
    
    while position not in ["1", "2", "3", "4","5", "6", "7", "8",'9']:
      position = input("That input is not compatible. Please try a number between 1 - 9")
        
    position = int(position) - 1

    if board[position] == "-":
      valid = True
    else:
      print("That isn't a valid move; please try again.")


  board[position] = current_player

  display_board()

def check_if_game_over():
  check_if_game_win()
  check_if_game_tie()



def check_if_game_win():
  # Set global variables
  global winner
  # Check if there was a winner anywhere
  row_winner = check_rows()
  column_winner = check_columns()
  diagonal_winner = check_diagonals()
  # Get the winner
  if row_winner:
    winner = row_winner
  elif column_winner:
    winner = column_winner
  elif diagonal_winner:
    winner = diagonal_winner
  else:
    winner = None
  

def check_rows():
  #--Global Variable--
  global game_still_going
  #In order to check rows, create a new variable and check to see if all the indexes are equal to one another excluding the "-" sign
  row_1 = board[0] == board[1] == board[2] != "-"
  row_2 = board[3] == board[4] == board[5] != "-"
  row_3 = board[6] == board[7] == board[8] != "-"
  #Ends the game if a win occurs via rows
  if row_1 or row_2 or row_3:
    game_still_going = False
  #hh
  if row_1:
    return board[0]
  elif row_2: 
    return board[3]
  elif row_3: 
    return board[6]
  
  
  return

def check_columns():
  #--Global Variable--
  global game_still_going
  #In order to check rows, create a new variable and check to see if all the indexes are equal to one another excluding the "-" sign
  column_1 = board[0] == board[3] == board[6] != "-"
  column_2 = board[1] == board[4] == board[7] != "-"
  column_3 = board[2] == board[5] == board[8] != "-"
  #Ends the game if a win occurs via rows
  if column_1 or column_2 or column_3:
    game_still_going = False

  if column_1:
    return board[0]
  elif column_2: 
    return board[1]
  elif column_3: 
    return board[2]
  
  return 

def check_diagonals():
  #--Global Variable--
  global game_still_going
  #In order to check rows, create a new variable and check to see if all the indexes are equal to one another excluding the "-" sign
  diagonals_1 = board[0] == board[4] == board[8] != "-"
  diagonals_2 = board[6] == board[4] == board[2] != "-"

  #Ends the game if a win occurs via rows
  if diagonals_1 or diagonals_2:
    game_still_going = False

  if diagonals_1:
    return board[0]
  elif diagonals_2: 
    return board[6]
  
  return


def check_if_game_tie():
  #GLOBAL VARIABLE
  global game_still_going
  if "-" not in board:
    game_still_going = False
  return


def flip_player():
  #GLOBAL VARIABLES 
  global current_player
  #Changes current player based on who made the previous decision
  if current_player == "X":
    current_player = "O"
  elif current_player == "O":
    current_player = "X"
  return 





play_game()
