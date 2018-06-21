# KSP Algorithm class:
# Author: Antonio Cruz
# Creation date: June,19,2018
# Class made to run the KSP algorithm needed for the research
# given R the reliability factor and chosen source node.
# Based on the Dijkstra algorithm.

class KSP:
    from NodeClass import Node
    def __init__(self,source,next_node,next_weight,):
        self.source=source
        self.next_node=next_node
        self.next_weight=next_weight

#Dijkstra
    def Dijkstra(self,graph, source):
        #Onode=List(next,next_node,nnode_weight,prev_node,pnode_weight,curr_node)
        nodenum=10
        i=0
        #while i<nodenum**2:





