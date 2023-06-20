line = input()

def check(line):
    count = -1
    for letter in line:
        if letter == line[count]:
            count -= 1
    if count == -(len(line))-1:
        print(True)
    else:
        print(False)

check(line)


