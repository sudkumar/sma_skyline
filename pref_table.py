#!/usr/bin/python


# Create a preference table for men and women and return
def pref_table(menDataFileName, womenDataFileName, queryFileName):
    # get query options from queryfile
    queryFile = open(queryFileName, "r")
    # get the dimensions for quality and requirements
    aQDims, aRDims = map(int, queryFile.readline().split())
    queryFile.close()

    # score list of men for each woman (listIndex = man.id)
    menScoreList = []
    # score list for women for each man (listIndex = man.id)
    womenScoreList = []


    with open(menDataFileName, "r") as menData:
        for man in menData:
            # get the quality and requirement for man
            manSplit = man.split()
            manId = int(manSplit[0])
            manQuality =  map(int, manSplit[1:aQDims+1])
            manRequirements = map(float, manSplit[aQDims+1:])
            womanScoreList = []
            manScoreList = []
            with open(womenDataFileName, "r") as womenData:
                for woman in womenData:
                    # get the quality and requirement for woman
                    womanSplit = woman.split()
                    womanId = int(womanSplit[0])
                    womanQuality =  map(int, womanSplit[1:aRDims+1])
                    womanRequirements = map(float, womanSplit[aRDims+1:])

                    # calculate the score
                    womanScoreList.append([manId, float( "%.3f" % sum([ a*b for a,b in zip(manRequirements, womanQuality)]))])
                    manScoreList.append([womanId, float( "%.3f" % sum([a*b for a,b in zip(womanRequirements, manQuality)]))])


            # append the manScoreList to menScoreList
            menScoreList.append(manScoreList)
            # append the womanScoreList to womenScoreList
            womenScoreList.append(womanScoreList)

    # arrange the womenScoreList so that key for each list is a women id
    womenScoreList = zip(*womenScoreList)


    # men and women score list without any sorting
    # print "Without Sorting"
    # print menScoreList
    # print womenScoreList

    # print "-------"

    # sort each list item in menScoreList and womenScoreList to get the rank 
    menRankList = []
    womenRankList = []
    for i in range(len(menScoreList)):
        rankList = []
        # sort the items with score as key
        afterSort = sorted(menScoreList[i],reverse=True,key=lambda x: x[1])
        [rankList.append(item[0]) for item in afterSort]
        menRankList.append(rankList)
        menScoreList[i] = afterSort

    for i in range(len(womenScoreList)):
        rankList = []
        # sort the items with score as key
        afterSort = sorted(womenScoreList[i],reverse=True,key=lambda x: x[1])
        [rankList.append(item[0]) for item in afterSort]
        womenRankList.append(rankList)
        womenScoreList[i] = afterSort

    # men and women after sorting
    # print "Men and Women after sorting"
    # print menScoreList
    # print womenScoreList
    # print "---------"

    # only ranks
    # print "Only ranks"
    # print menRankList
    # print womenRankList

    return [menRankList, womenRankList]

if __name__ == '__main__':
    # get the rank of all women for each man and of all men for each woman
    menRankList, womenRankList =  pref_table("aData.txt", "bData.txt", "query.txt")
    print menRankList, womenRankList
