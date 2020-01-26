from copy import deepcopy


def read_input_program(filename):
    args = open(filename).read().split(",")
    return [int(arg) for arg in args]


# Calculates the product of each item in an iterable
# (e.g. a list)
def mul(iterable):
    product = 1
    for item in iterable:
        product *= item
    return product


# Runs a simple intcode algorithm on a given instruction
# sequence (the program)
def run_intcode_program(program):
    # Makes a copy of the memory so as not to change the original
    # program values
    memory = deepcopy(program)
    pointer = 0
    while pointer < len(program):
        opcode = memory[pointer]
        if opcode == 99: # 'Halt' opcode
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
