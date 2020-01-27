from copy import deepcopy

MAX_PARAMS = 3

# The number of parameters used by each instruction
PARAM_COUNTS = {
    "01": 2,
    "02": 2,
    "03": 0,
    "04": 1,
    "05": 2,
    "06": 2,
    "07": 2,
    "08": 2
}


def decode_instruction(instruct_code):
    instruct_code = str(instruct_code)
    # Fills the instruction code up to a certain standardised length
    while len(instruct_code) < MAX_PARAMS + 2:
        instruct_code = "0" + instruct_code
    opcode = instruct_code[-2:]
    param_modes = list(instruct_code[:3])
    param_modes.reverse() # Param modes are taken from right to left
    return (opcode, param_modes)


# See day_two.py 'run_intcode_program' for further details
def run_intcode_program(program):
    memory = deepcopy(program)
    pointer = 0

    while pointer < len(memory):
        opcode, modes = decode_instruction(memory[pointer])
        if opcode == "99":
            break
        pointer += 1

        param_count = PARAM_COUNTS.get(opcode)
        if param_count is None:
            print(f"[ERROR]: Invalid opcode ({opcode})")
            break

        params = memory[pointer:pointer + param_count]
        values = []
        for i, param in enumerate(params):
            values.append(memory[param] if modes[i] == "0" else param)
        pointer += param_count

        result_addr = memory[pointer]
        result = None
        if opcode == "01":
            result = sum(values)
        elif opcode == "02":
            product = 1
            for num in values:
                product *= num
            result = product
        elif opcode == "03":
            result = int(input("[03]: Enter an integer: "))
        elif opcode == "04":
            print(values[0])
        elif opcode == "05":
            if values[0] != 0:
                pointer = values[1]
        elif opcode == "06":
            if values[0] == 0:
                pointer = values[1]
        elif opcode == "07":
            result = 1 if values[0] < values[1] else 0
        elif opcode == "08":
            result = 1 if values[0] == values[1] else 0

        # Not all instructions return an output value
        if result is not None:
            memory[result_addr] = result
            pointer += 1


def read_input_program(filename):
    instructions = open(filename).read().split(",")
    return [int(instruct) for instruct in instructions]
