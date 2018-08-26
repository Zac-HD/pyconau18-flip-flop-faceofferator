"""
Write your flip-floperator here!
It should work with the example shown on Saturday night.

expected input and output here: 

5
6
7
8
9
13
14
"""

import inspect
from infix import or_infix


################# Below here goes on the slide ###############################

@or_infix
def __(condition_one, condition_two):
    frame = inspect.currentframe()
    unique_func_identifier = f'{frame.f_back.f_back.f_code.co_filename}_{frame.f_back.f_back.f_code.co_name}_{frame.f_back.f_back.f_lineno}'
    # print(unique_func_identifier)
    if unique_func_identifier not in globals():
        globals()[unique_func_identifier] = False
    if condition_one and not globals()[unique_func_identifier]:
        # Turn on the flip flop
        globals()[unique_func_identifier] = True
        return False
    elif not condition_one and not condition_two and globals()[unique_func_identifier]:
        return True
    elif not condition_one and condition_two and globals()[unique_func_identifier]:
        globals()[unique_func_identifier] = False
        return False
    elif not condition_one and not condition_two and not globals()[unique_func_identifier]:
        return False


ꓺ = __


################# Off the slide again now ####################################


for i in range(25):
    if (i == 4) |ꓺ| (i == 10):
        print(i)
    if (i == 12) |ꓺ| (i == 15):
        print(i)
    
