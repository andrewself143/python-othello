import tkinter
import new_logic
import point

_BACKGROUND_COLOR = '#3996cc'
_DEFAULT_FONT = ('Helvetica', 20)

class startMenu:

	def __init__(self):
		self._root_window=tkinter.Tk()

		self._game_rows=''
		self._game_cols=''
		self._game_first_player=''
		self._game_upper_left=''
		self._game_win_con=''

		self._invalid_message= tkinter.StringVar()
		self._invalid_message.set('')
		self._invalid=tkinter.Label(
			master=self._root_window,textvariable=self._invalid_message
			,font= _DEFAULT_FONT)

		_game=tkinter.Label(
			master=self._root_window, text='Start An Othello Game.',
			font=_DEFAULT_FONT)


		_num_rows=tkinter.Label(
			master=self._root_window, text= 'Rows: ',
			font= _DEFAULT_FONT)

		self._row_response=tkinter.Entry(
			master=self._root_window, width=20, font=_DEFAULT_FONT)

		_num_columns=tkinter.Label(
			master=self._root_window, text='Columns: ',
			font= _DEFAULT_FONT)

		self._col_response=tkinter.Entry(
			master=self._root_window, width=20, font=_DEFAULT_FONT)

		_first_player=tkinter.Label(
			master=self._root_window, text='First Player: ',
			font=_DEFAULT_FONT)

		self._first_player=tkinter.IntVar()

		self._player_response=tkinter.Frame(master=self._root_window)

		self._black_response=tkinter.Radiobutton(
			master=self._player_response, text='Black', variable=self._first_player,
			value=1)

		self._white_response=tkinter.Radiobutton(
			master=self._player_response, text='White', variable=self._first_player,
			value=2)

		self._black_response.grid(row=0,column=0)
		self._white_response.grid(row=0,column=1)

		_upper_left=tkinter.Label(
			master=self._root_window, text='Upper Left Disc: ',
			font=_DEFAULT_FONT)

		self._topleft_player=tkinter.IntVar()

		self._upleft_response=tkinter.Frame(master=self._root_window)

		self._black1_response=tkinter.Radiobutton(
			master=self._upleft_response, text='Black', variable=self._topleft_player,
			value=1)

		self._white1_response=tkinter.Radiobutton(
			master=self._upleft_response, text='White', variable=self._topleft_player,
			value=2)

		self._black1_response.grid(row=0,column=0)
		self._white1_response.grid(row=0,column=1)

		_win_con=tkinter.Label(
			master=self._root_window, text='Win Condition: ',
			font=_DEFAULT_FONT)

		self._wincon_player=tkinter.IntVar()

		self._wincon_response=tkinter.Frame(master=self._root_window)

		self._black2_response=tkinter.Radiobutton(
			master=self._wincon_response, text='>', variable=self._wincon_player,
			value=1)

		self._white2_response=tkinter.Radiobutton(
			master=self._wincon_response, text='<', variable=self._wincon_player,
			value=2)

		self._black2_response.grid(row=0,column=0)
		self._white2_response.grid(row=0,column=1)

		_make_button=tkinter.Button(master=self._root_window, text='Make Game',
									command = self._on_make_button)

		_game.grid(row=1, column=0, sticky=tkinter.W+tkinter.N + tkinter.S)
		_num_rows.grid(row=2, column=0, sticky=tkinter.W+tkinter.N + tkinter.S)
		_num_columns.grid(row=3, column=0, sticky=tkinter.W+tkinter.N + tkinter.S)
		_first_player.grid(row=4, column=0, sticky=tkinter.W+tkinter.N + tkinter.S)
		_upper_left.grid(row=5, column=0, sticky=tkinter.W+tkinter.N + tkinter.S)
		_win_con.grid(row=6, column=0, sticky=tkinter.W+tkinter.N + tkinter.S)
		self._row_response.grid(row=2, column=1, sticky=tkinter.W+tkinter.N + tkinter.S)
		self._col_response.grid(row=3, column=1, sticky=tkinter.W+tkinter.N + tkinter.S)
		self._player_response.grid(row=4, column=1, sticky=tkinter.W+tkinter.N + tkinter.S)
		self._upleft_response.grid(row=5, column=1, sticky=tkinter.W+tkinter.N + tkinter.S)
		self._wincon_response.grid(row=6, column=1, sticky=tkinter.W+tkinter.N + tkinter.S)
		_make_button.grid(row=7, column=0, sticky=tkinter.W+tkinter.N + tkinter.S)
		self._invalid.grid(row=0, column=0, columnspan=2,sticky=tkinter.W+tkinter.N+tkinter.S)


		self._root_window.rowconfigure(0, weight= 1)
		self._root_window.rowconfigure(1, weight=1)
		self._root_window.rowconfigure(2, weight= 1)
		self._root_window.rowconfigure(3, weight= 1)
		self._root_window.rowconfigure(4, weight=1)
		self._root_window.rowconfigure(5, weight= 1)
		self._root_window.rowconfigure(6, weight= 1)
		self._root_window.columnconfigure(0, weight=1)
		self._root_window.columnconfigure(1, weight= 1)

	def _on_make_button(self)-> None:
		'Gets information and creates Othello game from setting window'
		self._game_rows=self._row_response.get()
		self._game_cols=self._col_response.get()


		if (self._first_player.get()==1):
			self._game_first_player='B'
		if (self._first_player.get()==2):
			self._game_first_player='W'

		if (self._topleft_player.get()==1):
			self._game_upper_left='B'
		if (self._topleft_player.get()==2):
			self._game_upper_left='W'

		if (self._wincon_player.get()==1):
			self._game_win_con='>'
		if (self._wincon_player.get()==2):
			self._game_win_con='<'

		while True:
			if self.is_entries_valid():
				game=new_logic.game_state(self._game_rows,
					self._game_cols,self._game_first_player,self._game_upper_left
				   ,self._game_win_con)

				game.startPositions()
				board=OthelloGame(game)
				board.drawBoard()
				board.drawCircles()
				board.start()
				return
			else:
				self._root_window.destroy()
				newgame=startMenu()
				newgame._invalid_message.set('Rows and Columns must be even integers between 4 and 16')
				newgame.run()
				return



	def is_entries_valid(self)->bool:
		'Determines if the rows and columns are acceptable'
		try:
			self._game_rows=int(self._game_rows)
		except:
			return False
		try:
			self._game_cols=int(self._game_cols)
		except:
			return False
		if not (self._game_rows%2==0):
			return False
		if not (self._game_cols%2==0):
			return False
		if not (4<=self._game_rows<=16):
			return False
		if not (4<=self._game_cols<=16):
			return False
		return True


	def run(self)->None:
		'Runs the loop on the start menu and waits to create game'
		print('hello')
		self._root_window.mainloop()
	

