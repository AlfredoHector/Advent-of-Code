# I couldnt find a way to maintain both parts of the excercise in the same file while keeping
# it as readable as possible, so I just copied everything, and remade what I needed.

from Part1 import openfile
from Part1 import parse

def empty_square_array(n):
    array = []
    for x in range(n):
        array.append([])
        for y in range(n): 
            array[x].append(0)
    return array

    
def turn_off(array, point):
    x = point[0]
    y = point[1]
    if array[x][y] != 0:
        array[x][y] -= 1
    return array

def turn_on(array, point):
    x = point[0]
    y = point[1]
    array[x][y] += 1
    return array

def toggle(array, point):
    x = point[0]                        
    y = point[1]                        
    array[x][y] += 2
    return array

def count(Array):
    count = 0

    for x in range(len(Array)):
        for y in range(len(Array[x])):
            count += Array[x][y]
    
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