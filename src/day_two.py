from copy import deepcopy


def read_input_program(filename):
    args = open(filename).read().split(",")
    return [int(arg) for arg in args]


def mul(iterable):
    product = 1
    for item in iterable:
        product *= item
    return product


def run_intcode_program(program):
    memory = deepcopy(program)
    pointer = 0
    while pointer < len(program):
        opcode = memory[pointer]
        if opcode == 99:
            break

        input_params = memory[pointer + 1:pointer + 3]
        input_values = [memory[addr] for addr in input_params]
        output_addr = memory[pointer + 3]

        result = 0
        if opcode == 1:
            result = sum(input_values)
        elif opcode == 2:
            result = mul(input_values)
        memory[output_addr] = result

        pointer += 4
    return memory


input_program = read_input_program("res/day_two_inputs.txt")
for noun in range(99 + 1):
    for verb in range(99 + 1):
        input_program[1] = noun
        input_program[2] = verb
        result = run_intcode_program(input_program)[0]
        if result == 19690720:
            print(100 * noun + verb)
            break
