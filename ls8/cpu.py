"""CPU functionality."""
import sys

class CPU:
    """Main CPU class."""
### Add list properties to the CPU class to hold 256 bytes of memory and 8 general-purpose registers. ###
    def __init__(self):
        """Construct a new CPU."""
        self.reg = [0] * 8 
        self.ram = [0] * 256
        self.pc = 0
        self.halted = False
        
        self.instructions = { # dictionary with the necessary isntructions.
                            'LDI' : 0b10000010,
                            'PRN' : 0b01000111,
                            'HLT' : 0b00000001,
                            'MUL' : 0b10100010
                            }

        self.address = 0
### In CPU, add method ram_read() and ram_write() that access the RAM inside the CPU object. ###
### ram_read() should accept the address to read and return the value stored there. ###
    def ram_read(self, address):
        print(self.ram[address])
### ram_write() should accept a value to write, and the address to write it to. ###
    def ram_write(self, address, instruction):
        self.ram[address] = instruction
        self.address += 1

        ### Hardcoded a program ###
       # program = [
            # From print8.ls8
           # 0b10000010, # LDI R0,8
           # 0b00000000,
           # 0b00001000,
           # 0b01000111, # PRN R0
            #0b00000000,
           # 0b00000001, # HLT
      #  ]

    ### Add the load method ###
    ### use the command line arguments to open a file, read in its contents line by line, and save appropriate data into RAM.
    def load(self):
        """Load a program into memory."""
        program_name = sys.argv[1]
        
        with open(program_name) as f:
            for line in f:
                line = line.split('#')[0]
                line = line.strip() # Lose whitespace
                
                if line == '':
                    continue
                
                val = int(line, base=2)
                self.ram[self.address] = val
                self.address +=1

    ### alu method ###
    def alu(self, op, reg_a, reg_b):
        """ALU operations."""

        if op == "ADD":
            self.reg[reg_a] += self.reg[reg_b]
        #elif op == "SUB": etc
        else:
            raise Exception("Unsupported ALU operation")

    ### trace method ###
    def trace(self):
        """
        Handy function to print out the CPU state. You might want to call this
        from run() if you need help debugging.
        """
        print(f"TRACE: %02X | %02X %02X %02X |" % (
            self.pc,
            #self.fl,
            #self.ie,
            self.ram_read(self.pc),
            self.ram_read(self.pc + 1),
            self.ram_read(self.pc + 2)
        ), end='')

        for i in range(8):
            print(" %02X" % self.reg[i], end='')
        print()

    ### run method ###
    """ *** need to work into branch tsble *** """
    def run(self):
        """Run the CPU."""
        print('--- Analyzing Results ---')
        while not self.halted:
            instruction = self.ram[self.pc]
            ### Add the LDI instruction ###
            ### This instruction sets a specified register to a specified value. 
            if instruction == self.instructions['LDI']: # equal to LDI
                value = self.ram[self.pc + 2]
                register_num = self.ram[self.pc + 1]
                self.reg[register_num] = value 
                self.pc += 3
            ### Add the PRN instruction ###
            ### Very similar process to adding LDI, but the handler is simpler. See the LS-8 spec. 
            if instruction == self.instructions['PRN']: # equal to PRN
                register_num = self.ram[self.pc + 1]
                print(self.reg[register_num])
                self.pc += 2
            ### Add the HLT instruction define to cpu.h. ###
            ### exit the loop if a HLT instruction is encountered, regardless of whether or not there are more lines of code in the LS-8 program you loaded. 
            if instruction == self.instructions['HLT']: # equal to HLT
                self.halted = True 
                self.pc += 1
            ### Add the MUL instruction, this is an instruction handled by the ALU ###
            ### Multiply the values in two registers together and store the result in registerA. 
            if instruction == self.instructions['MUL']:
                reg_num1 = self.reg[self.ram[self.pc + 1]]
                reg_num2 = self.reg[self.ram[self.pc + 2]]
                self.reg[self.ram[self.pc + 1]] = reg_num1 * reg_num2
                self.pc += 3

'''
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

class Stack:
    #Constructor
    def __init__(self):
        self.stack = list()
        self.maxSize = 8
        self.top = 0
    #Adds element to the Stack
    def push(self,data):
        if self.top>=self.maxSize:
            return ("Stack Full!")
        self.stack.append(data)
        self.top += 1
        return True
    #Removes element from the stack
    def pop(self):
        if self.top<=0:
            return ("Stack Empty!")
        item = self.stack.pop()
        self.top -= 1
        return item
       
    #Size of the stack
    def size(self):
        return self.top
'''