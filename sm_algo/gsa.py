#!/usr/bin/ python

class GSA():
	""" Gale-Shapley (Stable Marriage) Algorithm """
	def __init__(self, setA, setB):
		self.a = setA
		self.b = setB
		
	'''
	Algorithm to compute matched pairs 
	'''	
	def Marriage(self):
		# match will contain matched pair
		# matched = [ [from_set_a], [from_set_b] ]
		matched = []

		# unmatched will contain unmatched items from set b
		unmatched = []

		# compute the match for set a and b
		"""
			for set a (for set b, just replace a with b)
			quality = self.a[i].mbr.minDim
			require = self.a[i].child.data
			id = self.a[i].mbr.child.id
		"""


		# for now
		if len(self.a) <= len(self.b):
			matched.append(self.a)
			matched.append(self.b[:len(self.a)])
			unmatched = self.b[len(self.a):]
		else:
			matched.append(self.a[:len(self.b)])
			matched.append(self.b)
			unmatched = self.a[len(self.b):]

		return [matched, unmatched] 
