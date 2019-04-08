import sys
import binascii

F1 = {"000":"NOP", "001":"ADD", "010":"CLRAC", "011":"INCAC", "100":"DRTAC", "101":"DRTAR", "110":"PCTAR", "111":"WRITE"}
F2 = {"000":"NOP", "001":"SUB", "010":"OR", "011":"AND", "100":"READ", "101":"ACTDR", "110":"INCDR", "111":"PCTDR"}
F3 = {"000":"NOP", "001":"XOM", "010":"COM", "011":"SHL", "100":"SHR", "101":"INCPC", "110":"ARTPC", "111":"RES"}

CD = {"00":"U", "01":"I", "10":"S", "11":"Z"}
BR = {"00":"JMP", "01":"CALL", "10":"RET", "11":"MAP"}

MALAIN = {"0000":"ADD", "0001":"BRANCH", "0010":"STORE", "0011":"EXCHANGE"}
