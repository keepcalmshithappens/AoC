lowerCase = "abcdefghijklmnopqrstuvwxyz"
upperCase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def mainpt1(): 
    f = open("day3data.txt")
    file = f.readlines()
    comp1 = []
    comp2 = []
    sum = 0
    for line in file:
        compartment = int((len(line)-1)/2)
        compLen = compartment
        for char in line:
            if char.strip() == "":
                continue
            elif compartment > 0: 
                comp1.append(char.strip())
                compartment -= 1
            else: 
                comp2.append(char.strip())
        sum += calc(comp1, comp2, compLen)
        comp1 = []
        comp2 = []
    print("pt1: ", sum)


def mainpt2():
    f = open("day3data.txt")
    file = f.readlines()
    elf0 = []
    elf1 = []
    elf2 = []
    sum = 0
    compartment0=0
    compartment1=0
    compartment2=0
    elfCounter = 0
    for line in file:
        if elfCounter >2:
            elfCounter = 0
        for char in line:
            if char.strip() == "":
                continue
            elif elfCounter == 0:
                elf0.append(char.strip())
                compartment0 = int((len(line)-1))
            elif elfCounter == 1: 
                elf1.append(char.strip())
                compartment1 = int((len(line)-1))

            elif elfCounter == 2:
                elf2.append(char.strip())
                compartment2 = int((len(line)-1))
        if elfCounter == 2:
            sum += calcpt2(elf0, elf1, elf2, compartment0, compartment1, compartment2)
            elf0 = []
            elf1 = []
            elf2 = []
        elfCounter += 1
    print("pt2: ", sum)


def calcpt2(elf0, elf1, elf2, compLen1, compLen2, compLen3):
    for char in range(compLen1):
        for char2 in range(compLen2):
            for char3 in range(compLen3):
                if elf0[char] == elf1[char2]:
                    if elf0[char] == elf2[char3]:
                        return priorityType(elf0[char])


def calc(comp1, comp2, compLen):
    for char in range(compLen):
        for char2 in range(compLen):
            if comp1[char] == comp2[char2]:
                return priorityType(comp1[char])


def priorityType(priorityChar):
    for char in range(len(upperCase)): 
        if lowerCase[char] == priorityChar:
            return 1 + char
        elif upperCase[char] == priorityChar:
            return 27 + char


mainpt2() 
mainpt1()