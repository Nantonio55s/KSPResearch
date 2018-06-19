# K-Shortest-Path and Network viewer
# Author: Antonio Cruz
# This code is divided mainly in 2 parts:
# I.) A K-shortest path function based on the Dijkstra algorithm
# II.) Graph Network modeling and analysis
#
#
# I. A KSP algorithm determines the amount(K) of shortest paths given from a source node to a destination node
#    Most KSPs are based in the Dijkstra algorithm
#    For this project, the KSP algorithm has been altered so it can also be applied to areas inside the links,
#    This means that the KSP can determine the distance from either Node to Node, or from Node to a specified Point in the link
#
# II.
#
#
#
from listClass import List
C=2
P=1
N=3
PW=5
NW=7

blist= List(3,7,1,5,2)

blist.print()
