"""
INPUT: list of strings -strArr-
OUTPUT: the number of positive reviews
A positive review is a string that contain more positive words then negative (positive and negative words are given).
"""
def RulebasedSentimentAnalysis(strArr):
    POSITIVE_WORDS = ["good", "great", "excellent", "amazing", "awesome", "superb", "outstanding", "best"]
    NEGATIVE_WORDS = ["bad", "terrible", "awful", "horrible", "worst", "disappointing", "poor", "lousy"]
    total = 0
    for i in range(len(strArr)):
        p_no = 0
        n_no = 0
        for j in range(len(POSITIVE_WORDS)):
            if POSITIVE_WORDS[j] in strArr[i]:
                p_no += 1
            if NEGATIVE_WORDS[j] in strArr[i]:
                n_no += 1
        if n_no < p_no:
            total += 1
    return total


print(RulebasedSentimentAnalysis(
    ["This movie was amazing and I loved the acting", "The plot was terrible and the characters were poorly developed",
     "I think it is the best movie of the year", "The film was disappointing and not worth watching"]))
