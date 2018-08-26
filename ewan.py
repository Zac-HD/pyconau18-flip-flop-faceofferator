#! /usr/bin/python3
# Flip Floperator -- PyCon AU 2018 -- like ".." in Ruby
#
# http://nithinbekal.com/posts/ruby-flip-flop/
# https://blog.newrelic.com/engineering/weird-ruby-part-3-fun-flip-flop-phenom/
#
# turns on when startwhen condition is achieved; stays on until
# stopwhen condition is achieved.
#
# Output is item that triggered startwhen through item that triggerd
# stopwhen inclusive.  May trigger repeatedly.
#
# This is somewhat clumsy to use without the syntatic sugar :-)
#
# Two variations implemented:
# - a context manager/callable
# - a generator function
#
# Of the two the context manager/callable is closer to the operator syntax,
# but requires more setup; the generator function is more pythonic.
#
# See challenge:
# https://twitter.com/tveastman/status/1033254994110103552
#
# and elaborate, magical, nearly operator answer (with off-by-one error):
# https://twitter.com/_lewisjb/status/1033337618702856193
#
# Written by Ewen McNeill <ewen@naos.co.nz>, 2018-08-25
# Updated by Ewen McNeill <ewen@naos.co.nz>, 2018-08-26
#---------------------------------------------------------------------------

import sys

# Flop Flop Context / Callable
#
class FlipFlopContext:
    def __init__(self):
        self.included = False

    def __enter__(self):
        return self

    def __exit__(self, *exc):
        pass

    def __call__(self, startnow, finishafterthis):
        if not self.included:
           self.included = startnow

        include_current = self.included

        if self.included:
           self.included = not finishafterthis

        return include_current

def testFlipFlopContext():
    printed = False
    with FlipFlopContext() as ff:
        for item in sys.argv[3:]:
            if ff(item == sys.argv[1], item == sys.argv[2]):
                print(item, end=" ")
                printed = True

    if printed:
        print("")

#---------------------------------------------------------------------------
# Flip Flop Generator
#
# Args: 
# startwhen - callable: if evaluates true, start including items with this one
# stopwhen  - callable: if evaluates false, stop including items after this one
# iterable  - source of candidate itemss
#
def FlipFlopGenerator(startwhen, stopwhen, iterable):
    included = False
    for item in iterable:
        # Check if we need to start from this item
        if not included:
           included = startwhen(item)

        if included:
            yield item

        # Check if we should stop after this item
        if included:
           included = not stopwhen(item)

def testFlipFlopGenerator():
    print(" ".join(FlipFlopGenerator((lambda x: x == sys.argv[1]), 
                                     (lambda x: x == sys.argv[2]),
                                     sys.argv[3:])))

def dotest():
    if len(sys.argv) <= 3:
        print("Usage: {0} STARTAT STOPAT item [item [...]]".
              format(sys.argv[0]), file=sys.stderr)
        sys.exit(1)

    print("Flip Flop Context:")
    testFlipFlopContext()

    print("")

    print("Flip Flop Generator:")
    testFlipFlopGenerator()

if __name__ == "__main__":
    dotest()
