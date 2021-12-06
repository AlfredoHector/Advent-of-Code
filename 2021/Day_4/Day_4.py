#THIS IS NOT THE BEST. CHECK Better_Part_1.py!!!


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


class board():
    def __init__(self,dat):
        self.Y = len(dat)
        self.X = len(dat[0])
        self.drawn = [[0 for x in range(self.X)] for y in range(self.Y)]
        self.numbers = dat
        self.lastdrawn = 0
    
    def check_rows(self):
        for Y in range(self.Y):
            if sum(self.drawn[Y]) == self.Y:
                return True
        return False
                
    def check_columns(self):
        for X in range(self.X):
            temp = [self.drawn[Y][X] for Y in range(self.Y)]
            if sum(temp) == self.X:
                return True
        return False


    def check_win(self):
        if self.check_rows() or self.check_columns():
            return True
        return False
    
    def draw(self,n):
        for Y in range(self.Y):
            for X in range(self.X):
                if self.numbers[Y][X] == n:
                    self.drawn[Y][X] = 1
                    self.lastdrawn = n
    
    def final_points(self):
        total = 0
        for Y in range(self.Y):
            for X in range(self.X):
                if self.drawn[Y][X] == 0:
                    total += int(self.numbers[Y][X])
        return total * int(self.lastdrawn)

def parse():
    boards = []
    
    data = openfile()
    picks = data[0].split(",")
    data = data[2:]
    currentboard = []
    while len(data) >= 1:
        if data [0] == "":
            a = board(currentboard)
            boards.append(a)
            data = data[1:]
            currentboard = []
        else:
            line = data[0]
            data = data[1:]
            if line[0] == " ":
                line = line[1:]
            line = line.replace("  ", " ")
            line = line.split(" ")
            currentboard.append(line)
    boards.append(board(currentboard))
    return picks, boards




if __name__ == "__main__":
    picks, boards = parse()
    winners = []
    for pick in picks:
            for index, board in enumerate(boards):
                if index not in winners:
                    board.draw(pick)
                    if board.check_win() == True:
                        winners.append(index)

    # we have all the winners in that "winners" list, IN THE ORDER THEY WON...
    # so we just have to get the first for the first part, and the last for the second
    part1 = winners[0]
    print(f"Part 1: Winner is board No. {part1}, with points: {boards[part1].final_points()}")
    part2 = winners[len(winners)-1]
    print(f"Part 2: Last winner is board No. {part2}, with points: {boards[part2].final_points()}")