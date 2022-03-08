import sys

def fileerror():
    print("||| FILE IS NOT DEFINED")
    sys.exit()

def varname(line, index):
    print(f"Line: {index+1} ||| {line}")
    print(f"||| {line}")
    print(" Variable name can starts with letter or underscore")
    sys.exit()

def syntaxerror(line, index):
    print(f"Line: {index+1} ||| {line}")
    print(f"Invalid Syntax")
    sys.exit()

def logicerror():
    print("SOME LOGIC ERROR")
    sys.exit()

def undef(line, index):
    print(f"Line: {index+1} ||| {line}")
    print(f" name '{line[0]}' is not defined")
    sys.exit()

def bracketerror():
    print(f"Some of brackets are missing")
    sys.exit()

def elseerror(line, index):
    print(f"Line: {index+1} ||| {line}")
    print("Ther is no if for this else")
