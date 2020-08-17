EMPTY= 0
BLACK=1
WHITE=2

class WrongRow(Exception):
	'Raised with a non-existant row'
	pass

class WrongColumn(Exception):
	'Raised with an non-existant column'
	pass

class game_state:

	def __init__(self, numRows: int, numCols: int, firstMove: str,
				 topLeftDisc: str, winCondition: str):
		game_state.won= False
		game_state.rows= numRows
		game_state.columns= numCols
		game_state.turn= firstMove
		game_state.topLeft= topLeftDisc
		game_state.winCon= winCondition
		game_state.board=[]
		for x in range(game_state.rows):
			game_state.board.append([])
		for element in game_state.board:
			for y in range(game_state.columns):
				element.append(0)

	def startPositions(self)->None:
		'Initializes the board to have the correct starting position'
		topRow= int((self.rows/2)-1)
		bottomRow= int((self.rows/2))
		leftColumn= int((self.columns/2)-1)
		rightColumn= int((self.columns/2))
		if self.topLeft == 'B':
			self.board[topRow][leftColumn]=1
			self.board[topRow][rightColumn]=2
			self.board[bottomRow][rightColumn]=1
			self.board[bottomRow][leftColumn]=2
		if self.topLeft == 'W':
			self.board[topRow][leftColumn]=2
			self.board[topRow][rightColumn]=1
			self.board[bottomRow][rightColumn]=2
			self.board[bottomRow][leftColumn]=1

	def getBlacks(self)->int:
		'Returns the number of black pieces on the board'
		numBlacks=0
		for x in self.board:
			for y in x:
				if y==1:
					numBlacks +=1
		return numBlacks

	def getWhites(self)->int:
		'Returns the number of black pieces on the board'
		numWhites=0
		for x in self.board:
			for y in x:
				if y==2:
					numWhites +=1
		return numWhites

	def getTurn(self, count_iteration: int)->int:
		'Determines if its black\'s or white\'s turn'
		if self.turn== 'B':
			if (count_iteration%2==0):
				return 1
			if (count_iteration%2==1):
				return 2
		if self.turn=='W':
			if (count_iteration%2==0):
				return 2
			if (count_iteration%2==1):
				return 1

	def otherPiece(self, count)->int:
		'Returns the integer of the opposite team'
		if self.getTurn(count)==1:
			return 2
		if self.getTurn(count)==2:
			return 1


	def make_move(self, count_iteration: int,
			   row_input: int, col_input: int)-> None:
		'Drops a piece on the board'
		self.board[row_input][col_input]=self.getTurn(count_iteration)

	def iter_flipped(self, count_iter:int, row: int, col:int)->[(int,int)]:
		'Returns a list of pieces that should be flipped, given a move'
		self._need_valid_col(col)
		self._need_valid_row(row)
		if self.board[row][col]!=EMPTY:
			return []
		pieces=[]
		directs= [[0,1],[1,0],[0,-1],[-1,0],[1,1],[1,-1],[-1,1],[-1,-1]]
		for element in directs:
			pieces.extend(self._list_flipped(element, row, col, count_iter))
		return (pieces)

	def _list_flipped(self, direction: [int], row: int, col: int, count_iter: int)->[(int,int)]:
		'Finds pieces that should be flipped given a direction'
		flipped=[]

		if (self._valid_col(col+direction[1]) and self._valid_row(row+direction[0])):

			if self.board[row+direction[0]][col+direction[1]] != self.otherPiece(count_iter):

				return []
		n=1
		while True:
			if not (self._valid_col(col+direction[1]*n)and self._valid_row(row+direction[0]*n)):
				return []
			if self.board[row+direction[0]*n][col+direction[1]*n] == EMPTY:
				return []
			if self.board[row+direction[0]*n][col+direction[1]*n] == self.getTurn(count_iter):
				for x in range(1,n):
					flipped.append(((row+direction[0]*x),(col+direction[1]*x)))

				return flipped
			#searches for cell to end chain of not cells
			n+=1
		return flipped

	def flip_pieces(self, pieces: [(int, int)], count)->None:
		'Flips pieces given a list'
		for element in pieces:
			row= element[0]
			col= element[1]
			self.board[row][col] = self.getTurn(count)

	def has_move(self, count: int)->bool:
		'Returns whether or not a player has a valid move'
		for row in range(self.rows):
			for col in range(self.columns):
				if len(self.iter_flipped(count, row, col))>0:
					return True
		return False

	def game_over(self)-> bool:
		'returns true when neither player has a move'
		return not(self.has_move(0) or self.has_move(1))

	def winner(self)->None:
		'Prints out the winner'
		winner= ''
		if self.getWhites()== self.getBlacks():
			winner = 'NONE'
		if self.winCon =='>':
			if (self.getWhites()> self.getBlacks()):
				winner = 'White'
			if (self.getBlacks()> self.getWhites()):
				winner= 'Black'
		if self.winCon == '<':
			if (self.getWhites()< self.getBlacks()):
				winner = 'White'
			if (self.getBlacks()< self.getWhites()):
				winner= 'Black'
		return winner


	def _need_valid_row(self, row_num: int)-> None:
		if type(row_num) != int or not self._valid_row(row_num):
			raise WrongRow('row must be int between 1 and {}'.format(self.rows))

	def _need_valid_col(self, col_num: int)-> None:
		if type(col_num) != int or not self._valid_col(col_num):
			raise WrongColumn('row must be int between 1 and {}'.format(self.columns))

	def _valid_col(self, col_num:int)->bool:
		'Determins if a column being checked is valid'
		return 0<=col_num<self.columns

	def _valid_row(self, row_num: int)->bool:
		'Determines if a row being checked is valid'
		return 0<=row_num<self.rows

def _addColor( color: int)->str:
	'Adds color to integers'
	if color== EMPTY:
		return '.'
	if color== BLACK:
		return 'B'
	if color== WHITE:
		return 'W'
