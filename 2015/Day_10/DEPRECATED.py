#""" If you are learning python, use this as a lesson: modules are there to be used, the
#    community maintains them, they are secure, they have been tested millions of times,
#    and are improving day by day, by a lot of people that provide ideas, they will probably
#    be better than what you can write in an hour or two....
#
#    This piece of code will solve the challenge, (without modules) but it will take a long
#    time to solve (it took like 5 hours on my pc), use 'Day10.py' instead. that uses regular
#    expressions, and it took less than a minute to solve the challenge in my pc. 
#    Its pretty fast..... """

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

def read(number):
    new = ""
    # number = str(number)
    while len(number) != 0:
        counter = 0
        while len(number) > counter and number[counter] == number[0]:
            counter += 1
        new += str(counter) + str(number[0])
        number = number[counter:]
    return new
        

if __name__ == "__main__":
    number = openfile()[0]
    repeats = input("insert number of repeats : ")
    for _ in range(int(repeats)):
        number = read(number)
        print(_)
    print(len(number))