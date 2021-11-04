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

alphabet = "abcdefghijklmnopqrstuvwxyz"

def stringyfy(L):
    S = ""
    for a in L:
        S += a
    return S

def generate_tests():
    banned = ["i","o","l"]
    required = []
    for i in range(len(alphabet)-2):
        required.append(str(alphabet[i] + alphabet[i+1] + alphabet[i+2]))
    for i in range(len(alphabet)):
        required.append(str(alphabet[i] + alphabet[i]))
    return required, banned

def test(word, required):
    match = []

    for a in required:
        if a in word:
            match.append(a)

    b = {len(x) for x in match}
    
    if len(match) < 3:
        return 1
    if len(b) != 2:
        return 1
    return 0

def modify(word, index, li, A):
    if word[index] == li[-1]:
        word = modify(word, index-1, li, A)
        word[index] = li[0]
    else:
        word[index] = li[A[word[index]]+1]
    return word
        

def generate_word(word, banned):
    correct = [x for x in alphabet if x not in banned]
    A = {}
    for index in range(len(correct)):
        A[correct[index]] = index

    return stringyfy(modify(list(word), -1, correct, A))
    


if __name__ == "__main__":
    first = openfile()[0]
    required, banned = generate_tests()
    new_word = generate_word(first, banned)
    

    while test(new_word, required) != 0:
        # print(f"Test failed: {new_word}")
        new_word = generate_word(new_word, banned)
    print("Part 1 : " + new_word)                       # Maybe this was luck, I didnt
                                                        # feel confident it would work
    new_word = generate_word(new_word, banned)
    while test(new_word, required) != 0:
        # print(f"Test failed: {new_word}")
        new_word = generate_word(new_word, banned)
    print("Part 2 : " + new_word)    
    