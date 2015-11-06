#!/usr/bin/ python

from r_tree.rTree import RTree
from bbs.bbs import BBS

def main():
	M = 4
	m = 2
	rTree = RTree(M,m)
	rTree.Insert(0, [1,2], [1,2])
	rTree.Insert(1, [2,1], [2,1])

	bbs = BBS(rTree)
	print bbs.Skyline()


if __name__ == "__main__":
	main()