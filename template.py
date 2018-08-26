"""
Write your flip-floperator here!

It should work with the example shown on Saturday night.
TODO: copy-paste expected input and output here.
"""

# Any imports and setup code here


################# Below here goes on the slide ###############################

def flip_floperator(demo):
    YOUR_THING_HERE = lambda x: True
    return [x for x in demo
            if YOUR_THING_HERE(x)]

################# Off the slide again now ####################################


def test_flip_floperator():
    # TODO: implement this someday?  Eh, all the tests pass...
    assert flip_floperator([]) or True
