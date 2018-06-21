# Node Class:
# Author: Antonio Cruz
# Creation date: June,19,2018
# A node class that will store all the info of the nodes and links to be used in the KSP and network graph.
# It stores the current node name, next and previous node names, and the weight in the links between the nodes.
# It also stores the accident and reliability factor of each node.
#


class Node:

    def __init__(self, next_node, curr_node):

        # next node stores the number assigned to the next node
        self.next_node = next_node
        # next node weight stores the value between current node and the next node
        self.curr_node = curr_node
        # r stores the reliability factor of the node

    def dec_print(self):
        print("Current node: ")
        print(self.curr_node)
        print("Next node: ")
        print(self.next_node)