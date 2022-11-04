"""
This script will demonstrate how to work with strings and text
in Python. We will perform tokenization, text cleaning, and 
using NLTK.
"""

#%% 

text = "This is my text. It includes commas, question marks? and other stuff. Acronyms, like U.S. or Dr. aren't easy to handle."

# %% split string

words = text.split(' ')

words[3]

# %% capitalization matters
'this' == 'This'            # false
'this' == 'This'.lower()    # true
'this'.upper() == 'This'.upper() # True

#%% download NLTK extras for tokenization

# we need to download the punkt tokenization data
import nltk
nltk.download('punkt')


# %% use NLTK
from nltk import word_tokenize

tokens = word_tokenize(text)

print(tokens)
# %% remove punctuation from the list

import string
words = []
for token in tokens:
    print('The current element is', token)
    if token not in string.punctuation:
        print(token)
        words.append(token)



# %% string.punctuation
print(string.punctuation)


# %% count the number of words
len(words)


# %% sentiment examples
# download the vader lexicon
import nltk
nltk.download('vader_lexicon')

# %% run sentiment examples
from nltk.sentiment.vader import SentimentIntensityAnalyzer
nltk_sentiment = SentimentIntensityAnalyzer()

nltk_sentiment.polarity_scores("This algorithm is AWESOME :) !!!")

# %%
