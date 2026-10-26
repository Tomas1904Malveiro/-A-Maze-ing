import random
N, E, S, W = 0, 1, 2, 3

class MazeGenerator:
    def __init__(self, width: int, height: int,
                entry: tuple[int, int], exit_: tuple[int, int],
                perfect: bool = True, seed: int | None = None) -> None:
        self.width = width
        self.height = height
        self.grid = [[15] * width for _ in range(height)]
        self.entry = entry
        self.exit_ = exit_
        self.perfect = perfect
        self.rng = random.Random(seed)


    def open_wall(self, x: int, y: int, direction: int) -> None:
        dx = [0, 1, 0, -1]
        dy = [-1, 0, 1, 0]
        opposite = [S, W, N, E]

        nx = x + dx[direction]
        ny = y + dy[direction]

        self.grid[y][x] &= ~(1 << direction)
        self.grid[ny][nx] &= ~(1 << opposite[direction])

    
    def generate(self) -> None:
        visited = [[False] * self.width for _ in range(self.height)]

        x = self.entry[0]
        y = self.entry[1]
        visited[y][x] = True
        stack = [(x, y)]

        while len(stack) > 0:
            current = stack[-1]
            x = current[0]
            y = current[1]
        
            options = []
            if y > 0 and not visited[y - 1][x]:
                options.append(N)
            if x < self.width - 1 and not visited[y][x + 1]:
                options.append(E)
            if y < self.height - 1 and not visited[y + 1][x]:
                options.append(S)
            if x > 0 and not visited[y][x - 1]:
                options.append(W)
            
            if len(options) > 0:
                direction = self.rng.choice(options)
                self.open_wall(x, y, direction)

                if direction == N:
                    y = y - 1
                elif direction == E:
                    x = x + 1
                elif direction == S:
                    y = y + 1
                else:
                    x = x - 1

                visited[y][x] = True
                stack.append((x, y))
            else:
                stack.pop()


    def display(self) -> None:
        for y in range(self.height):
            line = ""

            for x in range(self.width):
                line += "+"

                if self.grid[y][x] & (1 << N):
                    line += "---"

                else:
                    line += "   "

            line += "+"
            print(line)


            line = ""
            for x in range(self.width):
                if self.grid[y][x] & (1 << W):
                    line += "|"
                else:
                    line += " "
                line += "   "
            if self.grid[y][self.width - 1] & (1 << E):
                line += "|"
            else:
                line += " "
            print(line)

        line = ""
        for x in range(self.width):
            line += "+"
            if self.grid[self.height - 1][x] & (1 << S):
                line += "---"
            else:
                line += "   "
        line += "+"
        print(line)


def main() -> None:
    maze = MazeGenerator(5, 5, (0, 0), (4, 4), seed=42)
    maze.generate()
    for row in maze.grid:
        print(row)


if __name__ == "__main__":
    main()
