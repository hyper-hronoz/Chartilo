class Line:
	width = 8 

	def __init__(self, data):
		self.closeTime = data[0]
		self.openPrice = float(data[1])
		self.closePrice = float(data[4])
		