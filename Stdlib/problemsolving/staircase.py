def staircase(n):
    space_num = n-1
    for i in range(n):
        spaces = " "*space_num
        hashes = "#"*(i+1)
        space_num -= 1
        print(spaces+hashes)
        
staircase(6)