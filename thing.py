import os
import time
from defaultmaps import *


WIDTH = 8
HEIGHT = 8
MAXTRIES = 25

solved = 0


class Player:
    def __init__(self):
        self.y = 0
        self.x = 0
        self.moved = 0
        self.routes = 0


def printmap(chosen):
    print()
    for row in maps[chosen]:
        print("".join(row))
    print()


p = []
player = Player()
p.append(player)

def solve(chosen):
    
    global solved

#    print("solving")

    moves = [
        (1, 0, "down"),
        (-1, 0, "up"),
        (0, 1, "right"),
        (0, -1, "left")
    ]

    for i in range(0,len(p)):
        for dy, dx, direction in moves:
            if maps[chosen][p[i].y + dy][p[i].x + dx] == ".":
                p[i].routes += 1
#        print(f"{i} has routes:", p[i].routes)

    # if theres 2 or more routes possible, make a new player per route
    for i in range(0,len(p)):
        for j in range(0,p[i].routes-1):
            if p[i].routes > 1:
                tmp = Player()
                p.append(tmp)
                p[-1].y = p[i].y
                p[-1].x = p[i].x
                p[-1].moved = 0
#            print(f"player {i} pos: {p[i].y, p[i].x}, moved = {p[i].moved}")

#    print(f"size: {len(p)}")

    # move through available routes
    for i in range(0, len(p)):
#        print(f"player {i} has moved: {p[i].moved}")
        for dy, dx, direction in moves:
            if p[i].moved != 1 and maps[chosen][p[i].y + dy][p[i].x + dx] == "E":
#                maps[chosen][p[i].y][p[i].x] = f"{i}"
                maps[chosen][p[i].y][p[i].x] = "x"
                p[i].y += dy
                p[i].x += dx
#                maps[chosen][p[i].y][p[i].x] = f"{i}"
                maps[chosen][p[i].y][p[i].x] = "O"
                p[i].moved = 1
                solved = 1
            elif p[i].moved != 1 and maps[chosen][p[i].y + dy][p[i].x + dx] == ".":
#                maps[chosen][p[i].y][p[i].x] = f"{i}"
                maps[chosen][p[i].y][p[i].x] = "x"
                p[i].y += dy
                p[i].x += dx
#                maps[chosen][p[i].y][p[i].x] = f"{i}"
                maps[chosen][p[i].y][p[i].x] = "O"
                p[i].moved = 1
#                print(f"{i} moved {direction}, and is moved = {p[i].moved}")

    if solved == 1:
        return
    for i in range(0, len(p)):
        p[i].moved = 0
        p[i].routes = 0

def defaultmap():

    chosen = 0
    chose = ''
    i = 0
    # choose default map
    for map in maps:
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f"so like which map")
        print(f"\n----- Map {i} -----")
        printmap(i)
        print("you want this one? - [y] / [n]")
        chose = input()
        if chose == 'y':
            print(f"so like which map or wtv")
            chosen = i
            break
        elif chose == 'n':
            i += 1
            pass


    # print blank chosen map
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f"\n----- Attempt 0 -----")
    printmap(chosen)
    time.sleep(1)
    # initialize player
    solvable = False
    for y in range(HEIGHT):
        for x in range(WIDTH):
            if maps[chosen][y][x] == "S":
                p[0].y = y
                p[0].x = x
                maps[chosen][y][x] = "O"
                solvable = True
                break

    if solvable == False:
        print("map not solvable")
        return

    os.system('cls' if os.name == 'nt' else 'clear')
    print(f"\n----- Attempt 0 -----")
    printmap(chosen)
    time.sleep(1)
    tries = 1

    for i in range(MAXTRIES):
        os.system('cls' if os.name == 'nt' else 'clear')

        print(f"\n----- Attempt {tries} -----")

        solve(chosen)

    #    for i in range(0,len(p)):
    #        print(p[i].y, p[i].x)

        printmap(chosen)
        if solved:
            print(f"Solved in {tries}!\n")
            break
        tries += 1
        time.sleep(1)

    if not solved:
        print(f"Couldn't solve within {MAXTRIES} attempts.\n")


if __name__ == "__main__":
    os.system('cls' if os.name == 'nt' else 'clear')
    print('''what do you want to do?\n
           1: use default maps\n
           2: import map\n
           3: create map\n
           4: random map\n
           q: quit
           ''')
    choice = input()
    os.system('cls' if os.name == 'nt' else 'clear')

    if choice == '1':
        defaultmap()
#    elif choice == '2':
#        importmap()
#    elif choice == '3':
#        createmap()
#    elif choise == '4':
#        randommap()
