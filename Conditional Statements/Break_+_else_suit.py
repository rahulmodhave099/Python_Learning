# Break Statement

x = 10
while(x > 0):
    print(x)
    x -= 1
    if(x == 5):
        break;



playerList = ["Rohit","Shubhman","Virat","Ayyar","KLRahul","SKYadav","Jadeja"]

playerName = input("Enter Player Name : ")
cnt = 0
for player in playerList:
    cnt += 1
    if(player == playerName):
        print(playerName,"present in list")
        break

else:
    print(playerName,"is not present in list")

