#!/usr/bin/ python
"""
Data file generator for our algorithm
Create file for both A and B set with given arguments

usages: python data.py <rows> <aQDims> <aRDims>
rows:		number of rows in data file
aQDims:	length of dimensions for qualities in data set A
aRDims:	length of dimensions for requirements in data set B
"""

import random
import sys
import getopt

def dumpData(fileHandle, rows, qualityCols, requireCols):
	for row in range(rows):
		# scaling quality from 1 to 10
		tupleData = [row+1]
		for i in range(qualityCols):
			tupleData.append(random.randrange(1,10))

		maxRequire = 1
		for i in range(requireCols-1):
			val = float("%.1f" % random.uniform(0, maxRequire) )
			tupleData.append(val)
			maxRequire -= val
		tupleData.append(abs(float("%.1f" % maxRequire)))
		# put tuple in data file
		line = " ".join(map(str, tupleData))+"\n"
		fileHandle.write(line)

def main(argv=None):
	if argv is None:
		argv = sys.argv
  # parse command line options
	try:
		opts, args = getopt.getopt(argv[1:], "h", ["help"])
	except getopt.error, msg:
		print msg
		print "for help use --help"
		sys.exit(2)
  # process options
	for o, a in opts:
		if o in ("-h", "--help"):
			print __doc__
			sys.exit(0)
  # process arguments
	if len(args) == 3:
		# get the number of rows for data file
		rows = int(args[0])

		# get quality dimension for set A, which 
		# also gives require dimesion of set B
		aQDims = int(args[1])
		
		# get require dimensions for set A, which
		# also gives 	quality dimension for set B	
		aRDims = int(args[2])
	else:
		print "Program requires 3 args..."
		print "for help use --help"
		sys.exit(2)


	

	# dump data into file for set A
	aDataFile = open("aData.txt","w")
	dumpData(aDataFile, rows, aQDims, aRDims)
	aDataFile.close()

	# dump data into file for set B
	bDataFile = open("bData.txt", "w")
	dumpData(bDataFile, rows, aRDims, aQDims)
	bDataFile.close()

	# now create the query file 
	queryFile = open("query.txt", "w")
	queryFile.write(str(aQDims)+" "+str(aRDims)+"\n")
	queryFile.write(str(2048)+"\n")
	queryFile.write(str(4)+" "+str(12)+"\n")
	queryFile.close()

if __name__ == "__main__":
	main()