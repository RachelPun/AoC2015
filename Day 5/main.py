def read_lines(filename: str) -> list[int]:

    with open(f"./{filename}.txt") as file:
        lines = [line.strip("\n") for line
                 in file.readlines()]

    return lines


def check_3_vowels(line: str) -> bool:
    """Return boolean of whether there are at least 3 vowels in the line."""

    vowel_count = sum([line.count(vowel) for vowel
                       in ["a", "e", "i", "o", "u"]])

    return vowel_count >= 3


def check_double_letter(line: str) -> bool:
    """Return boolean of whether there is at least 1 letter that
    appears twice in a row."""

    for i in range(len(line)-1):
        if line[i] == line[i+1]:
            return True

    return False


def check_no_certain_strings(line: str) -> bool:
    """Return boolean of whether the line does not contain any of
    [ab, cd, pq, xy]."""

    return all([combo not in line
                for combo in ["ab", "cd", "pq", "xy"]])


def check_all_checks(line: str) -> bool:
    """Return boolean of whether the line fulfills
    all 3 requirements"""

    return all([check_3_vowels(line),
                check_double_letter(line),
                check_no_certain_strings(line)])


if __name__ == "__main__":

    strings = read_lines("input")

    print(sum(
        [1 for string in strings
         if check_all_checks(string)]
    ))
