MOV AX,[1000h]
MOV BX,[1002h]
MOV CX,0000h
ADD AX,BX
MOV [1004h],AX
JNC jump
INC CL
jump:
MOV [1006h],CL
HLT