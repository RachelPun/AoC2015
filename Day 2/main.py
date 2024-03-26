def read_lines(filename: str) -> list[int]:

    with open(f"./{filename}.txt") as file:
        lines = file.readlines()
        lines = [line.strip("\n") for line in lines]

    return lines


def get_dims(line: str) -> list[int]:
    """Takes a string of present dimensions.
    Returns the dimensions as a list of integers."""

    return [int(num) for num in line.split("x")]


def calc_paper_area(dims: list[int]) -> int:
    """Returns the area of paper needed for a present of 3 dimensions."""

    areas = [dims[0]*dims[1],
             dims[1]*dims[2],
             dims[2]*dims[0]]

    areas.sort()

    area = areas[0]*3 + areas[1]*2 + areas[2]*2

    return area


def calc_ribbon_len(dims: list[int]) -> int:
    """Returns the length of ribbon needed for a present of 3 dimensions."""

    dims.sort()

    return sum(dims[:2])*2 + dims[0]*dims[1]*dims[2]


if __name__ == "__main__":

    all_lines = read_lines("input")
    all_dims = [get_dims(line) for line in all_lines]
    total_area = sum([calc_paper_area(dims)
                      for dims in all_dims])
    total_len = sum([calc_ribbon_len(dims)
                     for dims in all_dims])

    print(
        total_len
    )
