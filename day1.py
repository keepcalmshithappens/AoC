
def main ():
    f = open("data.txt")
    read = f.readlines()
    #print(read)
    data = []
    lista = []
    for line in read:
        if len(line) < 2:
            lista.append(data)
            data = []
        else: 
            data.append(line.strip())
    biggest = add(lista[0])
    index = 0
    resultList= []

    for i in range(3):
        for listor in lista: 
            new = add(listor)
            if new > biggest:
                biggest = new
                
        resultList.append(biggest)
        print(biggest)
        lista = remove(lista, biggest)
        biggest = 0
    print(add(resultList))




def add(list):
    result = 0
    for cal in list:
        result = result + int(cal)
    return result

def remove(list, biggest):
    newList = []
    for i in list: 
        if add(i) == biggest: 
            print("hej")
        else: 
            newList.append(i)
    return newList



main()


