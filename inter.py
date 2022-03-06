import asdasd
from asdasd import vars
import sys
import errors

if len(sys.argv)==2 and sys.argv[1].endswith(".prt"):
    file=sys.argv[1]
##############################################
elif True:file="asd.prt"####  Delet this part
##############################################
else: errors.fileerror()

with open( file )as file:
    code=file.readlines()
for index in range(len(code)):
    codeline=code[index].rstrip("\n")
    if codeline.startswith("#"):
        pass
    elif codeline.strip()=="":
        pass
    elif codeline.split(" ")[0] == "vrbl":                        ##     <--|
        asdasd.mkvar(codeline.split(" "))                         ##        |
    elif codeline.split(" ")[0] in vars:                          ##     <--|
        asdasd.doeval(codeline.split(" "))
    elif codeline.split(" ")[0] == "output":
        asdasd.prnt(codeline.split(" "))
            
    else:
        errors.undef(codeline,index)
    