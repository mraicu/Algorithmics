"""
Two strings are said to be the same if they are of the same length and have the same character at each index.
Backspacing in a string removes the previous character in the string.

Given two strings containing lowercase English letters and the character '#' which represents a backspace key,
determine if the two final strings are equal. Return 1 if they are equal or O if they are not.
Note that backspacing an empty string results in an empty string.

Example

s1 = 'axx#bb#c'
s2 = 'axbd#c#c'

In the first string, one 'x' and one 'b' are backspaced over.
The first string becomes axbc.
The second string also becomes axbc. The answer is 1.
"""

def compareStrings(s1, s2):
    """
    Determine if the two strings are equal.
    :param s1: first string
    :type s1: str
    :param s2: second string
    :type s2: str
    :return: True/False
    """
    i=len(s1)-1
    j=len(s2)-1
    while i:
        if s1[i]!=s2[j] and s1[i]!='#' and s2[j]!='#':
            return False
        if s1[i]=='#':
            i-=2
        else:
            i -= 1
        if s2[j]=='#':
            j-=2
        else :
            j-=1
    return True

assert compareStrings('axx#bb#c', 'axbd#c#c')
