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

class Part1():
    def __init__(self):
        self.X = 0
        self.Y = 0
    
    def forward(self,n):
        self.X += int(n)
    def down(self,n):
        self.Y -= int(n)
    def up(self,n):
        self.Y += int(n)
    
    def result(self):
        r = self.Y * self.X
        if r < 0 :
            return -r
        else:
            return r

class Part2():
    def __init__(self):
        self.X = 0
        self.Y = 0
        self.Aim = 0 
    
    def forward(self,n):
        self.X += int(n)
        self.Y += (int(n) * self.Aim)
    def down(self,n):
        self.Aim += int(n)
    def up(self,n):
        self.Aim -= int(n)
    
    def result(self):
        r = self.Y * self.X
        if r < 0 :
            return -r
        else:
            return r


if __name__ == "__main__":
    data = openfile()
    sub = Part2()


    for step in data:
        direction, steps = step.split(" ")
        if direction == "forward":
            sub.forward(steps)
        elif direction == "up":
            sub.up(steps)
        elif direction == "down":
            sub.down(steps)

    print(sub.result())