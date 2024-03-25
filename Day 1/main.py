def read_lines(filename: str) -> list[int]:

    with open(f"./{filename}.txt") as file:
        lines = file.readlines()
        lines = [line.strip("\n") for line in lines]

    return lines[0]


def get_floor(instructions: str) -> int:
    """Return int that indicates the floor Santa should go to."""

    floor = 0

    for instruction in instructions:
        if instruction == "(":
            floor += 1
        else:
            floor -= 1

    return floor


def get_basement_pos(instructions: str) -> int:
    """Return int that indicates the floor Santa should go to."""

    floor = 0

    for i, instruction in list(enumerate(instructions, 1)):
        if instruction == "(":
            floor += 1
        else:
            floor -= 1
        if floor == -1:
            return i


if __name__ == "__main__":

    print(
        get_basement_pos(
            read_lines("input")
        )
    )
