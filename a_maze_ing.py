from mazegen.generator import MazeGenerator
from display import display


def main() -> None:
    maze = MazeGenerator(20, 15, (0, 0), (19, 14), seed=42)
    maze.generate()
    display(maze)


if __name__ == "__main__":
    main()
