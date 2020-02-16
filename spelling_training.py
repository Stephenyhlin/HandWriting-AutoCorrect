import os
from textblob import TextBlob
from textblob.en import Spelling
import os
path = "spelling-model-weighted.txt"
assert os.path.isfile(path)
spelling = Spelling(path=path)
MOCKDATA = "hi i dont spel"
test = TextBlob(MOCKDATA)
test1 = test.replace('dont',"don't")
test1 = test1.replace('doesnt',"doesn't")
test1 = test1.replace('didnt',"didn't")
test1 = test1.replace('wont',"won't")
test1 = test1.replace('wouldve',"would've")
test1 = test1.replace('cant',"can't")
test1 = test1.replace('couldnt',"couldn't")
test1 = test1.replace('couldve',"could've")
test1 = test1.replace('shouldnt',"shouldn't")
test1 = test1.replace('shoulve',"shouldn've")
test1 = test1.replace('mightve',"might've")
test1 = test1.replace('havent',"haven't")
test1 = test1.replace('lets',"let's")

print(test1)
for word in test1.words:
    print(spelling.suggest(word))

