from os import popen
import sys
#                   AABCDDDD
PRINT_TIM       = 0b00000001
HALT            = 0b00000010
PRINT_NUM       = 0b01000011
SAVE            = 0b10000100 # LDI 
PRINT_REGISTER  = 0b01000101
ADD             = 0b10100110
PUSH            = 0b01000111
POP             = 0b01001000

# is_alu_op = (command >> 5) & 0b001 == 1

memory = [0] * 256

def load_memory():
    if (len(sys.argv)) != 2:
        print("remember to pass the second file name")
        print("usage: python3 fileio.py <second_file_name.py>")
        sys.exit()

    address = 0
    try:
        with open(sys.arg[1]) as f: # this method will 'close' the file after exception
            for line in f:
                # parse the file to isolatethe binary 
                # print(line.find('#'))
                possible_number = line[:line.find('#')]
                if possible_number == '':
                    continue # skip to next iteration 

                instruction = int(possible_number, 2)
                memory[address] = instruction

    except FileNotFoundError:
        print(f"error from {sys.argv[0]}: {sys.argv[1]} not found")
        sys.exit()

load_memory()

'''
PRINT_TIM,
PRINT_NUM,
42,
SAVE,
2,
10,
SAVE,
3,
10,
ADD,
2,
3,
PRINT_REGISTER,
2,
HALT
'''

# cabinets in your shop: registers 
# storage unit: cache 
# warehouse outside town: RAM 

# registers
# physically located on CPU, treat as variables 



# R0-R7
registers = [0] * 8
registers[7] = 0xF4


# cpu should now step through memory and take actions based on commands it finds

# a data-driven machine

# program counter 
pc = 0
running = True 

# where to start our stack 
# 
class Stack: # stack class
    def __init__(self): # initializer constructor method
        self.size = 0 # set size to 0
        self.items = [] # set storage items to empty list

    def __len__(self): # method to show the length
        return self.size

    def push(self, value): # method to add a value
        self.items.append(value) # append the value to items list
        self.size += 1 # add 1 to the length

    def pop(self): # method to remove a value
        if self.items != []: # if items list is not empty
            self.size -= 1 # remove 1 from the length
            return self.items.pop()


while running:
    command = memory[pc]

    num_args = command >> 6

    if command == PRINT_TIM:
        print("tim!")

    elif command == PRINT_NUM:
        # number = memory[pc + 1]
        number = memory[pc]
        print(number)

    elif command == SAVE:
        # get out the arguments 
        # pc+1 is reg idx, pc+2 value 
        reg_idx = memory[pc + 1]
        value = memory[pc + 2]

        # put the value into the correct register 
        registers[reg_idx] = value 

        # increment program counter by 2 
        ## 2 + 1 below == 3=byte command 

    elif command == PRINT_REGISTER:
        # get out the argument 
        reg_idx = memory[pc + 1]

        # the argument is used as the pointer 
        value = registers[reg_idx]
        print(value)

    elif command == ADD:
        reg_idx_1 = memory[pc + 1]
        reg_idx_2 = memory[pc + 2]

        # add regs together 
        registers[reg_idx_1] = registers[reg_idx_1] + registers[reg_idx_2]

    elif command == HALT:
        running = False

    elif command == PUSH: 
        # get a value

        # where is the SP
        registers[7] -= 1
        # decrement SP

        # copy value in given register adress pointed by SP 
        reg_idx = memory[pc + 1]
        value = registers[reg_idx]
        SP = registers[7]
        memory[SP] = value

    elif command == POP:
        # copy address from pointer 
        SP = registers[7]

        value = memory[SP]
        # get value from address 
        # put the value in register  

        pass
    else:
        print('Commmand not known!')
        running = False

    pc += 1 + num_args

