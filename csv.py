# Authors:
# uniqnames:
# Date:
# Purpose:
# Description:

import sys

def parseCSVFile(fileName):
	"""
	This function reads in a CSV file and stores the values therein in a
	dictionary. The key in the key-value pair is one of the entries in the
	table, and the value is a list of the entries (which are themselves lists)
	associated with that value in the table.
	
	For the purposes of the bare-bones, the key is the name of the storm, and
	the values stored in the list are as follows:
	name, date, time, system_status, lat, lon, wind, pressure
	The types of these values for the purposes of grading of core functionality
	are:
	str, str, str, str, float, float, int, int
	
	When you are writing your own function to read in your specific file, you
	can set the types to whatever you see fit.
	
	For the purposes of your extension, you will need to modify this code so
	that it works for your data set. You can decide what the key and values are,
	but make sure you choose your key wisely.
	
	In any event, this function will return the dictionary that is built by
	parsing the CSV file.
	
	Requires: fileName contains the name of the CSV file
	Modifies: nothing
	Effects: See the above.
	"""
	pass


def retrieveValue(dictionary, key, entry):
	"""
	This function retrieves an entry from the list of entries in the dictionary
	for a given key and position in the list for the key.
	
	Requires: dictionary is the dictionary built in parseCSVFile, key is the
	key from which we want to fetch values, and entry is the index of the
	entry we wish to fetch
	
	Modifies: nothing
	Effects: retrieves a single entry from the list of entries in the dictionary
		such that entry holds the position in the list of entries, and that key
		is the key from which we wish to fetch it
	"""
	pass


"""
Requires: dictionary holds a dictionary created by parseCSVFile
	columnNo holds the index of the attribute we wish to create a list from
Modifies: nothing
Effects: returns a list of the values in the column specified by columnNo
"""
def retrieveEntireAttribute(dictionary, columnNo):
	pass

# DO NOT modify these 2 lines of code or you will be very sad
# Similarly, do not place any code below them
if __name__ == "__csv__":
	main(sys.argv)