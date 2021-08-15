from read_file import *
R = {
    "R0" : 1,
    "R1" : 0,
    "R2" : 0,
    "R3" : 0,
    "R4" : 0,
    "R5" : 0,
    "R6" : 0,
    "R7" : 0,
    "R8" : 0,
    "R9" : 0,
    "R10" : 0,
    "R11" : 0,
    "R12" : 0,
    "v"  : 0,
    "E"  : 0,
    "G"  : 0,
    "L"  : 0,
    "Error" : 0,
}

labels={}

var = {}

def stringtobinary_8bit(string):
    n = int(string)
    num = 0
    answer = ""
    while n != 0:
        if n % 2 == 1:
            answer += "1"
        else:
            answer += "0"
        n //= 2
    size = len(answer)
    value = "0"*(8-size)
    answer = answer[::-1]
    value += answer
    return value

def validreg(string):
    if int(string[1:])<=12:
        return True
    return False

def debug(temp):
    for i in temp.keys():
        print(i +": "+ str(R[i]))

def BinaryToDecimal(binary):
    decimal = 0
    for digit in binary: 
        decimal = decimal*2 + int(digit) 
    return decimal

def DecimalToBinary(num):
    if num >= 1:
        DecimalToBinary(num // 2)
    print(num % 2, end = '')

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

## sparsh was here:
def add(R1,R2,R3):
    if(validreg(R1) and validreg(R2) and validreg(R3)):
        R[R1] = R[R2]+R[R3]
        print("0000000"+stringtobinary(R1[1:])+stringtobinary(R2[1:])+stringtobinary(R3[1:]))
    else:
        R["Error"]= 1
        print("Invalid Register")



def sub(R1, R2, R3):
    
    if(validreg(R1) and validreg(R2) and validreg(R3)):
        #print("FUNC REAcHED")
        R[R1] = R[R2]-R[R3]
        if(R[R1]<0):
            R["V"] =1
            R[R1]=0
        print("0000100"+stringtobinary(R1[1:])+stringtobinary(R2[1:])+stringtobinary(R3[1:]))
    else:
        R["Error"]= 1
        print("Invalid Register")

def multiply(R1,R2,R3):
    if(validreg(R1) and validreg(R2) and validreg(R3)):
        imm = R[R2]*R[R3]
        R[R1] = R[R2]*R[R3]
        print("0011000"+stringtobinary(R1[1:]) +stringtobinary(R2[1:])+stringtobinary(R3[1:]))
    else:
        R["Error"]= 1
        print("Invalid Register")

def xor(R1,R2,R3):
    if(validreg(R1) and validreg(R2) and validreg(R3)):
        R[R1] = R[R1]^R[R2]
        print("0101000"+stringtobinary(R1[1:]) +stringtobinary(R2[1:])+stringtobinary(R3[1:]))
    else:
        R["Error"]= 1
        print("Invalid Register")

def OR(R1,R2,R3):
    if(validreg(R1) and validreg(R2) and validreg(R3)):
        R[R1] = (R[R1])|(R[R2])
        print("0101000"+stringtobinary(R1[1:]) +stringtobinary(R2[1:])+stringtobinary(R3[1:]))
    else:
        R["Error"]= 1
        print("Invalid Register")

def AND(R1,R2,R3):
    if(validreg(R1) and validreg(R2) and validreg(R3)):
        R[R1] = R[R1]&R[R2]
        print("0101000"+stringtobinary(R1[1:]) +stringtobinary(R2[1:])+stringtobinary(R3[1:]))
    else:
        R["Error"]= 1
        print("Invalid Register")

## rahul add here: done
def move_imm(R1,imm):
    if(validreg(R1)):
        if imm<0 or imm>255:
            R["Error"] = 1
            return
        R[R1] = imm
        print("00010"+stringtobinary(R1[1:])+stringtobinary_8bit(imm))
    else:
        R["Error"]= 1
        print("Invalid Register")

# def load(R1,mem_add):
#     R[R1] = mem_add[0]
#     print("00100"+stringtobinary(R1[1:])+stringtobinary(mem_add[0]))

# def store(R1,mem_add):
#     mem_add[0] = R[R1]
#     print("00101"+stringtobinary(R1[1:])+stringtobinary(mem_add[0]))

def unconditionaljump(mem_add):
    print("01111"+ stringtobinary(mem_add))
    return True


def jumpiflessthan(mem_add):
    if R["L"]==1:
        return True
    print("10000"+ stringtobinary(mem_add))
    return False
    

def jumpifgreaterthan(mem_add):
    if R["G"]==1:
        return True
    print("10001"+ stringtobinary(mem_add))
    return False

def jumpifequalto(mem_add):
    if R["E"]==1:
        return True
    print("10010"+ stringtobinary(mem_add))
    return False

def right_shift(R1,imm):
    if(validreg(R1)):
        if imm<0 or imm>255:
            R["Error"] = 1
            return

        x = R[R1]
        for i in range(imm):
            x*=2
        R[R1]= x
        print("01000"+stringtobinary(R1[1:])+stringtobinary(imm))
    else:
        R["Error"]= 1
        print("Invalid Register")

def left_shift(R1,imm):
    if(validreg(R1)):
        if imm<0 or imm>255:
            R["Error"] = 1
            return
        x = R[R1]
        for i in range(imm):
            x/=2
        R[R1]= x
        print("01000"+stringtobinary(R1[1:])+stringtobinary(imm))
    else:
        R["Error"]= 1
        print("Invalid Register")

## sahas add here: ok
# C
# Performs reg1 = reg2
def MoveRegister(rx, ry):
    if(validreg(rx) and validreg(ry)):
        R[rx] = R[ry]
        print('0001100000' + stringtobinary(rx[1:]) + stringtobinary(ry[1:]))
    else:
        R["Error"]= 1
        print("Invalid Register")

# Performs reg3/reg4 Stores the quotient in R0 and the remainder in R1.
def Divide(rx, ry):
    if(validreg(rx) and validreg(ry)):
        R["R0"] = R[rx]//R[ry]
        R["R1"] = R[rx]%R[ry]
        print('00111' + stringtobinary(rx[1:]) + stringtobinary(ry[1:]))
    else:
        R["Error"]= 1
        print("Invalid Register")

# Performs bitwise NOT of reg2. Stores the result in reg1.
def Invert(rx, ry):
    # string = "101"
    if(validreg(rx) and validreg(ry)):
        string = bin(R[ry][2:])
        n = len(string)
        answer=""
        for i in range(n):
            if string[i]=="1":
                answer+="0"
            else:
                answer+="1"
        print('0110100000'+ stringtobinary(rx[1:])+ stringtobinary(ry[1:]))
    else:
        R["Error"]= 1
        print("Invalid Register")

def stringtodecimal(string):
    n = len(string)
    num = 0
    for i in range(n):
        num*=2
        if string[i]=="1":
            num+=1
    return num
    print(stringtodecimal(answer))

# Compares reg1 and reg2 and sets up the FLAGS register.
def Compare(rx, ry):
    if R[rx] > R[ry]:
        G = 1
    elif R[rx] < R[ry]:
        L = 1
    elif R[rx] == R[ry]:
        E = 1
    print('01110' + stringtobinary(rx[1:]) + stringtobinary(ry[1:]))

#D
# Loads data from mem_addr into reg1.
def Load(rx, memaddr):
    R[rx] = memaddr
    print('00100' + stringtobinary(rx[1:]) + stringtobinary(memaddr))

# Stores data from reg1 to mem_addr.
def Store(rx, memaddr,i):
    if not(memaddr in var.keys()):
        print("variable doesnt exist")
        R["Error"]=1
        return
    print('00101' + stringtobinary(rx[1:]) + stringtobinary_8bit(str(i)))
    var[memaddr] = R[rx]

def check_label(line,i):
    temp = line.split(":")
    if len(temp)==2:
        labels[temp[0]] = i
        return True
    return False    

def storevar(variable):
    if variable in var.keys():
        print("Variable already defined")
        R["Error"] = 1
    else:
        var[variable]=0

fullcode=[]

for line in list_of_instructions:
    temp = line
    #print(type(temp))
    if temp == "hlt":
      break
    islabel = check_label(temp, len(fullcode))
    temp.split(":")
    #print(temp)
    if(temp == ""):
      continue
    if islabel:
      fullcode.append(temp.split()[1:])
    else:
      fullcode.append(temp.split())

#print(fullcode)
curIndex = 0
while(True):
    if curIndex == len(fullcode):
        print("1001100000000000")
        break
    currentcode = fullcode[curIndex]
    curIndex += 1
    print(currentcode)
    if(len(currentcode) == 0):
        continue
    if(currentcode[0]=="hlt"):
        print("1001100000000000")
        break
    if(currentcode[0]=="var"):
        storevar(currentcode[1])
    elif(currentcode[0]=="add"):
        if(len(currentcode)==4):
            add(currentcode[1], currentcode[2], currentcode[3])
        else:
            print("404 ERROR")
            print("1001100000000000")
            break
    elif(currentcode[0]=="sub"):
        if(len(currentcode) == 4):
            sub(currentcode[1], currentcode[2], currentcode[3])
        else:
            print("404 ERROR")
            print("1001100000000000")
            break
    elif(currentcode[0]=="mul"):
        if(len(currentcode) == 4):
            multiply(currentcode[1], currentcode[2], currentcode[3])
        else:
            print("404 ERROR")
            print("1001100000000000")
            break
    elif(currentcode[0]=="xor"):
        if(len(currentcode) == 4):
            xor(currentcode[1], currentcode[2], currentcode[3])
        else:
            print("404 ERROR")
            print("1001100000000000")
            break
    elif(currentcode[0]=="or"):
        if(len(currentcode) == 4):
            OR(currentcode[1], currentcode[2], currentcode[3])
        else:
            print("404 ERROR")
            print("1001100000000000")
            break
    elif(currentcode[0]=="and"):
        if(len(currentcode) == 4):
            AND(currentcode[1], currentcode[2], currentcode[3])
        else:
            print("404 ERROR")
            print("1001100000000000")
            break
    elif(currentcode[0] == "mov"):
        if currentcode[2][0] == '$':
            move_imm(currentcode[1],int(currentcode[2][1:]))
        else:
            MoveRegister(currentcode[1], currentcode[2])
    elif currentcode[0]=="st":
        Store(currentcode[1], currentcode[2], curIndex)
    elif(currentcode[0] == 'div'):
        Divide(currentcode[1], currentcode[2])
    elif(currentcode[0] == 'not'):
        Invert(currentcode[1], currentcode[2])
    elif(currentcode[0] == 'cmp'):
        Compare(currentcode[1], currentcode[2])
    elif(currentcode[0] == 'rs'):
        right_shift(currentcode[1], int(currentcode[2][1:]))
    elif(currentcode[0] == 'ls'):
        left_shift(currentcode[1], int(currentcode[2][1:]))      
    elif(R["Error"]==1):
        print("1001100000000000")
        break
    else:
        print("kuch to gabdab hai daya")
        break
        #debug()

