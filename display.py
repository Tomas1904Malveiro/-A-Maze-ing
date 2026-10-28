from mazegen.generator import MazeGenerator, N, E, S, W


def display(maze: MazeGenerator) -> None:
    for y in range(maze.height):
        line = ""

        for x in range(maze.width):
            line += "+"

            if maze.grid[y][x] & (1 << N):
                line += "---"

            else:
                line += "   "

        line += "+"
        print(line)

        line = ""
        for x in range(maze.width):
            if maze.grid[y][x] & (1 << W):
                line += "|"
            else:
                line += " "

            if (x, y) in maze.cells_42:
                line += "███"
            else:
                line += "   "

        if maze.grid[y][maze.width - 1] & (1 << E):
            line += "|"
        else:
            line += " "
        print(line)

    line = ""
    for x in range(maze.width):
        line += "+"
        if maze.grid[maze.height - 1][x] & (1 << S):
            line += "---"
        else:
            line += "   "
    line += "+"
    print(line)
