MOV AX,[1000h]
MOV BX,[1002h]
MOV CX,0000h
SUB AX,BX
JNC jump
INC CL
NOT AX
ADD AX,0001h
jump:

MOV [1004h],AX
MOV [1006h],CL
HLT