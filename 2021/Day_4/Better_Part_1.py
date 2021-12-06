# I had a problem on this day, got me stuck for hours, and asked a friend for a little help.
# we had to use numpy for it, and it sometimes makes the code smaller, but I find it
# fun to make it entirely without modules, so this one is the best, but the other one is 
# still there if you want it.

import numpy as np , sys 

max_num =sys.maxsize -1

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
        # self.drawn = [[0 for x in range(self.X)] for y in range(self.Y)]
        self.drawn = np.zeros((5,5))
        self.numbers = np.matrix(dat)
        self.lastdrawn = 0
    
    def check_rows(self):
        for valor in self.numbers.sum(axis = 1):
            if valor == 0:
                return True
        return False
                
    def check_columns(self):
        auxiliar_numbers = self.numbers.swapaxes(0,1)
        for valor in auxiliar_numbers.sum(axis = 1):
            if valor == 0:
                return True
        return False


    def check_win(self):
        if self.check_rows() or self.check_columns():
            return True
        return False
    
    def draw(self,n):
        self.numbers = np.where(self.numbers!=n, self.numbers, 0)
    
    def final_points(self, lastnumber):
        total = self.numbers.sum()
        return total * lastnumber

def parse():
    boards = []
    
    data = openfile()
    picks = data[0].split(",")
    picks = [int(x) for x in picks]
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
            currentboard.append([int(x) for x in line])
    boards.append(board(currentboard))
    return picks, boards

def ganador_en_turnos(picks,board,min_winner):
    for loop, pick in enumerate(picks):
        board.draw(pick)

        if loop > min_winner:
            break
        if loop >= 5:
            if board.check_win():
                return loop, board
    return max_num, board






if __name__ == "__main__":
    picks, boards = parse()
    min_ganador = max_num
    for board in boards:
        nuevo_valor, posible_ganador =ganador_en_turnos(picks,board,min_ganador)
        if min_ganador >= nuevo_valor:
            min_ganador = nuevo_valor
            winner = posible_ganador

    print(winner.final_points(picks[min_ganador]))