def read_input(file: str) -> list[str]:
    """Returns instructions from input as a list of lines."""

    with open(f"./{file}.txt", "r") as f:
        return [line.strip("\n") for line in f.readlines()]


def clean_instructions(instructions: list[str]) -> list[str]:
    """Extracts components in each instruction.
    Returns list of instructions."""

    cleaned = {}
    for instruction in instructions:
        exp, target = instruction.split(" -> ")
        cleaned[target] = exp.split()

    return cleaned


def find_wire(chain):

    if all([not x.isnumeric() for x in chain[0][:-1]]):
        return chain
    else:
        for


def chain_to_a(instructions: list[dict]) -> list[dict]:
    """Reorder wires that transmit signals to wire a.
    Returns a list of wires and signals."""

    gates = ["AND", "OR", "LSHIFT", "RSHIFT", "NOT"]
    chain = [instructions["a"] + ["a"]]

    i = 1
    while any([not x.isnumeric() for x in chain[0][:-1]]):
        for instruction in chain[0:i]:
            for item in instruction[:-1]:
                if item not in gates and not item.isnumeric():
                    chain.insert(0, instructions[item]+[item])
                    i += 1

    return chain

# def follow_instruction(instruction: str, wires: dict) -> None:
#     """Keeps track of signal transformation and transfer.
#     Returns nothing."""

#     keys = wires.keys()

#     if len(instruction) == 2:
#         signal = int(instruction[0])
#     elif len(instruction) == 3:
#         if instruction[1] in keys:
#             value = wires[instruction[1]]
#             binary = bin(value).replace("0b", "").zfill(16)
#             complement = "".join([str(abs(int(char)-1))
#                                   for char in binary])
#             signal = int(complement, 2)
#     elif "AND" in instruction:
#         if instruction[0] in keys and instruction[2] in keys:
#             signal = wires[instruction[0]] & wires[instruction[2]]
#     elif "OR" in instruction:
#         signal = wires[x] | wires[y]
#     elif "LSHIFT" in instruction:
#         signal = wires[x] << int(y)
#     elif "RSHIFT" in instruction:
#         signal = wires[x] >> int(y)

#     wires[instruction[-1]] = int(signal)


if __name__ == "__main__":

    instructions = read_input("input")
    instructions = clean_instructions(instructions)
    instructions_to_a = chain_to_a(instructions)
    print(instructions_to_a)

    # wires = {}

    # for instruction in instructions:
    #     follow_instruction(instruction, wires)

    # print(wires["a"])
