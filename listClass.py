class List:

    def __init__(self, next_node,nnode_weight,prev_node,pnode_weight,curr_node):

    # next node stores the number assigned to the next node
        self.next_node=next_node
    # nnode weight stores the value between current node and the next node
        self.nnode_weight = nnode_weight
    # prev node stores the number assigned to the prev node
        self.prev_node = prev_node
    # pnode weight stores the value between current node and the previous node
        self.pnode_weight = pnode_weight
    # curr node stores the number assigned to the current node
        self.curr_node=curr_node

    def print(self):
        print("Current node: ")
        print(self.curr_node)
        print("Previous node: ")
        print (self.prev_node)
        print("Distance between current node and previous node: ")
        print(self.pnode_weight)
        print("Next node: ")
        print(self.next_node)
        print("Distance between current node and next node: ")
        print(self.nnode_weight)