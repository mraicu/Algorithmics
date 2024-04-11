'''
Coreference Resolution

Co-reference resolution is a natural language processing (NLP) task concerned with
grouping mentions of the same concept from a text.

Write a Python function that takes as an input a list of strings representing the entities
(i.e. names of people, companies or products) extracted from a text and outputs a string with the following specifications:

The mentions of the same entity follow each other, separated by a semicolon (;) and a space.
The mentions of the same entity are sorted by their length in reverse order
The groups of mentions are sorted in alphabetic order (based on the characters in the first element in the group),
separated by a dot and a space
The function is case-insensitive (the entity is the same, even if written in upper case or lower case)
Basic abbreviations may also appear. You should account for them ("LA" would match Los Angeles).

Examples:

Input: ["John", "Apple", "JOHN S", "John Smith", "APPLE Inc."]
Output: APPLE Inc.; Apple. John Smith; JOHN S; John

Input: ["IBM", "International Business Machines "APPLE Inc.", "Apple"]
Output: APPLE Inc.; Apple. International Business Machines; IBM
'''


# neterminat
def flatten(A):
    rt = []
    for i in A:
        if isinstance(i, list):
            rt.extend(flatten(i))
        else:
            rt.append(i)
    return rt


def CoreferenceResolution(strArr):
    input = sorted([s.lower() for s in strArr])
    rez = []
    # check if substring
    for i in range(len(input)):
        crt_rez = []
        for j in range(i, len(input)):
            if input[i] in input[j]:
                fl = flatten(rez)
                if input[j] not in fl:
                    crt_rez.append(input[j])
        rez.append(crt_rez)

    rez.remove([])

    arr = []
    for r in rez:
        if len(r) == 1:
            arr.append(r)


    if isAbbreviation(arr[0], arr[1]):
        pass
    # for el in arr
    return rez, arr


def isAbbreviation(abbreviation, full_phrase):
    full_phrase_string = ''.join(full_phrase)
    index = 0
    for char in abbreviation:
        if char in full_phrase_string[index:]:
            index = full_phrase_string.index(char, index) + 1
        else:
            return False

    return True


print(CoreferenceResolution(["IBM", "International Business Machines", "APPLE Inc.", "Apple"]))
