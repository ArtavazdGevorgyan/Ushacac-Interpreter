import logic
import sys
import errors

if len(sys.argv)==2 and sys.argv[1].endswith(".ush"):
    file=sys.argv[1]
else: errors.fileerror() #file="Sqrnums.ush"#

with open( file )as file:
    code=file.readlines()
brkcount=0
for index in range(len(code)):
    if code[index].startswith("{"): brkcount+=1
    if code[index].startswith("}"): brkcount-=1
if brkcount!=0: errors.bracketerror()
index=0
while index<len(code):
    codeline=code[index].rstrip("\n")
    if codeline.startswith("#"):
        pass
        index+=1
    elif codeline.strip()=="":
        pass
        index+=1
    elif codeline.split(" ")[0] == "vrbl":
        logic.mkvar(codeline.split(" "), index)
        index+=1
    elif codeline.split(" ")[0] in logic.vars:
        logic.doeval(codeline.split(" "), index)
        index+=1
    elif codeline.split(" ")[0] == "output":
        logic.prnt(codeline.split(" "), index)
        index+=1
    elif codeline.split(" ")[0] == "if":
        index,ifworked=logic.cond_if(codeline.split(" "), index, code)
    elif codeline.split(" ")[0] == "else":
        index=logic.cond_else(index, code, ifworked)
    elif codeline.split(" ")[0] == "loop":
        index=logic.loop(codeline.split(" "), index, code)    
    
    else:
        errors.undef(codeline.split(" "), index)
    