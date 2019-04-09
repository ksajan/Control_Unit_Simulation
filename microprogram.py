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
ar = 0

dr = "0011000000000000"

mpc = ""
ad = ""
mar = "0011000000000000"
SBR = ""

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



def Exchange(lol, ac, CAR, dr, SBR, ad, mar, pc):
    #global dr,CAR
    #print("car value initial me kya hai", CAR)
    #print("function call hua kya")
    # Starting Address will be decimal 12 binary 0001100
    if lol == "0001100":
        cond = int(dr[0])
        
        if cond == 1:
            #print("le lia")
            CAR, SBR = ad, BinarySum(CAR, "1")
        elif cond == 0:
            #print("pahucha kya")
            CAR = BinarySum(CAR, "1")
            #print("execute ho raha hai kya", CAR)
        print("*********************************************")
        print("Next Binary address called in Exchange\n", CAR)
        print("*********************************************")
        #print(CAR)
        #print("ahlkhd")
        #Indrct("1000011", CAR, dr)    # Not able to reach back to this point by executing indirect cycle
        Exchange("0001101",ac, CAR, dr, SBR, ad, mar, pc)
    elif lol == "0001101":
        ac = ac + dr
        #print("ac value", ac) # check for the dat type of ac if its binary string please change this statement to ac = BinarySum(ac, dr) as dr is string binary no. so confused
        cond = 0
        if cond == 1:
            CAR = ad
        elif cond == 0:
            CAR = BinarySum(CAR, "1")
        print("*****************************************************\n")
        print(" Next Binary address called in exchange , CAR:\n", CAR)
        print("*****************************************************")
        Exchange("0001110", ac, CAR, dr, SBR, ad, mar, pc) 
        # don't complain about why i didn't use CAR value directly because I am confused how its value changing across different function
    elif lol == "0001110":
        ac = dr
        dr = ac
        cond = 1
        if cond == 1:
            CAR = ad
        elif cond == 0:
            CAR = BinarySum(CAR, "1")
        print("Final address called in exchange function value of CAR: ac: dr: \n", CAR, ac, dr)
        Exchange("0001111", ac, CAR, dr, SBR, ad, mar, pc)
    elif lol == "0001111":
        mar = dr
        cond = 1
        if cond == 1:
            CAR = ad
        elif cond == 0:
            CAR = BinarySum(CAR, "1")
        #print("Next address generated is : \n", CAR, ad, mar)
        print("according to condition fetching new address after succesful completiont of exchange micro routine\n")
        print(" Calling Fetch Cycle for next instruction cycle\n")
        Fetch("1000000", CAR, pc, dr,mar, ac) #As you have reached the end of the Exchange Microroutine so calling to get new instruction
        
    

def Add(pgl):
    print("Binary address %s", ad)
    # First argument
    
    if pgl == "0000000":
        cond = dr[0]
        if cond == 1:
            CAR, SBR = ad, BinarySum(CAR, "1")

        else:
            CAR = BinarySum(CAR, "1")
        #ad = "1000011"
        Fetch("1000011")
        Add(CAR)
    elif pgl == "0000001":
        dr = mar
        cond = 1
        if cond == 1:
            CAR = ad
        elif cond == 0:
            CAR = BinarySum(CAR, "1")
        Add(CAR)
    elif pgl == "0000010":
        ac = ac + dr # Same check for the data type of ac if its binary string please change this to ac = BinarySum(ac, dr) Thanks in advance!
        cond = 1
        if cond == 1:
            CAR = ad
        elif cond == 0:
            CAR = BinarySum(CAR, "1")
        Fetch("1000000")
        # add print statement this the last microroutine in add as last 4th routine is doing nothing


    # Second argument

    #Fetch(ad)
def Store(tal_nappi):
    if tal_nappi == "0001000":
        cond = dr[0]
        if cond == 1:
            CAR, SBR = ad, BinarySum(CAR, "1")

        else:
            CAR = BinarySum(CAR, "1")
        Indrct("1000011")
        Store("0001001")
    elif tal_nappi == "0001001":
        dr = ac
        cond = 1
        if cond == 1:
            CAR = ad
        elif cond == 0:
            CAR = BinarySum(CAR, "1")
        store("0001010")
    elif tal_nappi == "0001010":
        mar = dr
        cond = 1
        if cond == 1:
            CAR = ad
        elif cond == 0:
            CAR = BinarySum(CAR, "1")
        Fetch("1000000") # end of the this Store function as next address will be fetched hopefully!

    
