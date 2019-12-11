from intcode import intcode


def read_input_program():
    instructions = open("res/day_two_inputs.txt").read().split(",")
    return list(map(int, instructions))


program = read_input_program()
for noun in range(100):
    for verb in range(100):
        program[1] = noun
        program[2] = verb
        result = intcode.run_program(program)[0]
        if result == 19690720:
            print(100 * noun + verb)
            break
