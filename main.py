import urllib.request

wikipedia = str(urllib.request.urlopen("https://en.wikipedia.org/wiki/NBA_Most_Improved_Player_Award").read())
tableBegin = wikipedia.find("86 NBA season\">")
MIPDict = {}
seasonWon = 85
i = 0
while i < 33:
    prePlayer = wikipedia.find("\">",wikipedia.find("</a></span></span></span>", tableBegin) - 40) + 2
    postPlayer = wikipedia.find("</a>", prePlayer)
    playerName = wikipedia[prePlayer:postPlayer]
    if playerName.__contains__("x87"):
        playerName = "Goran Dragic"
    elif playerName.__contains__("xbcrko"):
        playerName = "Hedo Turkoglu"
    seasonWon += 1
    if seasonWon == 100:
        seasonWon = 0
    MIPDict[playerName] = seasonWon
    tableBegin = postPlayer + 20
    i += 1

print(MIPDict)




