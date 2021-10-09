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

def Part1(l,w,h):
    side_1 = l*w
    side_2 = w*h
    side_3 = h*l
    smallest = min([side_1, side_2, side_3])
    return (2*side_1) + (2*side_2) + (2*side_3) + smallest
        
def Part2(l,w,h):
        side_1 = 2*l+2*w
        side_2 = 2*w+2*h
        side_3 = 2*h+2*l
        smallest = min([side_1, side_2, side_3])
        return smallest + (l*w*h)


if __name__ == "__main__":
    data = openfile()

    result = 0
    for box in data:
        box = box.split("x")
        l = int(box[0])
        w = int(box[1])
        h = int(box[2])
        # result += Part1(l,w,h)          
        result += Part2(l,w,h)
    print(result)
