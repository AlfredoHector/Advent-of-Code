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
        return result

def parse(string):
    order = string.split(" ")
    point2 = order.pop()                
    order.pop()                         # pop gets rid of "through" word
    point1 = order.pop()

    # get a single string from the remaining words
    if len(order) == 2:
        order = str(order[0] + order[1])
    else:
        order = order[0]
    
    return order, point1.split(","), point2.split(",")

def empty_square_array(n):
    array = []
    for x in range(n):
        array.append([])
        for y in range(n): 
            array[x].append(False)
    return array

    
def turn_off(array, point):
    x = point[0]
    y = point[1]
    array[x][y] = False
    return array

def turn_on(array, point):
    x = point[0]
    y = point[1]
    array[x][y] = True
    return array

def toggle(array, point):
    x = point[0]                        # yes, I could do a one-liner, but that
    y = point[1]                        # would look ugly, wouldnt it?
    a = array[x][y]
    if a == True:
        array[x][y] = False
    elif a == False:
        array[x][y] = True
    return array

def count(Array):
    count = 0 

    for x in range(len(Array)):
        for y in range(len(Array[x])):
            if Array[x][y] == True:
                count += 1
    
    print(count)
        


if __name__ == "__main__":
    data = openfile()
    Array = empty_square_array(1000)
    # Main loop
    for string in data:
        order, point1, point2 = parse(string)
        for x in range( int(point1[0]) , int(point2[0])+1 ):          # need the 1, since range function excludes the last number
            for y in range( int(point1[1]) , int(point2[1])+1):
                if order == "toggle":
                    Array = toggle(Array,[x,y])
                elif order == "turnon":
                    Array = turn_on(Array,[x,y])
                elif order == "turnoff":
                    Array = turn_off(Array,[x,y])
    
    count(Array)