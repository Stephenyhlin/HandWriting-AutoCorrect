from textblob import TextBlob, Word
import json 
import os 
from textblob.en import Spelling


def auto_correct( data ):
    # Initialize path
    path = "spelling-model-weighted.txt"
    assert os.path.isfile(path)
    spelling = Spelling(path=path)
    # We will first turn the data into a TextBlob
    blob_data = TextBlob( data )
    # Create a changed flag
    changed = False
    return_list = []

    # Go through each word in the data set

    for word in blob_data.words:
        # Convert everything into a word that can be spell checked
        temp_word = Word( word )
        # temp_tuples = temp_word.spellcheck()
        # go through the first tuple. The first tuple is the most confident autocorrect word
        # tuples[0] is the word, tuples[1] is the confidence
        # for tuples in temp_tuples:
        #     if ( not (tuples[1] == 1.0 or (tuples[0] == temp_word) ) ):
        #         # We add to a list
        #         print( "Changed word " + word + " to " + tuples[0] + " since we have a confidence level of " + str(tuples[1]))
        #         if(not changed):
        #             changed = True
        #         break
        for tuples in spelling.suggest(word):
            if ( not (tuples[1] == 1.0 or (tuples[0] == temp_word) ) ):
                # We add to a list
                print( "Changed word " + word + " to " + tuples[0] + " since we have a confidence level of " + str(tuples[1]))
                return_list.append(tuples[0])
                if(not changed):
                    changed = True
                break
            return_list.append(tuples[0])
    
    if(changed) :
        # using list comprehension 
        list_to_str = ' '.join([str(elem) for elem in return_list])
        print("Did you mean: \"" + list_to_str + "\"?")
    return list_to_str
                


# MOCKDATA = "hi, I cant spel at al, snd hlp."
# auto_correct(MOCKDATA)

# passed_message = json.dumps({"text" : MOCKDATA})
# parsed_message = json.loads(passed_message)
# print(passed_message)
# print(parsed_message["text"])
# auto_correct(parsed_message["text"])
