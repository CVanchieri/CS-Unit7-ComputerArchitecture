"""CPU functionality."""
import sys
LDI     = 0b10000010
PRN     = 0b01000111
HLT     = 0b00000001
MUL     = 0b10100010
POP     = 0b01000110
PUSH    = 0b01000101

class CPU:
    """Main CPU class."""
### Add list properties to the CPU class to hold 256 bytes of memory and 8 general-purpose registers ###
    def __init__(self):
        """Construct a new CPU."""
        self.reg = [0] * 8 
        self.ram = [0] * 256
        self.pc = 0
        self.halted = False
        self.SP = 3 # start the SP at 3 
        self.address = 0
        """list or dictionary of functions that you can index by opcode value, fetch the instruction value from RAM, 
        then use that value to look up the handler function in the branch table, then call it.""" 
        self.bt = { # branch table
            LDI: self.oper_ldi,
            PRN: self.oper_prn,
            HLT: self.oper_hlt,
            MUL: self.oper_mul,
            POP: self.oper_pop,
            PUSH: self.oper_push,
            }

    """branch table operations"""
    ### LDI operation ###
        # this instruction sets a specified register to a specified value
    def oper_ldi(self, oper_a, oper_b):
        self.reg[oper_a] = oper_b
    
    ### PRN operation ###
    # very similar process to adding LDI, but the handler is simpler, See the LS-8 spec
    def oper_prn(self, oper_a, oper_b):
        print(self.reg[oper_a])

    ### HLT operation ###
    # exit the loop if a HLT instruction is encountered, regardless of whether or not there are more lines of code in the LS-8 program you loaded
    def oper_hlt(self, oper_a, oper_b):
        sys.exit(0)

    ### MUL operation ###
    # multiply the values in two registers together and store the result in register
    def oper_mul(self, oper_a, oper_b):
        self.alu("MUL", oper_a, oper_b)

    ### POP operation ### 
    # set reg[oper_a] with the pop_val method
    def oper_pop(self, oper_a, oper_b):
        self.reg[oper_a] = self.pop_val()

    ### PUSH operation ###
    # use push_val method on reg[oper_a]
    def oper_push(self, oper_a, oper_b):
        self.push_val(self.reg[oper_a])

    """CPU methods"""
    ### ram_read method ###
    # ram_read() should accept the address to read and return the value stored there 
    def ram_read(self, mar):
        address = self.ram[mar]
        return address

    ### ram_write method ###
    # ram_write() should accept a value to write, and the address to write it to
    def ram_write(self, mdr, mar):
        self.ram[mar] = mdr

    ### push method ###
    # decrement the SP, push the value stored in register to the address of the SP
    def push_val(self, val):
        self.reg[self.SP] -= 1
        self.ram_write(val, self.reg[self.SP])

    ### pop method ###
    # pop the value at the top of the stack into the given register, Copy the value, increment SP
    def pop_val(self):
        val = self.ram_read(self.reg[self.SP])
        self.reg[self.SP] += 1
        return val

    ### load method ###
    # use the command line arguments to open a file, read in its contents line by line, and save appropriate data into RAM
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
    def run(self):
        """Run the CPU."""
        while not self.halted: # loop while halted is not False 
            instruction = self.ram[self.pc] # set instruction to the ram[self.pc]
            oper_a = self.ram_read(self.pc + 1) # set the oper_a to the ram_read(self.pc + 1)
            oper_b = self.ram_read(self.pc + 2) # set the oper_b to the ram_read(self.pc + 2)
            instruct_length = (instruction >> 6) + 1 # set the instruct_length to instruction shift R 6 + 1 
            instruct_set_pc = ((instruction >> 4) & 0b1) == 1 # set the instruct_set_pc to instruction shift R 4 and 0b1 equal to 1 

            if instruction in self.bt: # if the instruction is in the branch table
                self.bt[instruction](oper_a, oper_b) # run the instruction with operations
       
            if instruct_set_pc != 1: # if the value is not equal to 1
                self.pc += instruct_length # increment pc by instruct_length

    