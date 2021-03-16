class Pawn:
    def __init__(self, rank, file, board, hasMoved = False):
        self.rank = rank
        self.file = file
        self.board = board
        self.hasMoved = False
        self.availableMoves = []
    
    def findAvailableMoves(self):
        if not self.hasMoved and self.rank == 1:
            if self.board[self.rank+2][self.file] == None:
                availableMoves.append( (self.rank+2, self.file) )

        if self.rank < 8:
            if self.board[self.rank+1][self.file] == None:
                availableMoves.append( (self.rank+1, self.file) )

            if self.board[self.rank+1][self.file+1] != None:
                availableMoves.append( (self.rank+1, self.file+1) )
        
            if self.board[self.rank+1][self.file-1] != None:
                availableMoves.append( (self.rank+1, self.file-1) )
    
    def move(self, rank, file):
        if (rank,file) in availableMoves:
            self.rank = rank
            self.file = file
            self.hasMoved = True                
        