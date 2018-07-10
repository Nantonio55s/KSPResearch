# Network Graph class:
# Author: Antonio Cruz
# Creation date: June,21,2018
# Class made to represent the network graph of the given network
# and to represent the k-shortest paths chosen from the source point
# given R the reliability factor
# Uses NetworkX and MatPlotLib modules

import networkx as nx
import matplotlib.pyplot as plt


class NetworkGraph:

	def __init__(self, graph_list, reliable_graph):
			self.graph_list = graph_list
			self.reliable_path = reliable_graph

	def print_graph(self):
		# glen = self.graph_list.len
		g = nx.Graph()
		i = 0
		while i < self.reliable_graph.len:
			g.add_edge(self.reliable_graph[i].curr_node, self.reliable_graph[i].next_node)

