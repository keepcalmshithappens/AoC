f = open("day4data.txt")
file = f.readlines()

def pt1(): 
    counter = 0
    pt2Counter = 0
    for line in file: 
        a = ""
        a=line.strip()
        b = (elfSplit(a))    
        if (b[0] <= b[2] and b[1] >= b[3]) or (b[0] >= b[2] and b[1] <= b[3]): 
            counter +=1
        if pt2(b): 
           pt2Counter += 1
    print("counter pt 1: ", counter, "counter pt2: ", pt2Counter)


def pt2(b):
    idLenOne = b[1] - b[0]
    elfOne = [b[0]]
    elfTwo = [b[2]]
    idLenTwo = b[3] - b[2]
    for i in range (idLenOne): 
        elfOne.append(b[0]+i+1)
    for i in range (idLenTwo): 
        elfTwo.append(b[2]+i+1)
    if b[2] in elfOne or b[3] in elfOne or b[0] in elfTwo or b[1] in elfTwo:

        return True
    else: 
        print("false", elfOne)
        return False 


def elfSplit(id): 
    start = ""
    zero = ""
    lista = []
    for num in id: 
        if num == "-" or num == "," : 
            lista.append(int(start))
            start = zero
            continue
        start += num
    lista.append(int(start))
    return lista

pt1()
