# -*- coding: utf-8 -*-
"""
Created on Sat Mar  9 19:13:56 2019

@author: TARUN RAMPATI
"""
import sys
import binascii
h={'0':"0000",'1':"0001",'2':"0010",'3':"0011",'4':"0100",'5':"0101",'6':"0110",'7':"0111",
   '8':"1000",'9':"1001",'A':"1010",'B':"1011",'C':"1100",'D':"1101",'E':"1110",'F':"1111"}

m={"AND":"000","ADD":"001","LDA":"010","STA":"011","BUN":"100","CALL":"101","SUB":"110"}
r={"CLA":"7800","CMA":"7400","INC":"7200","HLT":"7100"}
i={"INP":"F800","OUT":"F400","SKI":"F200","SKO":"F100","ION":"F080","IOF":"F040"}
f={'#':'0','@':'1'}


ac=0
pc=0
mem=[0 for i in range(4095)]
def hexatobin(d):
    x=""
    for p in d:
        x=x+h.get(p)
    return x

#print(mem)
mem[2929]=29
mem[29]=11
mem[2578]=27
mem[27]=7
def simulate(s):
    global ac
    global pc
    p=int(s,2)
    if(s[0:4]=="1111"):
        if (p==63488):
            c=input('')
            ac=ord(c)
        elif(p==62464):
            print(chr(ac))
        elif(p==61952):
            pass
        elif(p==61696):
            pass
        elif(p==61568):
            pass
        elif(p==61504):
            pass
    else:
        if (s[0:4]=="0111"):
           
            if (p==7800):
                ac=0
            elif (p==7400):
                ac=-ac
            elif(p==7200):
                ac=ac+1
            elif (p==7100):
                sys.exit()
        else:
            a=int(s[4:],2)
            if (s[0]=='1'):
                a=mem[a]
            d=mem[a]
            if (s[1:4]=="000"):
                ac= ac and d
            elif (s[1:4]=="001"):
                ac+=d
            elif (s[1:4]=="010"):
                ac=mem[a]
            elif (s[1:4]=="011"):
                mem[a]=ac
            elif (s[1:4]=="100"):
                pc=a
            elif (s[1:4]=="101"):
                pc=a
            elif (s[1:4]=="110"):
                ac=ac-d
           
            
            


f=open("output.bin",'rb')
while True:
    byte=f.read(2)
    if (byte==b''):
        break
    b=binascii.hexlify(byte)
   
    simulate(hexatobin(str(b,'ascii').upper()))
f.close()

print(mem)
print("data in B71",mem[2929])

print("data in A12 ",mem[2578])
print("by indirect computation data ",mem[mem[2578]])
print("ac=",ac)

#print(mem[3121])
#print(ac)