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

def mean(nums):
    return sum(nums)//len(nums)

def distance(num, target):
    dist = target - num
    if dist < 0:
        return dist*-1
    else:
        return dist


if __name__ == "__main__":
    data = openfile()[0].split(",")
    data = sorted([int(x) for x in data])
    for i in range(499,500):                # I am not as sharp in math as I used to be, but I found
                                            # that it was always the one in this position, I left the loop
                                            # as an interesting thing, (as this is how I found the number,
                                            # by using this loop)
        distances = []
        temp = data[1*i:-1*i]
        target = mean(temp)
        for n in data:
            distances.append(distance(n,target))

    print("target =" , target)
    print(sum(distances))