R1 = 0
R2 = 0
R3 = 0
R4 = 0
R5 = 0
R6 = 0
OVERFLOW = 0
EQUAL = 0
GREATERTHAN = 0
LESSTHAN = 0
def stringtobinary(string):
    returnstring="000"
    num = int(string)
    ##print(num-1)
    temp=""
    while(num>0):
        temp+= str(num%2)
        num/=2
        num = int(num)
    ##print(temp)
    for i in range(len(temp)):
        returnstring+=temp[len(temp)-i-1]
    #print(returnstring[-3:])
    return returnstring[-3:]
def add(R1,R2,R3):
    ##print(R1[1:]+" "+R2[1:])
    print("0001000"+stringtobinary(R1[1:])+stringtobinary(R2[1:])+stringtobinary(R3[1:]))

def sub(R1, R2, R3):
    
    print("0010000"+stringtobinary(R1[1:]) +stringtobinary(R2[1:])+stringtobinary(R3[1:]))

if __name__ == "__main__":
    while(True):
        currentcode =input().split()
        ##print(currentcode)
        if(currentcode[0]=="hlt"):
            print("1001100000000000")
            break
        if(currentcode[0]=="add"):
            ##print("add statement")
            add(currentcode[1], currentcode[2], currentcode[3])
        if(currentcode[0]=="sub"):
            sub(currentcode[1], currentcode[2], currentcode[3])


