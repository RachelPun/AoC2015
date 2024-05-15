from collections import defaultdict


def read_input(file: str) -> list[str]:
    """Returns instructions from input as a list of lines."""

    with open(f"./{file}.txt", "r") as f:
        return [line.strip("\n") for line in f.readlines()]


def clean_instructions(instructions: list[str]) -> list[str, tuple, tuple]:
    """Cleans up instructions, extracts verb and corner bulb coordinates.
    Returns as a list of str and two tuples."""

    cleaned = []

    for instruction in instructions:
        instruction = instruction.replace(" through ", " ")
        instruction = instruction.split(" ")
        verb = " ".join(instruction[0:-2])
        corner1 = [int(num) for num in instruction[-2].split(",")]
        corner2 = [int(num) for num in instruction[-1].split(",")]
        cleaned.append([verb, corner1, corner2])

    return cleaned


def follow_instruction(instruction: list[str, tuple, tuple],
                       bulbs: dict) -> dict:
    """Read one instruction and manipulates the bulb grid accordingly."""

    verb = instruction[0]
    rows = [instruction[1][0], instruction[2][0]]
    cols = [instruction[1][1], instruction[2][1]]

    if verb == "turn on":
        for row in range(min(rows), max(rows)+1):
            for col in range(min(cols), max(cols)+1):
                bulbs[(row, col)] += 1

    if verb == "turn off":
        for row in range(min(rows), max(rows)+1):
            for col in range(min(cols), max(cols)+1):
                if bulbs[(row, col)] > 0:
                    bulbs[(row, col)] -= 1

    if verb == "toggle":
        for row in range(min(rows), max(rows)+1):
            for col in range(min(cols), max(cols)+1):
                bulbs[(row, col)] += 2

    return bulbs


def count_brightness(bulbs: dict) -> int:
    """Count total lightbulb brightness in grid.
    Returns count."""

    return sum(bulbs.values())


if __name__ == "__main__":

    bulbs = defaultdict(lambda: 0)

    instructions = read_input("input")
    instructions = clean_instructions(instructions)

    for instruction in instructions:
        follow_instruction(instruction, bulbs)

    print(count_brightness(bulbs))
