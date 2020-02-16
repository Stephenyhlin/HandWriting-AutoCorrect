from textblob import TextBlob, Word
from textblob.en import Spelling

MOCKDATA = "Hi, I cant spel at al, snd hlp."

test = TextBlob(MOCKDATA)

# spelling = Spelling(path=path)
# spelling.train()


for data in test.words:
    temp = Word(data)
    tempTuples = temp.spellcheck()
    print(temp)
    print(temp.spellcheck())
    print(temp.correct())
    for tuples in tempTuples:
        print(tuples[0])
        print(tuples[1])


        # print(tuples.confidence)