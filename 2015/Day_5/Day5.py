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

def check_banned_combinations(string, banned):
    for a in banned:
        a = re.compile("("+a+")")
        b = a.search(string)
        if b == None:
            continue
        else:
            return True
    return False

def check_repeated_letter(string,part):
    for i in range(len(string)-part):
        if string[i] == string[i+part]:
            return False
    return True

def check_req_vowels(string,vowels):
    v = []
    for a in string:
        if a in vowels:
            v.append(a)
    if len(v) > 2:
        return False
    else:
        return True

def check_repeated_pair(string):
    for i in range(len(string)-1):
        a = "(" + string[i] + string[i+1] + ")"
        results = re.findall(a,string)
        if len(results) != 1:
            return False
    return True

def Part_1(data):
    nice = []
    vowels = ["a","i","u","e","o"]
    banned_combinations = ["ab","cd","pq","xy"]
    
    for string in data:
        stop = check_banned_combinations(string,banned_combinations)
        if stop != True:                                                # this way was the fastest (avoids most of the checks)
            stop = check_req_vowels(string,vowels)
        if stop != True:
            stop = check_repeated_letter(string, 1)
        if stop != True:
            nice.append(string)
    return nice

def Part_2(data):
    nice = []

    for string in data:
        stop = check_repeated_letter(string, 2)
        if stop != True:
            stop = check_repeated_pair(string)
        if stop != True:
            nice.append(string)

    return nice

if __name__ == "__main__":
    data = openfile()

    # nice = Part_1(data)
    nice = Part_2(data)

    print(len(nice))
    