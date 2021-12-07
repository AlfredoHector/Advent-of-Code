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

def parse():
    biggest = 0
    points = []
    data = openfile()
    for line in data:
        a,b = line.split(" -> ")
        
        ax, ay= a.split(",")
        ax = int(ax)
        ay = int(ay)
        a = (ax,ay)
        
        bx, by= b.split(",")
        bx = int(bx)
        by = int(by)
        b = (bx,by)
        
        points.append([a,b])

        # there are other ways to do it, but since we have this here...
        for n in [ax,ay,bx,by]:
            if biggest < n:
                biggest = n
        
    return points,biggest

class chizu():
    def __init__(self,size):
        self.size = size +1 
        self.values = [[0 for _ in range(self.size)] for _ in range(self.size)]
    
    def HVline(self,start,end):             # This could be used for rectangles too. but it is not asked
        minX = min(start[0],end[0])         # in this puzzle
        maxX = max(start[0],end[0])
        minY = min(start[1],end[1])
        maxY = max(start[1],end[1])
        for X in range(minX, (maxX +1)):      # Have to add that +1 for python's range function
            for Y in range(minY, (maxY +1)):
                self.values[Y][X] += 1

    def diagonal(self,start,end):           # The puzzle specifies that it is always at 45 degrees...
        if start[0] < end[0]:
            StepX = 1                       # that means we can safely cheat a little...
        else:
            StepX = -1
        if start[1] < end[1]:
            StepY = 1
        else:
            StepY = -1
        Xs = [x for x in range(start[0],end[0]+StepX,StepX)]
        Ys = [y for y in range(start[1],end[1]+StepY,StepY)]
        for i in range(len(Xs)):
            self.values[Ys[i]][Xs[i]] +=1

    def shape_detect(self,a,b,P2):
        if a[0] == b[0] or a[1] == b[1]:
            self.HVline(a,b)                # stands for Horizontal/Vertical Lines
            return
        if P2:
            self.diagonal(a,b)

    def count_overlaps(self):
        counter = 0
        for Y in range(self.size):
            for X in range(self.size):
                if self.values[Y][X] >= 2:
                    counter += 1
        return counter

if __name__ == "__main__":

    Part_2 = True                           # Is this part 2?

    points, biggest = parse()
    places = chizu(biggest)
    for a,b in points:
        places.shape_detect(a,b,Part_2)
    
    print(places.count_overlaps())
    print("Done!")