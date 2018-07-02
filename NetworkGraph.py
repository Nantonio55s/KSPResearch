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
	def print_graph(self,graph_list,reliable_graph):
		glen=graph_list.len
		G=nx.Graph()
		i=0
		while i<reliable_graph.len:
			G.add_edge(reliable_graph[i].curr_node, reliable_graph[i].next_node)



