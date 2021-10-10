def openfile() -> list:
    """return a list of the lines in the input file to work with."""
    try:

        dir = ""
        parts = __file__.split("\\")[:-1]
        parts = [x + "/" for x in parts]        
        for x in parts:
            dir += x            # up until here: get the path to the folder this file is in. (without extra modules)

        inputfile = open(f"{dir}input.txt")

    except FileNotFoundError:
        print("input.txt file not found on folder.\n Go get your input and store it in a file with this name, then retry.")
        quit()
    
    result = inputfile.read().split("\n")    # return list so I can copy-paste this function to all days and it should still work.
    
    if result[-1] == "":
        return result[:-1]
    else:
        return result

def parse(string):
    string = string.split(" ")
    output = string.pop()
    string.pop()
    return string, output

def NOT(n):
    return (~n)+2**16                       # unsigned integers in python...

def AND(a,b):
    return a & b

def OR(a,b):
    return a|b

def LSHIFT(a,b):
    return (a << b) & 65535


def RSHIFT(a,b):
    return (a >> b) & 65535

def operate(operation,values=dict):

    if len(operation) == 1:
        a = operation[0]
        if a.isnumeric() == True:
            return int(a)
        elif a in values.keys():
            return values[a]
        else:
            return None

    elif len(operation) == 2:
        a = operation[0]
        b = operation[1]

        if b.isnumeric() == True:
            temp = int(b)
        elif b in values.keys():
            temp = values[b]
        else:
            return None

        if a == "NOT":
            return NOT(temp)
        else:                                       # just in case, not really needed.
            print("error:command not supported")
        
    
    elif len(operation) == 3:
        a = operation[0]
        b = operation[1]
        c = operation[2]

        if a.isnumeric() == True:                   # probably would be better to have a function
            temp1 = int(a)                           # but its just 2 times... its fiiine...
        elif a in values.keys():
            temp1 = values[a]
        else:
            return None
        if c.isnumeric() == True:
            temp2 = int(c)
        elif c in values.keys():
            temp2 = values[c]
        else:
            return None            

        if b == "AND":
            return AND(temp1,temp2)
        elif b == "OR":
            return OR(temp1,temp2)
        elif b == "LSHIFT":
            return LSHIFT(temp1,temp2)
        elif b == "RSHIFT":
            return RSHIFT(temp1,temp2)
        else:
            print("error:command not supported")



def main(iteration, new_b ):
    pending = {}
    values = {}
    data = openfile()

    for string in data:                                     # this first pass is needed. to add
        operation, output = parse(string)                   # things to "pending"
        
        if iteration != 1 and output == "b":
            values["b"] = new_b
            continue

        result = operate(operation,values)
        if result == None:
            pending[output] = operation
        else:
            values[output] = result

    while len(pending) != 0:
        new_pending = {}

        for i in range(len(pending)):
            item = pending.popitem()
            output = item[0]
            operation = item[1]
            result = operate(operation,values)
            if result == None:
                new_pending[output] = operation
            else:
                values[output] = result

        for output in new_pending.keys():
            pending[output] = new_pending[output]
        
    print(f"part {iteration} :" + str(values["a"]))
    return values["a"]

if __name__ == "__main__":
    part2 = main(1, 0)
    main(2, part2)