# Edge Class class:
# Author: Antonio Cruz
# Creation date: June,21,2018
# Class made to store the edge info of the network graph.
# It is a subclass of the Node Class and it is used to store data that relates to the edge

# Imports the superclass
from NodeClass import Node


class Edge(Node):

	def __init__(self, weight, reliability, accident ):

		super().__init__(self,curr_node, next_node)
		self.weight = weight
		self.reliability = reliability
		self.accident = accident


	def dec_print(self):
		print("The link is between the following nodes: ")
		print(self.curr_node, self.next_node)
		print("The link weight is: ")
		print(self.weight)
		print("The link's reliability factor is: ")
		print(self.reliability)
		print("The link's accident factor is: ")
		print(self.accident)