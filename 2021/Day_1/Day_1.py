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
        return [result]

def Part_2(numbers):
    return [(numbers[i] + numbers[i+1] + numbers[i+2]) for i in range(len(numbers)-2)]


if __name__ == "__main__":
    Part2 = True                                # Use this to change between part 1 and 2 of the challenge
    numbers = [int(x) for x in openfile()]
    counts = 0

    if Part2:
        numbers = Part_2(numbers)


    for i,n in enumerate(numbers):
        if i != 0 and n > numbers[i-1]:
            counts +=1 
    
    print(counts)