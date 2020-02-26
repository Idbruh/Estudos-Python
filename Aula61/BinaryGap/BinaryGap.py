from itertools import dropwhile

# a generator that returns binary
# representation of the input
def getBinary(N):
    while N:
        yield N%2
        N //= 2

def longestGap(N):
    longestGap = 0
    currentGap = 0

    # we want to discard the initial 0's in the binary
    # representation of the input
    for i in dropwhile(lambda x: not x, getBinary(N)):
        if i:
            # a new gap is found. Compare to the maximum
            longestGap = max(currentGap, longestGap)
            currentGap = 0
        else:
            # extend the previous gap or start a new one
            currentGap+=1

    return longestGap