def read_input(file: str) -> list[str]:
    """Returns input as a list of strings."""

    with open(f"{file}.txt", "r") as f:
        return [line.strip("\n")
                for line in f.readlines()]


def code_memory_difference(string: str) -> int:
    """Returns the number of characters in difference
    between a string code and memory for a string value"""

    count = 2
    i = 1
    while i < len(string)-1:
        if string[i:i+2] in [r'\\', r'\"']:
            count += 1
            i += 2
        elif string[i:i+2] == r'\x':
            count += 3
            i += 4
        else:
            i += 1

    return count


if __name__ == "__main__":

    strings = read_input("input")
    print(
        sum(
            [code_memory_difference(string)
             for string in strings]
        )
    )
