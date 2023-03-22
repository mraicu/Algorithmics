import time
"""
Given the hacker's name and a string buffer, determine the number of times the name
appears as a subsequence in the buffer.  A subsequence is created by eliminating any 
number of characters from a string (possibly 0) without changing the order of the characters retained.

For simplicity, the hacker's name will always be of size 3.

Example

hname="ABC" buffer = "ABCBABC"

The hname appears 5 times as a subsequence in the buffer at 1-indexed positions of 
(1, 2, 3), (1, 2, 7), (1, 4, 7), (1, 6, 7), and (5, 6, 7). The answer is 5.

"""

start_time=time.time()
def getSubsequenceCount(hname, buffer):
    nr=0
    for i in range(len(buffer)-2):
        if hname[0]==buffer[i]:
            for j in range(i+1, len(buffer)-1):
                if hname[1] == buffer[j]:
                    for k in range(j+1, len(buffer)):
                        if hname[2] == buffer[k]:
                            nr+=1

    return nr

assert(getSubsequenceCount("ABC", "ABCBABC"))
l=["E"]*500
assert(getSubsequenceCount("EEE", l)==20708500)

print("time: ", (time.time() - start_time) * 10 ** 3, "ms")