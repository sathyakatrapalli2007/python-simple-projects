with open ("blank_space.txt") as f:
    r=f.readlines()
    r.reverse()
    for line in r:
        print(line)