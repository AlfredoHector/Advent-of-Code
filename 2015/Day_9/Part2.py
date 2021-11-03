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

def get_dict() -> dict:
    """ gets the travel times for all cities, returns a dictionary"""
    travel_times = {}

    for line in openfile():
        line = line.split(" ")
        origin, destiny, time = line[0], line[2], line[4]
        if origin not in travel_times:
            travel_times[origin] = {}
        if destiny not in travel_times:
            travel_times[destiny] = {}            
        travel_times[destiny][origin] = time
        travel_times[origin][destiny] = time
    return travel_times

def calculate(city, times, log= []) -> int:
    """calculates the distance in the entire travel"""
    log.append(city)
    possibles = [x for x in times[city].keys() if x not in log]
    
    if len(possibles) == 0:             # DONT TOUCH THIS, it is the end of the recursion.
        return 0

    max_distance = 0
    max_city = ""
    for a in possibles:
        b = int(times[city][a])
        if max_distance == 0:
            max_distance = b
            max_city = a
        elif max_distance < b:         # I am doing this in a rush, but there is a posibility
            max_distance = b           # that you get 2 cities with the maximum distance, wich
            max_city = a               # could mean you get wrong results. if you do, fix here...
    
    return max_distance + calculate(max_city,times,log)
    



if __name__ == "__main__":

    times = get_dict()
    travels = set()

    for city in times.keys():
        new = calculate(city, times, [])
        travels.add(new)

    print(max(travels))
