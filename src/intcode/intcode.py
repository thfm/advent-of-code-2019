def run_program(program):
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
