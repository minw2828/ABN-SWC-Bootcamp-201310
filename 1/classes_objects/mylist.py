# for the purpose of learning class inheritance

class MyList(list): # my class starts from list
	def reverse_sort(self):
		self.sort()
		self.reverse()
