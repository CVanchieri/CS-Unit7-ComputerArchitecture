'''
# LS-8
# lambda school 8-bit machine 


1111111
0000000

self.memory = [0] * 256

Memory bus (wires!) - can address 256 bytes of memory 
RAM - fast because we can access any address directly 
"storage" aka secondary memory aka hard drive 

Processor, REgisters, LA Cache, L2 Cache, Ram 
'''

# Cache hit!!!
# Cache miss...
import time 

matrix = []

size = 10 

for i in range(size):
    row = [0] * size
    matrix.append(row)

start_time = time.time()

for row in range(size):
    for col in range(size):
        matrix[row][col]

start_time = time.time()
for row in range(size):
    for col in range(size):
        matrix[col][row]
    
print(time.time() - start_time)



### how to create a stack ### 

# CPU can use to store 'variables that won't fit in registers 
# fucntoins case use it to store extra info 
# enables nested function calls 

# how to make a stack? 
# - storage 
# - Push  
# - POP
# - need to track the top of the stack 
'''
# push, decrement SP 'down', put value at that spot in menory
# pop, take value right where SP points, increment pointer 'up'

### what happens if we pop past the RAM we set aside for our stack? ###
# should we check before popping? no, would take up time and space, to much 'popping', the compiler does the check 
# prgrammer's JOB if asemply, complier's job if C or above 
# RESULT = stack underflow, 'pop' past memory available

### what happens if you underflow past RAM? ###
# 

### what happens if you go too far? ###
# stack overflow, overwrite the program 
# should we check before popping?

memory = [0] * 256

registers[7] = SP

FF: 00
FE: 00
FD: 00
FC: 00
FB: 00
FA: 00
F9: 00
F8:
F7:
F6:
F5:
F4: 00      <-- SP
F3: 05    
F2: 42
F1: 99 
F0:
. 
. 
. 
02:
03:
04:
05:
.
.
.

'''
"""
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
"""