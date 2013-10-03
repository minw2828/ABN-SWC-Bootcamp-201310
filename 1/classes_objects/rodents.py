class Rodent:
	def __init__(self, tag_id):
		self.tag_id = tag_id
		self.weights = []

	def plot(self): # self will return Rodent object itself
		return self.tag_id[0]
	
	def add_weight(self, weight):
		weight = float(weight)
		self.weights.append(weight)
	
