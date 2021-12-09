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
    return (max(nums) - min(nums)) //2

def distance(num, target):
    dist = target - num
    if dist < 0:
        return dist*-1
    else:
        return dist

def cost(num,target):
    n = distance(num,target)
    steps = [x for x in range(n+1)]
    return sum(steps)


if __name__ == "__main__":
    data = openfile()[0].split(",")
    data = sorted([int(x) for x in data])
    old_target = 0
    old_minimal = 9**15                     # This just had to be a big number.
    for target in range(max(data)):             # I am not as sharp in math as I used to, I couldnt find
                                                # proper function for this, so we are just looping!
        distances = []
        for n in data:
            distances.append(cost(n,target))
        minimal = sum(distances)
        if old_minimal > minimal:
            old_minimal = minimal
            old_target = target
    print("target =" , old_target)
    print(old_minimal)