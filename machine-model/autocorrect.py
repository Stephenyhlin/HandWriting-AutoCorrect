from textblob import TextBlob, Word


def auto_correct( data ):
    # We will first turn the data into a TextBlob
    blob_data = TextBlob( data )
    # Create a changed flag
    changed = False

    # Go through each word in the data set

    for word in blob_data.words:
        # Convert everything into a word that can be spell checked
        temp_word = Word( word )
        temp_tuples = temp_word.spellcheck()
        # go through the first tuple. The first tuple is the most confident autocorrect word
        # tuples[0] is the word, tuples[1] is the confidence
        for tuples in temp_tuples:
            if ( not (tuples[1] == 1.0 or (tuples[0] == temp_word) ) ):
                # We add to a list
                print( "Changed word " + word + " to " + tuples[0] + " since we have a confidence level of " + str(tuples[1]))
                if(not changed):
                    changed = True
                break
    
    if(changed) :
        print("Did you mean: \"" + str(blob_data.correct()) + "\"?")
    return blob_data.correct()
                


# MOCKDATA = "Hi, I cant spel at al, snd hlp."
# auto_correct(MOCKDATA)
