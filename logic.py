# Step 1: import the following modules
import random
from copy import deepcopy

# Step 2: Create a Game class
class Game:
    # Inialize the player, computer and board
    def __init__(self, player = 'o', computer = 'x'):
        self.player = player
        self.computuer = computer
        self.board = [' ',' ',' ',' ',' ',' ',' ',' ',' ']
        
    # Returns a copy of the board to experiment on
    def board_copy(self):
        return deepcopy(self.board)
    
    # Returns True if a particular position in the board is empty
    def position_empty(self,pos):
        if (self.board[pos] == ' '):
            return True
        else:
            return False
    
    # Returns a list of possible moves
    def get_possible_moves(self):
        moves= []
        for i in range(len(self.board)):
            if (self.position_empty(i)):
                moves.append(i)
        return moves
    
    # Returns true if the board is full
    def is_board_full(self):
        for i in range(0, len(self.board)):
            if (self.board[i] == ' '):
                return False
        return True
    
    # Returns the winning combination or returns False
    def has_won(self,board, mark):
        # Horizontal Win
        if board[0] == board[1] and board[0] == board[2] and board[0] == mark:
            return [[0,1,2]]
        elif board[3] == board[4] and board[3] == board[5] and board[3] == mark:
            return [[3,4,5]]
        if board[6] == board[7] and board[6] == board[8] and board[6] == mark:
            return [[6,7,8]]
        
        # Vertical Win
        elif board[0] == board[3] and board[0] == board[6] and board[0] == mark:
            return [[0,3,6]]
        elif board[1] == board[4] and board[1] == board[7] and board[1] == mark:
            return [[1,4,7]]
        if board[2] == board[5] and board[2] == board[8] and board[2] == mark:
            return [[2,5,8]]
        
        # Diagonal Win
        elif board[0] == board[4] and board[0] == board[8] and board[0] == mark:
            return [[0,4,8]]
        elif board[2] == board[4] and board[2] == board[6] and board[2] == mark:
            return [[2,4,6]]
        else:
            return False
        