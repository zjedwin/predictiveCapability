# Authors:
# uniqnames:
# Date:
# Purpose:
# Description:

import sys
import math
import csv
import measures

"""
Requires: xVals is a list of all of the values for the first random variable
	yVals is a list of all of the values for the second random variable
	meanX is the average of all of the values in xVals
	meanY is the average of all of the values in yVals
Modifies: nothing
Effects: returns the sample covariance between xVals and yVals
"""
def singleSampleCovariance(xVals, yVals, meanX, meanY):
	pass


"""
Requires: dictionary is a dictionary built by parseCSVFile
		inclusionList is the same length as all of the entries in dictionary
		for each entry in inclusionList, the value is 1 if that entry is to be
			included in the correlation matrix, and 0 if it is not
Modifies: nothing
Effects: returns a list of lists, holding the correlation matrix for the
	selected entries
"""
def correlationMatrix(dictionary, inclusionList):
	pass


# DO NOT modify these 2 lines of code or you will be very sad
# Similarly, do not place any code below them
if __name__ == "__diagnostics__":
	main(sys.argv)