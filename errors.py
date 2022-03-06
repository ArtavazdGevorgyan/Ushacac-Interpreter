import sys

def fileerror():
    print("||| FILE IS NOT DEFINED")
    sys.exit()

def varname(line):
    print(f"||| {line}")
    print(" Variable name can starts with letter or underscore")
    sys.exit()

def syntaxerror(line):
    print(f"Invalid Syntax: {line}")
    sys.exit()

def logicerror():
    print("SOME LOGIC ERROR")
    sys.exit()

def undef(line, index):
    print(f"Line: {index} ||| {line}")
    print(f" name '{line[0]}' is not defined")
    sys.exit()