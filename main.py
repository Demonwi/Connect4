class GameBoard:
	def __init__(self):
		self.c4Board = [[0 for x in range(7)] for y in range(6)]
	def printboard(self):
		for row in self.c4Board:
			print("|", end = "")
			for col in row:
				if col < 10:
					print(" ", end = "")
				print(col, end = "")
				print("|", end = "")
			print()
	def rowcalc(self):
		for x in range(4):
			for y in range(6):
				for nx in range(4):
					self.c4Board[y][x + nx] += 1
		return
	def colcalc(self):
		for x in range(7):
			for y in range(3):
				for ny in range(4):
					self.c4Board[y+ny][x] += 1
		return
	def rightdiacalc(self):
		for x in range(4):
			for y in range(3):
				for nz in range(4):
					self.c4Board[y+nz][x+nz] += 1
		return
	def leftdiacalc(self):
		for x in range(3,7):
			for y in range(3):
				for nz in range(4):
					self.c4Board[y+nz][x-nz] += 1
		return
	def calc(self):
		self.rowcalc()
		self.colcalc()
		self.rightdiacalc()
		self.leftdiacalc()
		return

gb = GameBoard()
gb.calc()
gb.printboard()