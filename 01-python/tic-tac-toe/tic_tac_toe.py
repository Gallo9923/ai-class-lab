import re
import random
_PLAYER = "player"
_MACHINE = "machine"

_PLAYER_SYMBOL = "x"
_MACHINE_SYMBOL = "o"

class TicTacToeGame():
  def __init__(self):
    self.board = [None] * 9
    self.turn = _PLAYER
    self.is_game_over = False
    self.winner = None

  def is_won_by_rows(self, turn):
    won = True
    for i in range(0, len(self.board), 3):
      won = True
      for i in range(i, i + 3):
        if self.board[i] != turn:
          won = False
          break
      if won == True:
        break
    return won

  def is_won_by_columns(self, turn):
    won = True
    for i in range(3):
      won = True
      for j in range(i, len(self.board), 3):
        if self.board[j] != turn:
          won = False
          break
      if won == True:
        break
    return won

  def is_won_by_diagonals(self, symbol):
    won_by_left_diagonal = False
    if self.board[0] == symbol and self.board[4] == symbol and self.board[8] == symbol:
      won_by_left_diagonal = True

    won_by_right_diagonal = False
    if self.board[2] == symbol and self.board[4] == symbol and self.board[6] == symbol:
      won_by_right_diagonal = True

    return won_by_left_diagonal or won_by_right_diagonal

  def is_over(self):  # TODO: Finish this function by adding checks for a winning game (rows, columns, diagonals)
    symbol = _PLAYER_SYMBOL if self.turn == _MACHINE else _MACHINE_SYMBOL
    won = self.is_won_by_rows(symbol) or self.is_won_by_columns(symbol) or self.is_won_by_diagonals(symbol)

    if won == True and symbol == _PLAYER_SYMBOL:
      self.winner = _PLAYER
    elif won == True and symbol == _MACHINE_SYMBOL:
      self.winner = _MACHINE

    return won

  def play(self):
    if self.turn == _PLAYER:
      self.player_turn()
      self.turn = _MACHINE
    else:
      self.machine_turn()
      self.turn = _PLAYER

  def player_choose_cell(self):
    print("Input empty cell bewtween 0 and 8")

    player_cell = input().strip()
    match = re.search("\d", player_cell)

    if not match:
      print("Input is not a number, please try again")

      return self.player_choose_cell()

    player_cell = int(player_cell)

    if self.board[player_cell] is not None:
      print("Cell is already taken, try again")

      return self.player_choose_cell()

    return player_cell

  def player_turn(self):
    chosen_cell = self.player_choose_cell()

    self.board[chosen_cell] = _PLAYER_SYMBOL

  def machine_turn(self):
    # TODO: Implement this function to make the machine choose a random cell (use random module)
    # The result of this function should be that self.board now has one more random cell occupied
    unoccupied_spaces = []
    for i in range(0, len(self.board)):
      if self.board[i] == None:
        unoccupied_spaces.append(i)

    play_cell = random.choice(unoccupied_spaces)
    self.board[play_cell] = _MACHINE_SYMBOL

    #for i, cell in enumerate(self.board):
    # if cell is None:
    #   self.board[i] = _MACHINE_SYMBOL
    #   break

  def format_board(self):
    # TODO: Implement this function, it must be able to print the board in the following format:
    #  x|o| 
    #   | | 
    #   | |
    board = ""
    for i in range(0, len(self.board), 3):
      for j in range(0, 3):
        symbol = " " if self.board[i+j] == None else self.board[i+j]
        if j == 1:
          board += "|" + symbol + "|"
        else:
          board += symbol
      board += "\n"
    return board

  def print(self):
    print("Player turn:" if self.turn == _MACHINE else "Machine turn:")
    print(self.format_board())
    print()

  def print_result(self):
    # TODO: Implement this function in order to print the result based on the self.winner
    print("========================= \n" +
          "The winner is: " + self.winner + "\n" +
          "=========================\n" +
          self.format_board())
    pass
