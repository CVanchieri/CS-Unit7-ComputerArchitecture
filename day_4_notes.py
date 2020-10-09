import sys
''' subroutines video notes '''
# like functions, same concept from higher-level languages 
# in assembly, we CALL a subroutine at a particular address
# then we RET (return) from that subroutine to pick up where we left off, just like a function does in a high-level language
# subroutines use the computer 'stack'

## limitations for subroutines ## 
# can not pass arguments 
# no return values, returns to caller 
# it is possible....

### the process ###
# when we CALL a subroutine, we need to store the return address somewhere so we knwo where to go when we hit the RET instruction 
# CPUs tend to use the stack for this 
# CALL will push the address of the instruction afte3r it on the stack, then move the PC to the subroutine address
# RET will pop the return address off the stack, and store it in the PC 

## uses 
# use anyplace you would use functions in a higher-levle language 
# DRY principle 
# d not repeat yourself 
# high level languages evetually use CALL and RET deep down to implement functions 

''' subroutines class notes '''
# also known as 'functions'
# use CALL and RET to build

def my_func(a, b):
    print(a, b)

def my_func2():
    my_func(1, 2)

# for other opcodes, we pass parameters by palcing them after the command in the program

## can we pass parameters to our subroutine by placing them after CALL?
# CALL spec does not allow this 
# how to pass paramneters from one functio nto another 

# could use the stack and memry addresses!
# could store params in registers before calling 
# cant do nested subroutines 

def mult2print(our_num):
    our_num += our_num 
    print(our_num)
    return
    
mult2print(10)
mult2print(15)
mult2print(18)
mult2print(30)
sys.exit(1)

### CALL ###
# in our project, uses registers to pass params to oru subroutine 
### RET ###
# 

'''
700: 0
699: 2
698: 2 
697: 3
696: 6  
695: 6      <-- SP
694: 3
693: 6 

R0 = 6

def add(x, y):
    z = x + y
    return z

def mult(a, b):
    z = a * b
    x = add(a, b)
    return z

def main():
    a = 2 

    c = mult(2,3)

    d = 42
'''