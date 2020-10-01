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
### In CPU, add method ram_read() and ram_write() that access the RAM inside the CPU object. ###
### ram_read() should accept the address to read and return the value stored there. ###
    def ram_read(self, address):
        print(self.ram[address])
### ram_write() should accept a value to write, and the address to write it to. ###
    def ram_write(self, address, instruction):
        self.ram[address] = instruction

        ### Hardcoded a program ###
        program = [
            # From print8.ls8
            0b10000010, # LDI R0,8
            0b00000000,
            0b00001000,
            0b01000111, # PRN R0
            0b00000000,
            0b00000001, # HLT
        ]

        for instruction in program:
            self.ram[address] = instruction
            address += 1

    def alu(self, op, reg_a, reg_b):
        """ALU operations."""
        if op == "ADD":
            self.reg[reg_a] += self.reg[reg_b]
        #elif op == "SUB": etc
        else:
            raise Exception("Unsupported ALU operation")

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

    def run(self):
        """Run the CPU."""
        while not self.halted:
            instruction = self.ram[self.pc]
            ### Add the LDI instruction ###
            ### This instruction sets a specified register to a specified value. 
            if instruction == 0b10000010: # equal to LDI
                value = self.ram[self.pc + 2]
                register_num = self.ram[self.pc + 1]
                self.reg[register_num] = value 
                self.pc += 3
            ### Add the PRN instruction ###
            ### Very similar process to adding LDI, but the handler is simpler. See the LS-8 spec. 
            elif instruction == 0b01000111: # equal to PRN
                register_num = self.ram[self.pc + 1]
                print(self.reg[register_num])
                self.pc += 2
            ### Add the HLT instruction define to cpu.h. ###
            ### exit the loop if a HLT instruction is encountered, regardless of whether or not there are more lines of code in the LS-8 program you loaded. 
            elif instruction == 0b00000001: # equal to HLT
                self.halted = True 
                self.pc += 1
            ### Handle an unkown instruction ###
            ### return an error if instruction is unkown. 
            else:
                print(f"Error: unkown instruction at index : {self.pc}")
                sys.exit(1)


