#!/usr/bin/python


from pref_table import pref_table


# Compute the score for simple and skyline sma and return
def computeScore(menDataFileName, womenDataFileName, queryFileName, smaFileName, smaSkyFileName):
    menRankList, womenRankList = pref_table(menDataFileName, womenDataFileName, queryFileName)

    # get the score for simple sma
    smaScore = 0
    with open(smaFileName, "r") as smaFile:
        for line in smaFile:
            manId, womanId = map(int, line.split("<>"))
            smaScore += menRankList[manId-1][womanId-1]
            smaScore += womenRankList[womanId-1][manId-1]

    # get the score for skyline sma 
    smaSkyScore = 0
    with open(smaSkyFileName, "r") as smaSkyFile:
        for line in smaSkyFile:
            manId, womanId = map(int, line.split("<>"))
            smaSkyScore += menRankList[manId-1][womanId-1]
            smaSkyScore += womenRankList[womanId-1][manId-1]

    return smaScore, smaSkyScore

if __name__ == '__main__':
    # get the score for both simple sma and skyline sma
    smaScore, smaSkyScore  =  computeScore("aData.txt", "bData.txt", "query.txt", "smaOut.txt", "smaOut_sky.txt")
    # lower the score, greater the thing
    print smaScore, smaSkyScore


