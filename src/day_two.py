def read_input_program():
    instructions = open("res/day_two_inputs.txt").read().split(",")
    return list(map(int, instructions))


def run_intcode_program(program):
    memory = list(program)
    pointer = 0
    opcode = memory[pointer]
    while opcode != 99:
        a = memory[memory[pointer + 1]]
        b = memory[memory[pointer + 2]]
        result_addr = memory[pointer + 3]

        if opcode == 1:
            memory[result_addr] = a + b
        elif opcode == 2:
            memory[result_addr] = a * b

        pointer = pointer + 4
        opcode = memory[pointer]
    return memory


program = read_input_program()
for noun in range(100):
    for verb in range(100):
        program[1] = noun
        program[2] = verb
        if run_intcode_program(program)[0] == 19690720:
            print(100 * noun + verb)
            break
