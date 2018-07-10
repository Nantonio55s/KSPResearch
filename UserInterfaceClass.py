# User Interface Class:
# Author: Antonio Cruz
# Creation date: July,9,2018
# A user interface class that presents the graph and info of the selected and calculated network to the user.
# This class will update the graph network whenever the user changes the parameters of the network, as to display them
# real time. The class will also allow for the saving of the information in two files, one for the network graph and
# one with the values of the network graph, such as the shortest path, the reliability between the nodes and the paths
# with the highest reliability
import Tkinter as TKin


class UserInterface:

	def __init__(self, graph, reliability):
		self.graph = graph
		self.reliability = reliability
		self.graph.name = graph.name

	def make_window(self):
		window = TKin.Tk()

		l1 = TKin.Label(window, text="Selected Network")
		l1.grid(row=0, column=0)
		l1 = TKin.Label(window, text=self.graph.name)
		l1.grid(row=0, column=1)
		l1 = TKin.Label(window, text="Reliability Factor")
		l1.grid(row=1, column=0)
		l1 = TKin.Label(window, text=self.graph.reliability)
		l1.grid(row=1, column=1)
		l1 = TKin.Label(window, text="# of Nodes")
		l1.grid(row=2, column=0)
		l1 = TKin.Label(window, text=self.graph.node_amt)
		l1.grid(row=2, column=1)
		l1 = TKin.Label(window, text="# of Links ")
		l1.grid(row=3, column=0)
		l1 = TKin.Label(window, text=self.graph.link_amt)
		l1.grid(row=3, column=1)

		# variables to be shown

		window.mainloop()
