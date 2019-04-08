# -*- coding: utf-8 -*-
"""
Created on Tue Feb 12 09:57:44 2019

@author: TARUN RAMPATI
"""
import binascii
h={'0':"0000",'1':"0001",'2':"0010",'3':"0011",'4':"0100",'5':"0101",'6':"0110",'7':"0111",
   '8':"1000",'9':"1001",'A':"1010",'B':"1011",'C':"1100",'D':"1101",'E':"1110",'F':"1111"}

m={"AND":"001","ADD":"000","LDA":"010","STA":"011","BUN":"100","CALL":"101","SUB":"110"}
r={"CLA":"7800","CMA":"7400","INC":"7200","HLT":"7100"}
i={"INP":"F800","OUT":"F400","SKI":"F200","SKO":"F100","ION":"F080","IOF":"F040"}
f={'#':'0','@':'1'}

def hexatobin(d):
    x=""
    for p in d:
        x=x+h.get(p)
    return x

def assembler(s):
    l=s.split(' ')
    if (len(l)>1):
        c=l[0]
        g=c[0:-1].upper()
        k=c[-1]
        n=l[1][0:-1]
        d=hexatobin(n)
        j=f.get(k)+m.get(g)+d
    elif (len(l)==1):
        g=s[0:].upper()
        if (g in r):
            j=hexatobin(r.get(g))
        else:
            j=hexatobin(i.get(g))
    else:
        j=""
    return j

fr=open("input.txt",'r')
lines=fr.readlines()
b=[]
for line in lines:
    if(line!="\n"):
        line=line.replace("\n","")
        p=assembler(line)
        a=int(p[0:8],2)
        c=int(p[8:],2)
        b.append(a)
        b.append(c)
        #print(hex(int(p,2)))


with open('output.bin', 'wb') as f:
    f.write(bytearray(b))
fr.close()    

print("From output file:")
f=open("output.bin",'rb')
while True:
    byte=f.read(2)
    if (byte==b''):
        break
    b=binascii.hexlify(byte)
    with open("outbin.txt", 'w') as filename:
        
        filename.write(hexatobin(str(b,'ascii').upper())+'\n')
    
    print(hexatobin(str(b,'ascii').upper()))
f.close()
