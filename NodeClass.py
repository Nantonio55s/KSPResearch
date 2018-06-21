# Node Class:
# Author: Antonio Cruz
# Creation date: June,19,2018
# A node class that will store all the info of the nodes and links to be used in the KSP and network graph.
# It stores the current node name, next and previous node names, and the weight in the links between the nodes.
# It also stores the accident and reliability factor of each node.
#


class Node:

    def __init__(self, curr_node, next_node, weight, reliability, accident ):

        # next node stores the number assigned to the next node
        self.next_node = next_node
        # next node weight stores the value between current node and the next node
        self.curr_node = curr_node
        # stores the reliability factor of the node
        self.reliability = reliability
        # stores the weight of the edge
        self.weight = weight
        # stores the accident factor of the edge
        self.accident = accident
        self.name="Node"

    def dec_print(self):
        print("The node's name is: ")
        print(self.name)
        print("Current node: ")
        print(self.curr_node)
        print("Next node: ")
        print(self.next_node)
        print("The link is between the following nodes: ")
        print(self.curr_node, self.next_node)
        print("The link weight is: ")
        print(self.weight)
        print("The link's reliability factor is: ")
        print(self.reliability)
        print("The link's accident factor is: ")
        print(self.accident)