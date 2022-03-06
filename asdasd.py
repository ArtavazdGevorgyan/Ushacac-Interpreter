import errors

vars={}
keyword=['vrbl','if','else','loop','otpt']

def mkvar(line):
    if ord(line[1][0]) in range(65,91) or ord(line[1][0]) in range(97,123) or line[1][0]=="_":
        if line[2]=="=":
            try:
                vars[str(line[1])]=str(eval(line[3]))
            except:
                vars[str(line[1])]=str(line[3])
        else:
            vars[str(line[1])]=None
    else: errors.varname(line)

def prnt(line):
    if line[1][0]=='"' and line[1][-1]=='"':
        print(line[1].replace('"', ''))
    elif line[1] in vars.keys():
        print(vars[line[1]])
    else: 
        try:
            print(eval(line[1]))
        except:
            errors.syntaxerror(line) 


def doeval(line):
    try:
        try:
            vars[line[0]]=eval(line[2])                # a = (1+2)*3
        except:
            exit=''
            for s in line[2]:                          # a = (a+b)*c
                if s in vars:                          # when a=1,b=2,c=3  
                    exit+=vars[s]                      # converting to
                elif s in "()+-*/.0123456789":          # a = (1+2)*3
                    exit+= s
            vars[line[0]]=eval(exit)
    except:
        errors.syntaxerror(line) 
