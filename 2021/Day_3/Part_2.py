
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

def get_mean(index,data):
    numbers = []
    for line in data:
        numbers.append(int(line[index]))
    
    if sum(numbers) >= len(numbers)/2:
        return 1
    else: 
        return 0

def not_mean(index,data):
    if get_mean(index,data) == 1:
        return 0
    else:
        return 1


if __name__ == "__main__":

    data = openfile()
    for i in range(len(data[0])):
        new_data = []
        mean = str(get_mean(i,data))
        for line in data:
            if line[i] == mean:
                new_data.append(line)
        data = new_data
        if len(new_data) == 1:
            break
    
    O2_rate = new_data[0]

    data = openfile()
    for i in range(len(data[0])):
        new_data = []
        mean = str(not_mean(i,data))
        for line in data:
            if line[i] == mean:
                new_data.append(line)
        data = new_data
        if len(new_data) == 1:
            break

    CO2_rate = new_data[0]

    print(O2_rate,CO2_rate)
    print(int(O2_rate,2)*int(CO2_rate,2))