# Read File Class:
# Author: Antonio Cruz
# Creation date: June,19,2018
# The read file class has a function named read_file
# that takes the given file and creates a list to represent a network graph.
# The file must be formatted in the following way
# Source Destination Distance
# Ex:  1  4  52.32
# every line will be a different link
# Ej. Link 1
# 1  2  3.54
# Link 2
# 3  2  4.56
# and so on
# the file must be in .txt extension in order to be read properly


# import the Node class
from NodeClass import Node


# main function of the class
def read_file(filename):

    # opens the file in read mode
    # count the lines in the file
    line_count = len(open(filename).readlines())
    r_file = open(filename)
#  line_count += 1

# Node structure initialization: next_node,nnode_weight,prev_node,pnode_weight,curr_node

    # defines list of nodes
    nodelist = []

    # defines list of node names
    node_name = "Node"

    namelist = [node_name]

    # defines list name as needed by the file
    [namelist.append(node_name+str(i)) for i in range(1, 11)]

    # reads a line in the file, it splits it and stores the values in the nodes

    i = 0
    line_read = []
    while i < line_count:

        with open(filename) as fp:
            for line in fp:
                line_read.append(line)

        line_read[i] = line_read[i].split("\t")
        line_read[i][2] = line_read[i][2].split("\n")
        #print line_read[i]
        # creates a new node that stores the values
        nodelist.append(Node(int(line_read[0][0]), int(line_read[0][1]), float(line_read[0][2][0]), 0, 0))

        # defines the previous node info based on the previous values
        #nodelist[i].name = namelist[i]

        # if its reading the source node, skip this step
        # if i == 0:
        #   continue

        # if its not reading the source node, store values in Node
        #        else:
        #   print("hello there")
        # nodelist.append(namelist[i])
        i += 1
        print nodelist[0].dec_print()
        print nodelist[1].dec_print()
    # closes the file
    r_file.close()

    return nodelist
