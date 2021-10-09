def parse(step):
    if step == "(":         
        return 1            
    elif step == ")":       
        return -1     


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
    return inputfile.readlines()    # return list so I can copy-paste this function to all days and it should still work.



if __name__ == "__main__":
    floor = 0
    data = openfile()[0]

    # part 1
    # for step in data:           
    #     floor += parse(step)
    # print(floor)
    # end of part 1

    # part 2
    iterations = 0
    while floor != -1:
        floor += parse(data[iterations])
        iterations += 1
    print(iterations)
    # end of part 2
    
