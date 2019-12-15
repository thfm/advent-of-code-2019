from copy import deepcopy

MAX_PARAMS = 3

PARAM_COUNTS = {
    "01": 2,
    "02": 2,
    "03": 0,
    "04": 1
}


def decode_instruction(instruct_code):
    instruct_code = str(instruct_code)
    while len(instruct_code) < 5:
        instruct_code = "0" + instruct_code
    opcode = instruct_code[-2:]
    param_modes = list(instruct_code[:3])
    param_modes.reverse()
    return (opcode, param_modes)


def run_intcode_program(program):
    memory = deepcopy(program)
    pointer = 0

    while pointer < len(memory):
        opcode, p_modes = decode_instruction(memory[pointer])
        if opcode == "99":
            break
        pointer += 1

        param_count = PARAM_COUNTS.get(opcode)
        if param_count is None:
            print(f"[ERROR]: Invalid opcode ({opcode})")
            break

        in_params = memory[pointer:pointer + param_count]
        in_values = []
        for i, param in enumerate(in_params):
            in_values.append(memory[param] if p_modes[i] == "0" else param)
        pointer += param_count

        result_addr = memory[pointer]

        result = None
        if opcode == "01":
            result = sum(in_values)
        elif opcode == "02":
            product = 1
            for num in in_values:
                product *= num
            result = product
        elif opcode == "03":
            result = int(input("[03]: Enter an integer: "))
        elif opcode == "04":
            print(in_values[0])

        if result is not None:
            memory[result_addr] = result
            pointer += 1


def read_input_program(filename):
    instructions = open(filename).read().split(",")
    return [int(instruct) for instruct in instructions]


INPUT_PROGRAM = read_input_program("res/day_five_inputs.txt")
run_intcode_program(INPUT_PROGRAM)
