WIDTH = 8
HEIGHT = 8
MAXTRIES = 10

solved = False

map = [
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

    print("solving")

    moves = [
        (1, 0, "down"),
        (-1, 0, "up"),
        (0, 1, "right"),
        (0, -1, "left")
    ]

    # check for exit

    print(f"no E -> traversing now")


    routes = 0

    for dy, dx, direction in moves:
        if map[p[0].y + dy][p[0].x + dx] == ".":
            print("route", direction)
            routes += 1
    print("routes:", routes)

    # if theres 2 or more routes possible, make a new player per route
    if routes > 1:
        for i in range(0,routes-1):
            tmp = Player()
            p.append(tmp)
            p[-1].y = p[0].y
            p[-1].x = p[0].x
            p[-1].moved = 0
            print(f"player {i} pos: {p[i].y, p[i].x}, moved = {p[i].moved}")

    print(f"size: {len(p)}")

    # move through available routes
    for i in range(0, len(p)):
        print(f"player {i} has moved: {p[i].moved}")
        for dy, dx, direction in moves:
            if p[i].moved != 1 and map[p[i].y + dy][p[i].x + dx] == ".":
                map[p[i].y][p[i].x] = "x"
                p[i].y += dy
                p[i].x += dx
                map[p[i].y][p[i].x] = "O"
                p[i].moved = 1
                print(f"{i} moved {direction}, and is moved = {p[i].moved}")
                printmap()


    for i in range(0, len(p)):
        p[i].moved = 0


    return p[0]


def backtrack():

    print("backtracking")

    moves = [
        (1, 0, "down"),
        (-1, 0, "up"),
        (0, 1, "right"),
        (0, -1, "left")
    ]

    for dy, dx, direction in moves:
        if map[p[0].y + dy][p.x + dx] == "x":
            map[p[0].y][p.x] = "-"
            p[0].y += dy
            p[0].x += dx
            print("moved", direction)
            map[p[0].y][p.x] = "O"
            return


# main
printmap()
# find start
for y in range(HEIGHT):
    for x in range(WIDTH):
        if map[y][x] == "S":
            p[0].y = y
            p[0].x = x
            map[y][x] = "O"
printmap()
tries = 1

for i in range(MAXTRIES):

    print(f"\n\n----- Attempt {tries} -----\n")

    printmap()
    solve()

    for i in range(0,len(p)):
        print(p[i].y, p[i].x)

    if solved:
        print("solved!!!!!!")
        printmap()
        break
    tries += 1


if not solved:
    print(f"couldnt solve within {MAXTRIES} attempts")
