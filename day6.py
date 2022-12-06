f = open("day6data.txt")
file = f.readlines()

def pt1(): 
    i=0
    charList = []
    pt2 = []
    counter =0
    for line in file: 
        for char in line: 
            counter += 1
            if i<4: 
                charList.append(char)
            if i<14: 
                pt2.append(char)
                i+=1
            else: 
                pt2.pop(0)
                pt2.append(char)
                charList.pop(0)
                charList.append(char)                
                #if not checkList(charList):
                #    return counter
                if not checkList(pt2):
                    return counter

                

def checkList(li):
    copy = li.copy()
    if len(li) == 1: 
        return False
    for i in range(len(copy)-1): 
        i+=1
        if copy[0] is copy[i]:
            return True
    copy.pop(0)
    return checkList(copy) 
        


print(pt1())