# K-Shortest-Path and Network viewer
# Author: Antonio Cruz
# Creation date: June,19,2018
# This code is divided mainly in 2 parts:
# I.) A K-shortest path function based on the Dijkstra algorithm
# II.) Graph Network modeling and analysis
#
#
# I. A KSP algorithm determines the amount(K) of shortest paths given from a source node to a destination node
#    Most KSPs are based in the Dijkstra algorithm
#    For this project, the KSP algorithm has been altered so it can also be applied to areas inside the links,
#    This means that the KSP can determine the distance from either Node to Node, or from Node to a specified Point
#    in the link.
#
# II.
#
#
#

from NodeClass import Node
from readFile import read_file_n
# from EdgeClass import Edge

b_list = Node(2, 3, 5.2, 2.1, 1.2)
listing = read_file_n("Distance")
listing[0].dec_print()
print "OOOOOOOOOOOOOOO"
listing[0].dec_print()