def Branch(arre_babu):
    print("Chalo abo print kardo :%s", arre_babu)
    if arre_babu == "0000100":
        # Please change the below code line 128 as it can be incorrect as i don't what value ac store 
        cond = ac[15]   # this might wil be changed according to what ac values it store
        if cond == 1:
            CAR = ad
        elif cond == 0:
            CAR = BinarySum(CAR, "1")
        Branch("0000110")
    elif arre_babu == "0000110":
        cond = dr[0]
        if cond == 1:
            CAR, SBR = ad, BinarySum(CAR, "1")
        elif cond == 0:
            CAR = BinarySum(CAR, "1")
        Fetch("1000011")
        Branch("0000111")
    elif arre_babu == "0000111":
        pc = ar
        cond = 1
        if cond == 1:
            CAR = ad
        elif cond == 0:
            CAR = BinarySum(CAR, "1")
        Fetch("1000000")
"""
    One of the branch file is missing as its contradicting with one of its own condition have to think how to add it lets disicuss

    Got any idea lets do it.
    Branch code which is contradicting and I can't understand it purpose 

    elif = "0000101"
        cond = 1
        if cond == 1:
            CAR = ad
        elif cond == 0:
            car = BinarySum(CAR, "1")
        Fetch("1000000")
"""
def Fetch(joker, CAR, pc, dr, mar, ac):
    
    #print("hello ", dr)
    print(" Binary calling address in Fetch", joker)
    #while True:
        #first argument
    if joker == "1000000":
        #print(joker)
        CAR = joker
        #ar = pc
        cond = 0
        if cond == 1:
            #print(CAR)
            CAR = ad
            #print(CAR)  
        elif cond == 0:
            CAR = BinarySum(CAR, "1")
            print("***********************************************\n")
            print("Next Binary Address called in Fetch cycle\n",CAR)
            print("***********************************************\n")    
        Fetch("1000001", CAR, pc, dr, mar, ac)
    elif joker == "1000001":
        dr = mar
        pc += 1
        print("pc value incremented",pc)
        cond = 0    
        if cond == 1:
            CAR = ad
        elif cond == 0:
            CAR = BinarySum(CAR, "1")
        print("************************************************\n")
        print("Next Binary Address called in Fetch cycle\n",CAR)   
        print("************************************************\n")

        Fetch("1000010", CAR, pc, dr, mar, ac)
    elif joker == "1000010":
        ar = dr[6:]
        cond = 1
        # Address mapping process
        #print("nuhi",dr) 
        
        CAR = "00" + dr[1:5] + "0"
        print("CAR: ", CAR)

        if CAR == "0001100":
            #print("pc value is",pc)
            print("callin function exchange\n")
            if pc == 1:
                Exchange(CAR, ac, CAR, dr, SBR, ad, mar, pc) #(lol, ac, CAR, dr, SBR, ad, mar, pc)
            else:
                print("#################################")
                print("Successfuly completed one cycle")
                print("#################################\n")
            
        #    break
        elif CAR == "0000000":
            Add(CAR)
        #    break
        elif CAR == "0000100":
            Branch(CAR)
         #   break
        elif CAR == "0001000":
            Store(CAR)
    #        break       
        #    break

    


def Indrct(joker, CAR, dr):
    #global CAR, dr
    print("*****************************************************")
    print(" Binary calling address in indiect cycle", joker)
    print("*****************************************************")

    #first argument
    if joker == " 1000011":
        dr = mar
        cond = 1
        if cond == 1:
            CAR = ad
        else:
            CAR = BinarySum(CAR, "1")
        Indrct("1000100", CAR, dr)
    elif joker == "1000100":
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
dr = myfile.read()
myfile.close()
#print(contents[:4])
#print(dr)

Opcode = dr[:4]
    
if Opcode in MALAIN:
    Symbol = MALAIN.get(Opcode)
    if Symbol == MALAIN["0011"]:
        Fetch("1000000", CAR, pc, dr, mar, ac)
        print("end of the execution")
        #Exchange()
    elif Symbol == ADD:
        #Add()
#    elif Symbol == BRANCH:
        #Branch()
#    elif Symbol == STORE:
        #Store()        
        print("reached")
else:
    print("error")
        
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
