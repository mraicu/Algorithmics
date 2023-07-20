#Să se determine ultimul (din punct de vedere alfabetic) cuvânt care poate apărea într-un text care conține mai multe cuvinte separate prin ” ” (spațiu).
# De ex. ultimul (dpdv alfabetic) cuvânt din ”Ana are mere rosii si galbene” este cuvântul "si".

def lastWord(sentence):
    last=""
    splitSentence=sentence.split(" ")
    for i in  range(len(splitSentence)-1):
        if splitSentence[i][0]<splitSentence[i+1][0]:
            last=splitSentence[i+1]
        if splitSentence[i][0]==splitSentence[i+1][0]:
            j=1
            while splitSentence[i][j]==splitSentence[i+1][j] and j < len(min(splitSentence[i], splitSentence[i+1]))-1:
                j+=1
            if j < len(splitSentence[i])-1:
                if splitSentence[i][j] < splitSentence[i + 1][j]:
                    last = splitSentence[i + 1]
                else:
                    last = splitSentence[i]
            if len(splitSentence[i])<len(splitSentence[i+1]):
                last=splitSentence[i+1]
            else:
                last = splitSentence[i]
    return last

def test():
    assert(lastWord("Ana are mere rosii si galbene")=="si")
    assert(lastWord("Ana are mere rosii si singure")=="singure")
    assert(lastWord("Ana are mere rosii")=="rosii")
test()