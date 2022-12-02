#ugly code
def main(): 
    #Part 1
    file = openFile()
    allLines = file.readlines()
    points = 0
    newScore = 0
    for line in allLines: 
        points = points + getPoints(line)
        newScore = newScore + getPoints2(line)
    print(points)
    print(newScore)

# X means you need to lose, Y means you need to 
# end the round in a draw, and Z means you need to win.

def getPoints2(line): 
    points = 0
    match line[2]:
        case "X": points = defe(line[0])
        case "Y": points = 3 + draw(line[0])
        case "Z": points = 6 + win(line[0])
        case _: print( "error")
    return points  

def defe(opp):
    match opp:
        case "A": return 3 
        case "B": return 1
        case "C": return 2 
        case _: print( "error")

def draw(opp):
    match opp:
        case "A": return 1 
        case "B": return 2
        case "C": return 3 
        case _: print( "error")

def win(opp):
    match opp:
        case "A": return 2 
        case "B": return 3
        case "C": return 1 
        case _: print( "error")


def openFile(): 
    file = open("day2data.txt")
    if file.readable: 
        return file


# Line[0] = ABC, Line[2]n= XYZ
# A,x = rock; B,Y = paper; C,Z = scissors


def getPoints(line): 
    points = 0
    match line[2]:
        case "X": points = 1 + winnerX(line[0])
        case "Y": points = 2 + winnerY(line[0])
        case "Z": points = 3 + winnerZ(line[0])
        case _: return "error"
    return points
    


def winnerX(opp):
    if opp == "A": 
        return 3
    if opp == "B":
        return 0
    if opp == "C": 
        return 6

def winnerY(opp): 
    if opp == "A": 
        return 6
    if opp == "B":
        return 3
    if opp == "C": 
        return 0

def winnerZ(opp):
    if opp == "A": 
        return 0
    if opp == "B":
        return 6
    if opp == "C": 
        return 3



main()
