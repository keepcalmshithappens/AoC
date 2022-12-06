f = open("day5data.txt")
file = f.readlines()
linee = f.readline()


def pt1(): 
    stack = getStacks()
    instruction = instructions()
    top = []  
    for line in instruction: 
        for i in line: 
            destination = line[2]
            takeOff = line[1]
            ammount = line[0]
        d = list(stack[takeOff])
        for i in range(ammount):
            stack[destination].append(d.pop())
        stack[takeOff] = d
    for i in range(9):
        i+=1
        lista = list(stack[i])
        top.append(lista.pop())
    print(top)
        

def pt2():
    instruction = instructions()
    stack = getStacks()
    top = []  
    for line in instruction: 
        for i in line: 
            destination = line[2]
            takeOff = line[1]
            ammount = line[0]
        d = list(stack[takeOff])
        a = []
        for i in range(ammount):
            a.append(d.pop())
        if ammount != 1:
            a.reverse()
        for i in range(len(a)):
            stack[destination].append(a[i])
        stack[takeOff] = d
    for i in range(9):
        i+=1
        lista = list(stack[i])
        top.append(lista.pop())
    print(top)
        


def instructions():
    instruction = []
    hej = "move from to"
    counter = 0
    charString = "" 
    
    for line in file:
        if line[0] == "m": 
            lineInstruction = []
            for char in line: 
                if char in hej: 
                    counter = 0
                    continue
                else: 
                    if counter!=0:
                        lineInstruction.pop()
                        charString += char
                        lineInstruction.append(int(charString))
                    else:
                        lineInstruction.append(int(char))
                    charString = str(char)
                    counter += 1
            instruction.append(lineInstruction)

    return(instruction)
        



def getStacks(): 
    stackCounter =0
    stack = {}
    stackFile = []
    stackList = []
    for line in range(8):
        stackFile.append(file[line].strip())
    for line in range(9):    
        stacknr = file[line]

    for i in range(9):
        i+=1
        stack[i]=[]
    for line in stackFile: 
        for char in range(len(line)):
            if line[char] != " " and stacknr[char] != " ":
                nr = int(stacknr[char])
                character = line[char]
                stack[nr].append(character)
    for nr in range(9):
        nr+=1
        stack[nr].reverse()
    return(stack)
                

            
        




    


pt2()