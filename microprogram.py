import sys
import binascii

F1 = {"000":"NOP", "001":"ADD", "010":"CLRAC", "011":"INCAC", "100":"DRTAC", "101":"DRTAR", "110":"PCTAR", "111":"WRITE"}
F2 = {"000":"NOP", "001":"SUB", "010":"OR", "011":"AND", "100":"READ", "101":"ACTDR", "110":"INCDR", "111":"PCTDR"}
F3 = {"000":"NOP", "001":"XOM", "010":"COM", "011":"SHL", "100":"SHR", "101":"INCPC", "110":"ARTPC", "111":"RES"}

CD = {"00":"U", "01":"I", "10":"S", "11":"Z"}
BR = {"00":"JMP", "01":"CALL", "10":"RET", "11":"MAP"}

MALAIN = {"0000":"ADD", "0001":"BRANCH", "0010":"STORE", "0011":"EXCHANGE"}

CAR =""
pc = 0
ac = ""
ar = ""
dr = ""
mpc = ""
ad = ""
mar = ""
def Exchange(lol):
    
    # Starting Address will be decimal 12 binary 0001100
    if lol = "0001100"
        cond = dr[1]
        if cond == 1:
            CAR, SBR = ad, BinarySum(CAR, "1")
        elif cond == 0:
            CAR = BinarySum(CAR, "1")
        Indrct("1000011")    # Not able to reach back to this point by executing indirect cycle
        Exchange("0001101")
    elif lol == "0001101":
        ac = ac + dr # check for the dat type of ac if its binary string please change this statement to ac = BinarySum(ac, dr) as dr is string binary no. so confused
        cond = 1
        if cond == 1:
            CAR = ad
        elif cond == 0:
            CAR = BinarySum(CAR, "1")
        Exchange("0001110") # don't complain about why i didn't use CAR value directly because I am confused how its value changing across different function
    elif lol = "0001110":
        ac = dr
        dr = ac
        cond = 1
        if cond == 1:
            CAR = ad
        elif cond == 0:
            CAR = BinarySum(CAR, "1")
        Exchange("0001111")
    elif lol == "0001111":
        mar = dr
        cond = 1
        if cond == 1:
            CAR = ad
        elif cond == 0:
            CAR = BinarySum(CAR, "1")
        Fetch("1000000") #As you have reached the end of the Exchange Microroutine so calling to get new instruction
        print("Next address generated is : %s" CAR)
    

def Add(pgl):
    print("Binary address %s", ad)
    # First argument
    
    if pgl = "0000000":
        cond = dr[15]
        if cond == 1:
            CAR, SBR = ad, BinarySum(CAR, "1")

        else:
            CAR = BinarySum(CAR, "1")
        ad = "1000011"
        Fetch(ad)
    elif pgl = "0000001":

    # Second argument

    #Fetch(ad)
def Store():
    pass
def Branch():
    pass

def Fetch(joker):
    print(" Binary calling address %s", joker)
    while True:
        #first argument
        if joker = " 1000000":
            ar = pc
            cond = 0
            if cond == 1:
                CAR = ad
            elif cond == 0:
                CAR = BinarySum(CAR, "1")
            
            Fetch(CAR)
        elif joker = "1000001":
            dr = mar
            pc += 1
            cond = 0    
            if cond == 1:
                CAR = ad
            elif == 0:
                CAR = BinarySum(CAR, "1")
            
            Fetch(CAR)
        elif joker = "1000010":
            ar = dr[6:]
            cond = 1
            # Address mapping process
            CAR = "00" + dr[1:5] + "0"

            if CAR == "0001100":
                Exchange(CAR)
                break
            elif CAR == "0000000":
                Add(CAR)
                break
            elif CAR == "0000100":
                Branch(CAR)
                break
            elif CAR == "0001000":
                Store(CAR)
                break       
        

    


def Indrct(joker):
    print(" Binary calling address %s", joker)

    #first argument
    if joker = " 1000011":
        dr = mar
        cond = 1
        if cond == 1:
            CAR = ad
        else:
            CAR = BinarySum(CAR, "1")
        Fetch("1000100")
    elif joker = "1000100":
        ar = dr[6:]
        cond = 1    # No use I don't understand the point of having this condition as 1
        CAR = SBR
    return CAR
"""
        # calling microroutine
        if CAR == "0001100":
                Exchange(CAR)
                break
            elif CAR == "0000000":
                Add(CAR)
                break
            elif CAR == "0000100":
                Branch(CAR)
                break
            elif CAR == "0001000":
                Store(CAR)
                break      
"""
        


myfile = open("outbin.txt", 'rt')
contents = myfile.read()
myfile.close()
#print(contents[:4])

Opcode = contents[:4]
    
if Opcode in MALAIN:
    Symbol = MALAIN.get(Opcode)
    if Symbol == EXCHANGE:
        Exchange()
    elif Symbol == ADD:
        Add()
    elif Symbol == BRANCH:
        Branch()
    elif Symbol == STORE:
        Store()        
        print("reached")
        
    #print(Symbol)




# This function adds two binary  
# strings return the resulting string 
def BinarySum(x, y): 
        max_len = max(len(x), len(y)) 
  
        x = x.zfill(max_len) 
        y = y.zfill(max_len) 
          
        # initialize the result 
        result = '' 
          
        # initialize the carry 
        carry = 0
  
        # Traverse the string 
        for i in range(max_len - 1, -1, -1): 
            r = carry 
            r += 1 if x[i] == '1' else 0
            r += 1 if y[i] == '1' else 0
            result = ('1' if r % 2 == 1 else '0') + result 
            carry = 0 if r < 2 else 1     # Compute the carry. 
          
        if carry !=0 : result = '1' + result 
  
        return result.zfill(max_len) 
