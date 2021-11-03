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
        # return result[:-1]
        return [str(x) for x in result[:-1]]
    else:
        return [str(x) for x in result]
        # return result

if __name__ == "__main__":
    rems = 0
    data = openfile()
    for string in data:
        leng = 0
        removed = 2 # the quote markers we are removing
        while len(string) != 1 :
            if string[0] == "\\":
                if string[1] != "x":
                    string = str(string[2:])
                    removed += 1
                else:
                    string = str(string[4:])
                    removed += 3
            else:
                string = str(string[1:])
            leng += 1
        rems += removed   
    print(rems)
    
    # a = b"\x9d\xa6\x6a".decode(encoding='UTF-8')    # I tried doing this, but either the console or python is reading the characters as more than strings, so it will get stuck. reading the hex digits as commands
    print("done!")
