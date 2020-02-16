import os
from textblob import TextBlob
from textblob.en import Spelling
import os
path = "spelling-model-weighted.txt"
assert os.path.isfile(path)
spelling = Spelling(path=path)

MOCKDATA = "hi i dont spel"
test = TextBlob(MOCKDATA)
print(test.sentences)
for word in test.sentences[0].words:
    print(word)

