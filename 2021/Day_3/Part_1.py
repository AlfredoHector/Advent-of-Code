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

def count(numbs):
    numbs = [int(x) for x in numbs]
    if sum(numbs) >= len(numbs)/2:
        return 1
    else: 
        return 0


if __name__ == "__main__":
    data = openfile()
    Gamma_rate = ""
    Epsilon_rate = ""

    for i in range(len(data[0])):
        listy = []
        for A in data:
            listy.append(A[i])
        
        Gamma_rate = Gamma_rate + str(count(listy))
        Epsilon_rate = Epsilon_rate + str((count(listy)+1)%2)

    print(Gamma_rate, Epsilon_rate)
    
    print(int(Gamma_rate,2) * int(Epsilon_rate,2))
