import os
import time


WIDTH = 8
HEIGHT = 8
MAXTRIES = 25

solved = False

map = [
    list("#.#....#"),
    list("#...##.#"),
    list("#.#.##.#"),
    list("#......#"),
    list("#.#S##.#"),
    list("#.####.#"),
    list("#......#"),
    list("######E#")
]
_map = [
    list("#.#....#"),
    list("#...##.#"),
    list("#.#.##.#"),
    list("#......#"),
    list("#.####.#"),
    list("#.####.#"),
    list("#......#"),
    list("######E#")
]
_map = [
    list("#.#....#"),
    list("S...##.#"),
    list("#.#.##.#"),
    list("#......#"),
    list("#.####.#"),
    list("#.####.#"),
    list("#......#"),
    list("######E#")
]
_map = [
    list("#.#....#"),
    list("SE..##.#"),
    list("###.####"),
    list("#......#"),
    list("#.####.#"),
    list("#.####.#"),
    list("#......#"),
    list("########")
]
_map = [
    list("#.#.E..#"),
    list("S...##.#"),
    list("###.####"),
    list("#......#"),
    list("#.####.#"),
    list("#.####.#"),
    list("#......#"),
    list("########")
]
_map = [
    list("#.#....#"),
    list("S...##.#"),
    list("###.####"),
    list("#......#"),
    list("#.####.#"),
    list("#.####.#"),
    list("#......#"),
    list("########")
]
_map = [
    list("###....#"),
    list("S...##.#"),
    list("###.#E##"),
    list("#......#"),
    list("#.####.#"),
    list("#.####.#"),
    list("#......#"),
    list("########")
]
_map = [
    list("###....#"),
    list("S...##.E"),
    list("###.####"),
    list("#......#"),
    list("#.####.#"),
    list("#.####.#"),
    list("#......#"),
    list("########")
]


class Player:
    def __init__(self):
        self.y = 0
        self.x = 0
        self.moved = 0
        self.routes = 0


def printmap():
    print()
    for row in map:
        print("".join(row))
    print()


p = []
player = Player()
p.append(player)

def solve():
    
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
            if map[p[i].y + dy][p[i].x + dx] == ".":
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
            if p[i].moved != 1 and map[p[i].y + dy][p[i].x + dx] == ".":
#                map[p[i].y][p[i].x] = f"{i}"
                map[p[i].y][p[i].x] = "x"
                p[i].y += dy
                p[i].x += dx
#                map[p[i].y][p[i].x] = f"{i}"
                map[p[i].y][p[i].x] = "O"
                p[i].moved = 1
#                print(f"{i} moved {direction}, and is moved = {p[i].moved}")
            elif p[i].moved != 1 and map[p[i].y + dy][p[i].x + dx] == "E":
#                map[p[i].y][p[i].x] = f"{i}"
                map[p[i].y][p[i].x] = "x"
                p[i].y += dy
                p[i].x += dx
#                map[p[i].y][p[i].x] = f"{i}"
                map[p[i].y][p[i].x] = "O"
                p[i].moved = 1
                solved = 1
                return


    for i in range(0, len(p)):
        p[i].moved = 0
        p[i].routes = 0


    return p[0]


# main
def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f"\n----- Attempt 0 -----")
    printmap()
    time.sleep(1)
    # find start
    solvable = False
    for y in range(HEIGHT):
        for x in range(WIDTH):
            if map[y][x] == "S":
                p[0].y = y
                p[0].x = x
                map[y][x] = "O"
                solvable = True

    if solvable == False:
        print("map not solvable")
        return -1

    os.system('cls' if os.name == 'nt' else 'clear')
    print(f"\n----- Attempt 0 -----")
    printmap()
    time.sleep(1)
    tries = 1

    for i in range(MAXTRIES):
        time.sleep(1)
        os.system('cls' if os.name == 'nt' else 'clear')

        print(f"\n----- Attempt {tries} -----")

        solve()

    #    for i in range(0,len(p)):
    #        print(p[i].y, p[i].x)

        printmap()
        if solved:
            print(f"solved in {tries}!")
            break
        tries += 1

    if not solved:
        print(f"couldnt solve within {MAXTRIES} attempts")

if __name__ == "__main__":
    main()
