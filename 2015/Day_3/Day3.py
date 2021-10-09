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

def store(house):
	if house not in houses:
		houses.append(house)

def getdir(input):
	if input == "<":
		return [-1,0]
	elif input == "^":
		return [0,1]
	elif input == ">":
		return [1,0]
	elif input == "v":
		return [0,-1]
		
def move(santa, dir):
	new = [santa[0] + dir[0] ,santa[1] + dir[1]]
	store(new)
	return new
	
if __name__ == "__main__":
    data = openfile()[0]

    santa1 = [0,0]
    santa2 = [0,0]
    houses = []
    placecounter = 0
    for a in data:
        store([0,0]) # need to store the beginning

        # santa1 = move(santa1, getdir(a))   # this line is part one
        
        # this is part 2
        if placecounter % 2 == 0:
            santa1 = move(santa1, getdir(a))
        elif placecounter % 2 == 1:
            santa2 = move(santa2, getdir(a))
        placecounter += 1 
        # end of part 2

    print (len(houses))