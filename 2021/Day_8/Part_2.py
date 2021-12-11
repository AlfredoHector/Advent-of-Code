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

class display():
    def __init__(self):
        self.known = {}
        pass

    def deep_recognize(self, imput):
        test1 = len([x for x in imput if x in self.known[1]])
        test2 = len([x for x in imput if x in self.known[4]])
        test3 = len([x for x in imput if x in self.known[7]])
        length = len(imput)
        if length == 5:
            if test1 == 1 and test2 == 2 and test3 == 2:
                return 2
            elif test1 == 2 and test2 == 3 and test3 == 3:
                return 3
            elif test1 == 1 and test2 == 3 and test3 == 2:
                return 5
        elif length == 6:
            if test1 == 2 and test2 == 3 and test3 == 3:
                return 0
            elif test1 == 1 and test2 == 3 and test3 == 2:
                return 6
            elif test1 == 2 and test2 == 4 and test3 == 3:
                return 9

    def recognize(self, imput,deep =False):
        input_len = len(imput)
        result = imput
        if input_len == 2:
            result = 1
            self.known[1] = imput
            return result
        elif input_len == 4:
            result = 4
            self.known[4] = imput
            return result
        elif input_len == 3:
            result = 7
            self.known[7] = imput
            return result
        elif input_len == 7:
            result = 8
            self.known[8] = imput
            return result
        if len(self.known) >= 3 and deep:
            result = self.deep_recognize(imput)
        return result

def parse(data):
    tempa = []
    tempb = []
    for line in data:
        line = line.split(" | ")
        tempa.append(line[1].split(" "))
        tempb.append(line[0].split(" "))
    return tempa,tempb

if __name__ == "__main__":
    values, prep = parse(openfile())
    numbers = []

    for index, Set in enumerate(values):
        temp = ""
        disp = display()
        for p in prep[index]:
            disp.recognize(p)
        for value in Set:
            temp += str(disp.recognize(value,True))
        del disp
        numbers.append(int(temp))
    print(sum(numbers))