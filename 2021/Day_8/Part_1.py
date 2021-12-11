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
    
    result = inputfile.read().split("\n")  # return list so I can copy-paste this function to all days and it should still work.
    
    if result[-1] == "":
        return result[:-1]
    else:
        if type(result) == list:
            return result
        else: return [result]

def recognize(imput):
    input_len = len(imput)
    if input_len == 2:
        return 1
    elif input_len == 4:
        return 4
    elif input_len == 3:
        return 7
    elif input_len == 7:
        return 8

def parse(data):
    tempa = []
    tempb = []
    for line in data:
        line = line.split(" | ")
        tempa.append(line[1].split(" "))
        tempb.append(line[0].split(" "))
    return tempa,tempb

if __name__ == "__main__":
    values, prep = parse(openfile())
    numbers = []
    for Set in values:
        for value in Set:
            numbers.append(recognize(value))
    numbers = [x for x in numbers if x != None]
    print(len(numbers))