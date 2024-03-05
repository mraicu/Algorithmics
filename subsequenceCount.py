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

start_time = time.time()


def getSubsequenceCount(hname, buffer):
    nr = 0
    for i in range(len(buffer) - 2):
        if hname[0] == buffer[i]:
            for j in range(i + 1, len(buffer) - 1):
                if hname[1] == buffer[j]:
                    for k in range(j + 1, len(buffer)):
                        if hname[2] == buffer[k]:
                            nr += 1

    return nr


assert (getSubsequenceCount("ABC", "ABCBABC"))


def count(hName, buffer):
    """
    Dynamic Programming
    """
    n = len(hName)
    m = len(buffer)

    # create a matrix to store results
    table = [[0] * (n + 1) for _ in range(m + 1)]

    # first column is 1
    for i in range(m + 1):
        table[i][0] = 1

    # the element will be the:
    # up + left, if the characters are the same
    # else: up element
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if buffer[i - 1] == hName[j - 1]:
                table[i][j] = table[i - 1][j - 1] + table[i - 1][j]
            else:
                table[i][j] = table[i - 1][j]
    # last element is the solution
    return table[m][n]


assert getSubsequenceCount("ABC", "ABCBABC") == 5
assert count("ABC", "ABCBABC") == 5
