import random

#tries to test this will be constant for all
#tries = int(input("tries: "))
tries = 100000

counter = 0
stake = {"TradeAnytimeZero":0.09,"resetStake":0.09}

balance = {"TradeAnytimeZero":1000.00}

wins =    {"TradeAnytimeZero":0}
looses = {"TradeAnytimeZero":0}
OOBtries = {"TradeAnytimeZero":0}

#perc = {"0":0,"0on0":0,"perc000":0}

#PIP
newPIPvalue = 0
oldPIPvalue = 0
PIPfile = open("pips","w")

returnperc = 0.098

showText = False

#generate a new pip
def NewPIP():
    global newPIPvalue
    global oldPIPvalue
    global stake
    oldPIPvalue = newPIPvalue
    newPIPvalue = random.randint(0,9)
    PIPfile.write(str(newPIPvalue))
    if showText == True:
        print("PIP",newPIPvalue)

def TradeAnytimeZero():
    #if the balance is enought to cover the stake
    global newPIPvalue
    global counter
    if showText == True:
        print("TradeAnytimeZero balance before trading: ",round(balance["TradeAnytimeZero"],2))
    balance["TradeAnytimeZero"] -= round(stake["TradeAnytimeZero"],2)
    # Loose
    if  newPIPvalue == 0:
        looses["TradeAnytimeZero"] += 1
        if showText == True:
            print("Lost: ",round(stake["TradeAnytimeZero"],2))
        # increase stake by 10
        stake["TradeAnytimeZero"] = round(stake["TradeAnytimeZero"] * 10,2)
        if showText == True:
            print("TradeAnytimeZero balance after trading: ",round(balance["TradeAnytimeZero"],2))
    # Win
    else:
        wins["TradeAnytimeZero"] += 1
        balance["TradeAnytimeZero"] += round(stake["TradeAnytimeZero"]+(stake["TradeAnytimeZero"]*returnperc),2)
        if showText == True:
            print("Won: ", round(stake["TradeAnytimeZero"]*returnperc,2))
            print("TradeAnytimeZero balance after trading: ",round(balance["TradeAnytimeZero"],2))
        stake["TradeAnytimeZero"] = stake["resetStake"]

while counter < tries:
    NewPIP()
    if balance["TradeAnytimeZero"] > stake["TradeAnytimeZero"]:
        TradeAnytimeZero()
        OOBtries["TradeAnytimeZero"] = counter
        
    counter += 1
    if showText == True:
        print("\n")
PIPfile.close()
print("----------------------------------------------------------------")
print("TradeAnytimeZero")
print("final balance : ",balance["TradeAnytimeZero"])
print("tries before OOB",OOBtries["TradeAnytimeZero"]+1)
print("times won: ",wins["TradeAnytimeZero"])
print("times lost: ",looses["TradeAnytimeZero"])
print("percentage lost",looses["TradeAnytimeZero"]/tries*100,"%")
print("----------------------------------------------------------------")
