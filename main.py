import urllib.request


def findLastSpace(name):
    firstSpace = name.find(" ")
    while name.find(" ", firstSpace + 1) != -1:
        firstSpace = name.find(" ", firstSpace + 1)

    return firstSpace


def getFirstName(name):
    name = name[:findLastSpace(name)]
    while name.find(".") != -1:
        name = name[:name.find(".")] + name[name.find(".") + 1:]
    while name.find("'") != -1:
        name = name[:name.find("'")] + name[name.find("'") + 1:]
    while name.find(" ") != -1:
        name = name[:name.find(" ")] + name[name.find(" ") + 1:]
    return name

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
    elif playerName.__contains__("Gheorghe"):
        playerName = "Gheorghe Muresan"
    seasonWon += 1
    if seasonWon == 100:
        seasonWon = 0
    MIPDict[playerName] = seasonWon
    tableBegin = postPlayer + 20
    i += 1

for player in MIPDict:
    if MIPDict[player] < 10:
        MIPDict[player] = "0" + str(MIPDict[player])
    else:
        MIPDict[player] = str(MIPDict[player])

bbref = "https://www.basketball-reference.com"
URLEnd = ""
URLDict = {}
for player in MIPDict:
    URLEnd = "/players/" + player[findLastSpace(player)+1] + "/" + player[findLastSpace(player) + 1:findLastSpace(player) + 6] + getFirstName(player)[:2] + "01.html"
#    playerPage = str(urllib.request.urlopen(bbref + URLEnd).read())
#    preURLEnd = playerPage.find("/players",playerPage.find(player) - 50)
#    postURLEnd = playerPage.find(".html", preURLEnd) + 5
#    URLEnd = playerPage[preURLEnd:postURLEnd]
    URLEnd = URLEnd.lower()
    URLDict[player] = bbref + URLEnd


print(URLDict)




