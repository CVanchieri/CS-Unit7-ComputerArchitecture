import sys

# open a filename 

###
'''
try: 
    f = open('ls8/examples/print8.ls8', 'r') # this method does not 'close' the file after exception
    lines = f.read()
    print(lines)

    raise Exception('hi')
except:
    print(f.closed)
'''
###
# sys.argv

if (len(sys.argv)) != 2:
    print("remember to pass the second file name")
    print("usage: python3 fileio.py <second_file_name.py>")
    sys.exit()

try:
    with open(sys.arg[1]) as f: # this method will 'close' the file after exception
        for line in f:
            # parse the file to isolatethe binary 
            # print(line.find('#'))
            possible_number = line[:line.find('#')]
            if possible_number == '':
                continue # skip to next iteration 
            regular_int = int(possible_number, 2)

            print(regular_int)
            #line = line[:line.find('#')].strip()

except FileNotFoundError:
    print(f"error from {sys.argv[0]}: {sys.argv[1]} not found")
    sys.exit()

###



