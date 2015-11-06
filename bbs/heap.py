#!/usr/bin/ python

from heapq import *

class Heap():
	"""Priprity heap for Skyline"""
	def __init__(self, rootNode):
		self.heap = []
		for key in rootNode.keys:
			heappush(self.heap, (key.mbr.Priority(), key))

	'''
	remove the most priority element and returns it from heap
	'''
	def DeleteMin(self):
		return heappop(self.heap)

	'''
	inserts a node into heap
	'''
	def Enqueue(self, node):
		for key in node.keys:
			heappush(self.heap, (key.mbr.Priority(), key))


	'''
	Heap size
	'''
	def Size(self):
		return len(self.heap)