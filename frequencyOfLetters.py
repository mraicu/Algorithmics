"""
INPUT: string strParam
OUTPUT: The strParam sorted by the frequency of its letters by this rule:
- any appearance of letters is 1
- any appearance of number [0-9] is 2
- special characters is ignored
- if the input is "Marco", yhe autput is "Polo"
- the order is the same as the input
"""


def FrequencyScrabbleEasy(strParam):
    if strParam == "Marco":
        return "Polo"
    strP = ""
    fr = [0] * 62
    for i in range(len(strParam)):
        if strParam[i] <= 'Z' and strParam[i] >= 'A':
            fr[ord(strParam[i]) - ord('A')] += 1
        elif strParam[i] <= 'z' and strParam[i] >= 'a':
            fr[ord(strParam[i]) - ord('a') + 26] += 1
        elif strParam[i] <= '9' and strParam[i] >= '0':
            fr[int(strParam[i]) + 52] += 2

        for j in range(len(strParam), 0, -1):
            for i in range(len(strParam)):
                if strParam[i] <= 'Z' and strParam[i] >= 'A':
                    if fr[ord(strParam[i]) - ord('A')] == j:
                        strP = strP + strParam[i]
                        fr[ord(strParam[i]) - ord('A')] = 0
                elif strParam[i] <= 'z' and strParam[i] >= 'a' and fr[ord(strParam[i]) - ord('a') + 26] == j:
                    strP = strP + strParam[i]
                    fr[ord(strParam[i]) - ord('a') + 26] = 0
                elif strParam[i] <= '9' and strParam[i] >= '0':
                    if fr[int(strParam[i]) + 52] == j:
                        strP = strP + strParam[i]
                        fr[int(strParam[i]) + 52] = 0
    return strP


print(FrequencyScrabbleEasy("this is a basic example"))
