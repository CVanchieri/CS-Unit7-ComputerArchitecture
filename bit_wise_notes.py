'''
operator  boolean operator    bitwise operators
# AND            &&                    &
# OR             ||                    |
# NOT            !                     ~
# XOR                                  ^
# NAND              
'''
# xor: exclusive or. one and only one can be true 
## (true xor false) --> true 
## (true xor true) --> false
## (false xor false) --> false 

# and: bot statements are true 
## (true and true) --> true 
## (true and false) --> false 
'''
### & ###
    1011
  & 0110
    ----
    0010

### masking ###
    10101011
  & 00000001
    --------
    00000001

### or ###
    10101011
 or 00000001
    --------
    10101011

### not ###
1010 --> 0101

### xor ###
    10101011
  ^ 00000001
    --------
    10101010

### bit shifting ###
    1101 >> 1 # shift right 
     110

    1101 >> 2 # shift right 
      11

# extract from the command the number of arguments this command takes to find out how much to move the program counter 
    
    1 << 1101 # shift left
    1010

    2 << 1101 # shift left
   10100



    ||
    vv
    10010101 >> 6
          10
    00000010


ADD
  |
  v
10100000
     101


'''