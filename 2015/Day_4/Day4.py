import hashlib


key = input()
x= 0 
while True:
    a = bytes(str(key) + str(x),encoding="utf8")
    b = hashlib.md5(a)
    c = str(b.hexdigest())
    # if c[:5] == "00000":  # PART 1
    if c[:6] == "000000":   # PART 2
        print(x)
        break
    else:
        x += 1