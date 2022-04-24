#takes instructions written in format for textbook and converts to format readable by http://morphett.info/turing/turing.html

#enter instructions here
instructions_str = """
(0,1,0,r,0)
(0,0,1,r,0)
(0,b,x,l,1)
"""

instructions_list = instructions_str.split('\n')



for instruction in instructions_list:
    if len(instruction)==0:
        continue
    # print(instruction)
    while instruction.find('(') != -1:
        instruction = instruction.replace('(', '')
    while instruction.find(')') != -1:
        instruction = instruction.replace(')', '')
    while instruction.find('b') != -1:
        instruction = instruction.replace('b', '_')
    while instruction.find(' ') != -1:
        instruction = instruction.replace(' ', '')

    # print(instruction)
    seq = instruction.split(',')
    # print(f'{seq=}')

    temp = seq[-1]
    seq[-1] = seq[-2]
    seq[-2] = temp

    if seq[-1]=='1':
        seq[-1]='0'
    
    if seq[0]=='1':
        seq[0]='0'

    for char in seq:
        print(f'{char} ', end='')
    
    print("")