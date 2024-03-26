def read_lines(filename: str) -> list[int]:

    with open(f"./{filename}.txt") as file:
        lines = file.readlines()
        lines = [line.strip("\n") for line in lines]

    return lines[0]


def get_visited_dict(instructions: str) -> dict:
    """Return a dictionary of location:visit_count."""

    visited = {(0, 0): 1}
    x, y = 0, 0

    for instruction in instructions:

        if instruction == "^":
            y += 1
        if instruction == "v":
            y -= 1
        if instruction == "<":
            x -= 1
        if instruction == ">":
            x += 1

        if (x, y) in visited.keys():
            visited[(x, y)] += 1
        else:
            visited[(x, y)] = 1

    return visited


def get_visited_dict_with_robot(instructions: str) -> dict:
    """Return a dictionary of location:visit_count."""

    visited = {(0, 0): 2}
    santa_x, santa_y = 0, 0
    robot_x, robot_y = 0, 0

    for i, instruction in enumerate(instructions):

        if i % 2 == 1:
            if instruction == "^":
                santa_y += 1
            if instruction == "v":
                santa_y -= 1
            if instruction == "<":
                santa_x -= 1
            if instruction == ">":
                santa_x += 1
            if (santa_x, santa_y) in visited.keys():
                visited[(santa_x, santa_y)] += 1
            else:
                visited[(santa_x, santa_y)] = 1
        else:
            if instruction == "^":
                robot_y += 1
            if instruction == "v":
                robot_y -= 1
            if instruction == "<":
                robot_x -= 1
            if instruction == ">":
                robot_x += 1
            if (robot_x, robot_y) in visited.keys():
                visited[(robot_x, robot_y)] += 1
            else:
                visited[(robot_x, robot_y)] = 1

    return visited


if __name__ == "__main__":

    instructions = read_lines("input")
    visited = get_visited_dict(instructions)
    visited_with_robot = get_visited_dict_with_robot(instructions)
    print(
        len(visited_with_robot.keys())
    )
