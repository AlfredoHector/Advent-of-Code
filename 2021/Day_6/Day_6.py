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

def next_day(fish):

    temp_fish = {}
    for i in range(0,8):
        temp_fish[i] = fish[i+1]
    temp_fish[6] += fish[0]
    temp_fish[8] = fish[0]

    return temp_fish

def count_fish(fish):
    total = 0
    for i in range(9):
        total += fish[i]
    return total

if __name__ == "__main__":
    fish = {x:0 for x in range(9)}
    data = openfile()[0].split(",")
    data = [int(x) for x in data]
    checkpoint = 0

    for n in data:                  # this is setting the already spawned fish
        fish[n] += 1

    for day in range(256):
        fish = next_day(fish)
        if day == 79:
            checkpoint = count_fish(fish)

    print(f"Part 1: after 80 days, there are {checkpoint} lanternfish!")
    print(f"Part 2: after 256 days, there are {count_fish(fish)} lanternfish!")