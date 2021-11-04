import re

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

def read(number):
    new = ""
    number = str(number)
    findings = re.findall("0{1,}|1{1,}|2{1,}|3{1,}|4{1,}|5{1,}|6{1,}|7{1,}|8{1,}|9{1,}", number)
    for n in findings:
        new += str(len(n)) + str(n)[0]
    return new
        

if __name__ == "__main__":
    number = openfile()[0]
    repeats = input("insert number of repeats : ")
    for _ in range(int(repeats)):
        number = read(number)
        print(f"Repeat: {_+1}  -  Length: {len(number)}")