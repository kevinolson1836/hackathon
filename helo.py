

def init_grid(size):
    grid = []
    for _ in range(size):
        grid.append([0]*size)
    return(grid)


def print_grid(grid):
    print()
    for x in range(len(grid)):
        print(grid[x])
    print()


grid = init_grid(5)

print_grid(grid)

print()
for x in range(8):
    print(grid[0][2-x])
    grid[0][2-x] = "H"
    print_grid(grid)