class OthelloGame:

	def __init__(self, game: new_logic.game_state):

		self._game=game

		self._root_window= tkinter.Toplevel()

		self._count=0

		self._valid_text= tkinter.StringVar()
		self._valid_text.set('')
		self._valid=tkinter.Label(
			master=self._root_window,textvariable=self._valid_text
			,font= _DEFAULT_FONT)

		self._valid.grid(row=2, column=1, sticky=tkinter.E+tkinter.N+tkinter.S)

		self._turn_text= tkinter.StringVar()

		self._turn_text.set('Turn: {}'.format(self.turn()))


		self._score= tkinter.StringVar()
		self._score.set('Black: {} White: {}'.format(game.getBlacks(),game.getWhites()))




		_full=tkinter.Label(
			master=self._root_window, text='FULL', font=_DEFAULT_FONT)

		_full.grid(row=0, column=1, sticky=tkinter.E+tkinter.N+tkinter.S)

		self._turn_label=tkinter.Label(
			master=self._root_window, textvariable= self._turn_text,
			font = _DEFAULT_FONT)

		self._turn_label.grid(row=0, column=0,
			sticky=tkinter.W+tkinter.N+tkinter.S)

		self._score_label=tkinter.Label(
			master=self._root_window, textvariable= self._score,
			font = _DEFAULT_FONT)

		self._score_label.grid(row=2, column=0,
			sticky=tkinter.W+tkinter.S+tkinter.N)


		self._game_canvas=tkinter.Canvas(
			master = self._root_window,
			width = 600, height = 600,
			background = _BACKGROUND_COLOR)

		self._game_canvas.grid(row=1, column=0,columnspan = 2,
			sticky= tkinter.N + tkinter.S + tkinter.W + tkinter.E)

		self._game_canvas.bind('<Configure>', self._on_canvas_resized)
		self._game_canvas.bind('<Button-1>', self._on_canvas_clicked)


		self._root_window.rowconfigure(1, weight= 1)
		self._root_window.columnconfigure(0, weight=1)
		self._root_window.columnconfigure(1, weight= 1)

	def _on_canvas_resized(self, event: tkinter.Event)->None:
		'Redraws board once its resized'
		self._game_canvas.delete(tkinter.ALL)
		self.drawBoard()
		self.drawCircles()

	def _on_canvas_clicked(self, event: tkinter.Event) -> None:
		'Makes the move depending on where the board was clicked'
		width = self._game_canvas.winfo_width()
		height = self._game_canvas.winfo_height()

		click_point = point.from_pixel(
			event.x, event.y, width, height)

		move= self.pixelToIndex(click_point)
		row, col=move

		moves= self._game.iter_flipped(self._count, row, col)
		if (len(moves)>0):
			self._game.make_move(self._count,row,col)
			self._game.flip_pieces(moves, self._count)
			self.drawCircles()
			if self._game.game_over():
				self.end_scenario()
				self._score.set('Black: {} White: {}'.format(self._game.getBlacks(),self._game.getWhites()))
				self._valid_text.set('')
			if self._game.has_move(self._count+1):
				self.add()
				self._turn_text.set('Turn: {}'.format(self.turn()))
				self._score.set('Black: {} White: {}'.format(self._game.getBlacks(),self._game.getWhites()))
				self._valid_text.set('')

		else:
			if not self._game.won:
				self._valid_text.set('INVALID MOVE')

	def end_scenario(self)->None:
		'Ends the game'
		self._turn_text.set('Winner: {}'.format(self._game.winner()))
		self._game.won=True

	def add(self)->None:
		'Adds the count to keep track of turns'
		self._count= self._count+1

	def pixelToIndex(self, p: point.Point)->(int,int):
		'Given point, returns board index'
		frac_x, frac_y= p.frac()
		xfracs= self.getXfracs()
		yfracs= self.getYfracs()

		col=0
		row=0

		for num in range(len(xfracs)-1):
			if xfracs[num] < frac_x < xfracs[num+1]:
				col= num

		for num in range(len(yfracs)-1):
			if yfracs[num] < frac_y < yfracs[num+1]:
				row= num

		return (row, col)

	def getXfracs(self)-> [float]:
		'Creates a list of x points to draw board'
		points=[]
		for x in range(self._game.columns+1):
			num= (x)/(self._game.columns)
			points.append(num)
		return points

	def getYfracs(self)->[float]:
		'Creates a list of y points to draw board'
		points=[]
		for x in range(self._game.rows+1):
			num= (x)/(self._game.rows)
			points.append(num)
		return points


	def drawBoard(self)->None:
		'Draws the grid'
		canvas_width=self._game_canvas.winfo_width()
		canvas_height=self._game_canvas.winfo_height()
		xpoints= self.getXfracs()
		ypoints= self.getYfracs()

		for x in xpoints:
			cur_point=x*canvas_width
			self._game_canvas.create_line(cur_point, 0, cur_point, canvas_height)

		for y in ypoints:
			cur_point=y*canvas_height
			self._game_canvas.create_line(0, cur_point, canvas_width, cur_point)

	def drawCircles(self)->None:
		'Draws the board'
		xfracs= self.getXfracs()
		yfracs= self.getYfracs()
		for row in range(self._game.rows):
			for col in range(self._game.columns):
				if self._game.board[row][col]==1:
					x1= xfracs[col]
					y1= yfracs[row]
					x2= xfracs[col+1]
					y2= yfracs[row+1]
					self.makeBlackCircle(x1,y1,x2,y2)

				if self._game.board[row][col]==2:
					x1= xfracs[col]
					y1= yfracs[row]
					x2= xfracs[col+1]
					y2= yfracs[row+1]
					self.makeWhiteCircle(x1,y1,x2,y2)

	def makeBlackCircle(self, x1,y1,x2,y2)->None:
		'Draws a black circle'
		canvas_width=self._game_canvas.winfo_width()
		canvas_height=self._game_canvas.winfo_height()
		x1=x1*canvas_width
		x2=x2*canvas_width
		y1=y1*canvas_height
		y2=y2*canvas_height
		self._game_canvas.create_oval(x1,y1,x2,y2, fill='black')

	def makeWhiteCircle(self, x1,y1,x2,y2)->None:
		'Draws a white circle'
		canvas_width=self._game_canvas.winfo_width()
		canvas_height=self._game_canvas.winfo_height()
		x1=x1*canvas_width
		x2=x2*canvas_width
		y1=y1*canvas_height
		y2=y2*canvas_height
		self._game_canvas.create_oval(x1,y1,x2,y2, fill='white')

	def turn(self)->str:
		'Determines the turn'
		if self._game.getTurn(self._count)==2:
			return ('White')
		else:
			return ('Black')

	def start(self)->None:
		'Runs the game'
		self._root_window.grab_set()
		self._root_window.wait_window()

if __name__=='__main__':
	print('hello')
	startMenu().run()
