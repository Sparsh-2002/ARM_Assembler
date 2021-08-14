R = {
  "R0" : 1,
  "R1" : 0,
  "R2" : 0,
  "R3" : 0,
  "R4" : 0,
  "R5" : 0,
  "R6" : 0,
  "v"  : 0,
  "E"  : 0,
  "G"  : 0,
  "L"  : 0,
  "Error" : 0,
}

labels={}


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
def debug():
  for i in R.keys():
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
    R[R1] = R[R2]+R[R3]
    print("0000000"+stringtobinary(R1[1:])+stringtobinary(R2[1:])+stringtobinary(R3[1:]))

def sub(R1, R2, R3):
    R[R1] = R[R2]-R[R3]
    if(R[R1]<0):
      R["V"] =1
      R[R1]=0
    print("0000100"+stringtobinary(R1[1:])+stringtobinary(R2[1:])+stringtobinary(R3[1:]))

def multiply(R1,R2,R3):
    imm = R[R2]*R[R3]
    R[R1] = R[R2]*R[R3]
    print("0011000"+stringtobinary(R1[1:]) +stringtobinary(R2[1:])+stringtobinary(R3[1:]))
  
def xor(R1,R2,R3):
    R[R1] = R[R1]^R[R2]
    print("0101000"+stringtobinary(R1[1:]) +stringtobinary(R2[1:])+stringtobinary(R3[1:]))
  
def OR(R1,R2,R3):
    R[R1] = (R[R1])|(R[R2])
    print("0101000"+stringtobinary(R1[1:]) +stringtobinary(R2[1:])+stringtobinary(R3[1:]))

def AND(R1,R2,R3):
    R[R1] = R[R1]&R[R2]
    print("0101000"+stringtobinary(R1[1:]) +stringtobinary(R2[1:])+stringtobinary(R3[1:]))

## rahul add here: done
def move_imm(R1,imm):
    if imm<0 or imm>255:
      R["Error"] = 1
      return
    
    R[R1] = imm
    print("00010"+stringtobinary(R1[1:])+stringtobinary_8bit(imm))

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
  if imm<0 or imm>255:
    R["Error"] = 1
    return

  x = R[R1]
  for i in range(imm):
    x*=2
  R[R1]= x
  print("01000"+stringtobinary(R1[1:])+stringtobinary(imm))

def left_shift(R1,imm):
  if imm<0 or imm>255:
      R["Error"] = 1
      return
  x = R[R1]
  for i in range(imm):
    x/=2
  R[R1]= x
  print("01000"+stringtobinary(R1[1:])+stringtobinary(imm))

## sahas add here: ok
# C
# Performs reg1 = reg2
def MoveRegister(rx, ry):
    R[rx] = R[ry]
    print('0001100000' + stringtobinary(rx[1:]) + stringtobinary(ry[1:]))

# Performs reg3/reg4 Stores the quotient in R0 and the remainder in R1.
def Divide(rx, ry):
    R["R0"] = R[rx]//R[ry]
    R["R1"] = R[rx]%R[ry]
    print('00111' + stringtobinary(rx[1:]) + stringtobinary(ry[1:]))

# Performs bitwise NOT of reg2. Stores the result in reg1.
def Invert(rx, ry):
    # string = "101"
    string = bin(R[ry][2:])
    n = len(string)
    answer=""
    for i in range(n):
      if string[i]=="1":
        answer+="0"
      else:
        answer+="1"
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
    memaddr = R[rx]
    print('00101' + stringtobinary(rx[1:]) + stringtobinary_8bit(str(i)))

def check_label(line,i):
    temp = line.split(":")
    if len(temp)==2:
      labels[temp[0]] = i
      return True
    return False    


fullcode=[]

while(True):
    fullcode.append(input())
    temp = fullcode[-1]
    if temp == "hlt":
      break
    islabel = check_label(temp,len(fullcode))
    temp = temp.split(":")
    #print(temp)
    fullcode.pop() 
    if islabel:
      fullcode.append(temp[1].split())
    else: 
      fullcode.append(temp[0].split())
    
#print(len(fullcode))
curIndex = 0
while(True):
        if curIndex == len(fullcode):
            print("1001100000000000")
            break
        currentcode = fullcode[curIndex]
        
        curIndex+=1
        #print(currentcode)
        if(currentcode[0]=="add"):
            add(currentcode[1], currentcode[2], currentcode[3])
        if(currentcode[0]=="sub"):
            sub(currentcode[1], currentcode[2], currentcode[3])
        if(currentcode[0]=="mul"):
            multiply(currentcode[1], currentcode[2], currentcode[3])
        if(currentcode[0]=="xor"):
            xor(currentcode[1], currentcode[2], currentcode[3])
        if(currentcode[0]=="or"):
            OR(currentcode[1], currentcode[2], currentcode[3])
        if(currentcode[0]=="and"):
            AND(currentcode[1], currentcode[2], currentcode[3])
        if(currentcode[0] == "mov"):
            if currentcode[2][0] == '$':
              move_imm(currentcode[1],int(currentcode[2][1:]))
            else:
              MoveRegister(currentcode[1], currentcode[2])
        if currentcode[0]=="st":
            Store(currentcode[1], currentcode[2], curIndex)
        if(currentcode[0] == 'div'):
            Divide(currentcode[1], currentcode[2])
        if(currentcode[0] == 'not'):
            Invert(currentcode[1], currentcode[2])
        if(currentcode[0] == 'cmp'):
            Compare(currentcode[1], currentcode[2])

        if(currentcode[0] == 'rs'):
            right_shift(currentcode[1], int(currentcode[2][1:]))

        if(currentcode[0] == 'ls'):
            left_shift(currentcode[1], int(currentcode[2][1:]))
            
        if(R["Error"]==1):
            print("1001100000000000")
            break

        #debug()

def stringtobinary_8bit(string):
  n = int(string)
  num = 0
  answer=""
  while n!=0 :
      if n%2==1:
        answer+="1"
      else:
        answer+="0"
      n//=2
  size = len(answer)
  value = "0"*(8-size)
  answer = answer[::-1]
  value+=answer
  return value


