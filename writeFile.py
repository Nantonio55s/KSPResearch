# Write file Class:
# Author: Antonio Cruz
# Creation date: June,19,2018
# This class creates a file with the name given, and stores in it the data of the KSP's of the selected network,
# based on the reliability selected and the network selected. It also stores the network data  so it can be re-used.
# The files will be stored in .txt format so it can be reused with this program.


# creates a file that stores the reliable network
def write_file_r(filename, r_list):
	# creates the file
	f = open(filename+"RelNetwork.txt", "w+")
	i = 0
	while i < len(r_list):
		f.write(r_list[i][0] + " " + r_list[i][1] + " " + r_list[i][2] + " " + "\r\n")
	f.close()


# creates a file that stores the network
def write_file_n(filename, n_list):
	f = open(filename + "Network.txt", "w+")
	i = 0
	while i < len(n_list):
		f.write(n_list[i][0] + " " + n_list[i][1] + " " + n_list[i][2] + "\r\n")
	f.close()
