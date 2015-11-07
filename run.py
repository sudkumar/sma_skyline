#!/usr/bin/ python

from r_tree.rTree import RTree
from bbs.bbs import BBS
from sm_algo.gsa import GSA
import threading


# fill data into RTree from fileHandle with given dimensions
def fillRTree(rTree, fileName, qualityDims, requireDims):
	fileHandler = open(fileName, "r")
	for line in fileHandler:
		row = line.split()
		id = int(row[0])
		mbrDim = map(int, row[1:qualityDims+1])
		sateliteData = map(float, row[qualityDims+1:])
		
		# create key with given data 
		key = rTree.MakeKey(mbrDim, id, sateliteData)
		# insert key into rTree
		rTree.Insert(key)

	fileHandler.close()

lock = threading.Lock()

# print the matched pairs
def printMatched(matched, skyFile):
	setA = matched[0]
	setB = matched[1]

	for i in range(len(setA)):
		a = str(setA[i].child.id)
		# +" " +' '.join(map(str, setA[i].mbr.minDim + setA[i].child.data))  
		b = str(setB[i].child.id)
		# +" " + ' '.join(map(str, setB[i].mbr.minDim + setB[i].child.data )) 
		lock.acquire() 
		skyFile.write( a + " <> " + b + "\n") 
		lock.release()

# main function 
def main():
	
	# get query options from queryfile
	queryFile = open("query.txt", "r")
	# get the dimensions for quality and requirements
	aQDims, aRDims = map(int, queryFile.readline().split())

	# get page size
	pageSize = int(queryFile.readline())

	# get size of pointers and keys
	prtSize, keySize = map(int, queryFile.readline().split())

	# close the query file
	queryFile.close()

	# calculate max and min size allowed for a node
	M = pageSize/(prtSize + keySize)
	m = M/2

	# create RTree instance for set A and B
	rTreeA = RTree(M, m)
	rTreeB = RTree(M, m)

	# fill data into trees with there corresponding data files  
	fillRTree(rTreeA, "aData.txt", aQDims, aRDims)
	fillRTree(rTreeB, "bData.txt", aRDims, aQDims)


	bbsA = BBS(rTreeA)
	bbsB = BBS(rTreeB)

	threads = []

	skyFile = open("skyline.txt", "w")

	while not rTreeA.IsEmpty() or not rTreeB.IsEmpty():
		# compute skylines for both sets	
		skylinesA, comparisionsA = bbsA.Skyline()
		skylinesB, comparisionsB = bbsB.Skyline()

		gsa = GSA(skylinesA, skylinesB)
		matched, unmatched = gsa.Marriage()


		# print the matched result
		# printMatched(matched, skyFile)
		thread = threading.Thread(target=printMatched, args=[matched, skyFile])
		threads.append(thread)
		thread.start()

		matchedA = matched[0]
		matchedB = matched[1]

		# remove matched key from trees
		for key in matchedA:
			rTreeA.Delete(key)
		for key in matchedB:
			rTreeB.Delete(key)


	# wait for all thread to print
	for thread in threads: 
		thread.join()	

	skyFile.close()

	# everything is done till this point

if __name__ == "__main__":
	main()