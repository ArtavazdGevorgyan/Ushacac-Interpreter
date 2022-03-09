import errors

vars={}
key=' .0123456789+-*/()[]|"qwertyuiopasdfghjklzxcvbnm,/;:=`~!@#$%^&*'

def mkvar(line, index):
    if ord(line[1][0]) in range(65,91) or ord(line[1][0]) in range(97,123) or line[1][0]=="_":
        if line[2]=="=":
            if line[3][0]=='"':
                exp=''
                for s in line[3:]:
                    for a in s:
                        if a in key:
                            exp+= a
                vars[line[1]]=exp
            else:
                exp=''
                for s in line[3:]:
                    if s in vars:
                        exp+=str(vars[s])
                    else:
                        for a in s:
                            if a in "()+-*/.0123456789":
                                exp+= a

                vars[line[1]]=str(eval(exp))
        else:
            vars[str(line[1])]=None
    else: errors.varname(line, index)


def prnt(line, index):
    if line[1][0]=='"' and line[-1][-1]=='"':
        exp=''
        for s in line[1:]:
            exp+= s + " "
        print(exp.replace('"', ''))
    else: 
        try:
            exp=''
            for s in line[1:]:
                if s in vars:
                    exp+=str(vars[s])
                else:
                    for a in s:
                        if a in "()+-*/.0123456789":
                            exp+= a
            print(str(eval(exp)))
        except:
            errors.syntaxerror(line, index) 


def doeval(line, index):
    try:
        exp=''
        for s in line[2:]:
            if s in vars:
                exp+=str(vars[s])
            elif s in "()+-*/.0123456789":
                exp+= s
        vars[line[0]]=str(eval(exp))
    except:
        errors.syntaxerror(line, index) 


def cond_if(line, index, code):
    body=[]
    exp=''
    for s in line[1:]:
        if s in vars:
            exp+=str(vars[s])
        elif s in "><=!()+-*/.0123456789":
            exp+= s
    index+=1
    erridx=index
    line=code[index].rstrip("\n")
    if line and line[0]=="{":
        while(code[index+1].rstrip("\n")[0]!="}"):
            body.append(code[index+1].lstrip("  ").rstrip("\n"))
            index+=1
    ifworked=0
    if eval(exp):      # if (True)
        ifworked=1
        for idx in range(len(body)):
            bodyline=body[idx].rstrip("\n")
            if bodyline.startswith("#"):
                pass
            elif bodyline.strip()=="":
                pass
            elif bodyline.split(" ")[0] == "vrbl":
                mkvar(bodyline.split(" "), idx)
            elif bodyline.split(" ")[0] in vars:
                doeval(bodyline.split(" "), idx)
            elif bodyline.split(" ")[0] == "output":
                prnt(bodyline.split(" "), idx)
            else:
                errors.undef(bodyline.split(" "),erridx+idx+1)
    return index+2,ifworked
        

def cond_else(index,code,ifworked):
    body=[]
    index+=1
    erridx=index
    line=code[index].rstrip("\n")
    if line and line[0]=="{":
        while(code[index+1].rstrip("\n")[0]!="}"):
            body.append(code[index+1].lstrip("  ").rstrip("\n"))
            index+=1

    if ifworked==0:
        for idx in range(len(body)):
            bodyline=body[idx].rstrip("\n")
            if bodyline.startswith("#"):
                pass
            elif bodyline.strip()=="":
                pass
            elif bodyline.split(" ")[0] == "vrbl":
                mkvar(bodyline.split(" "), idx)
            elif bodyline.split(" ")[0] in vars:
                doeval(bodyline.split(" "), idx)
            elif bodyline.split(" ")[0] == "output":
                prnt(bodyline.split(" "), idx)
            else:
                errors.undef(bodyline.split(" "),erridx+idx+1)
    return index+2


def loop(line, index, code):
    body=[]
    exp=''
    cond=line[1:]
    for s in cond:
        if s in vars:
            exp+=str(vars[s])
        elif s in "><=!()+-*/.0123456789":
            exp+= s
    index+=1
    erridx=index
    line=code[index].rstrip("\n")
    if line and line[0]=="{":
        while(code[index+1].rstrip("\n")[0]!="}"):
            body.append(code[index+1].lstrip("  ").rstrip("\n"))
            index+=1
    while eval(exp):      # while (True)
        for idx in range(len(body)):
            bodyline=body[idx].rstrip("\n")
            if bodyline.startswith("#"):
                pass
            elif bodyline.strip()=="":
                pass
            elif bodyline.split(" ")[0] == "vrbl":
                mkvar(bodyline.split(" "), idx)
            elif bodyline.split(" ")[0] in vars:
                doeval(bodyline.split(" "), idx)
            elif bodyline.split(" ")[0] == "output":
                prnt(bodyline.split(" "), idx)
            else:
                errors.undef(bodyline.split(" "),erridx+idx+1)
        exp=''
        for s in cond:
            if s in vars:
                exp+=str(vars[s])
            elif s in "><=!()+-*/.0123456789":
                exp+= s
    return index+2
