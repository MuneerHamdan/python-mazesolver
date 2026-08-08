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
        self.active = ""


def printmap():
    print()
    for row in map:
        print("".join(row))
    print()


p = Player()
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

    print(f"no E: p.y: {p.y}, p.x: {p.x}")

    print("traversing")

    routes = 0

    for dy, dx, direction in moves:
        if map[p.y + dy][p.x + dx] == ".":
            print("route", direction)
            routes += 1

    # move through available routes
    for dy, dx, direction in moves:
        if map[p.y + dy][p.x + dx] == ".":
            map[p.y][p.x] = "x"
            p.y += dy
            p.x += dx
            print("moved", direction)

    print("routes:", routes)

    map[p.y][p.x] = "O"

    return p


def backtrack(p):

    print("backtracking")

    moves = [
        (1, 0, "down"),
        (-1, 0, "up"),
        (0, 1, "right"),
        (0, -1, "left")
    ]

    for dy, dx, direction in moves:
        if map[p.y + dy][p.x + dx] == "x":
            map[p.y][p.x] = "-"
            p.y += dy
            p.x += dx
            print("moved", direction)
            map[p.y][p.x] = "O"
            return


# main
printmap()
# find start
for y in range(HEIGHT):
    for x in range(WIDTH):
        if map[y][x] == "S":
            p.y = y
            p.x = x
            map[y][x] = "O"
printmap()
tries = 1

for i in range(MAXTRIES):

    print(f"\n\n----- Attempt {tries} -----\n")

    solve()
    printmap()

    if solved:
        print("solved!!!!!!")
        printmap()
        break
    tries += 1


if not solved:
    print(f"couldnt solve within {MAXTRIES} attempts")
