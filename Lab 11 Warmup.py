"""
This script is a warmup exercise to get familiar 
with language processing in Python.
"""

#%% imports

# %% example

text = "This is my text. It includes commas, question marks? and other stuff. Acronyms, like U.S. or Dr. aren't easy to handle."

# str.split() splits on a character
words = text.split(' ')
text.capitalize()
text.upper()

# case sensitive
"This" == "this" # False
"THIS".lower() == 'this' # True

# %% easy with NLTK
from nltk import word_tokenize

# break a string into tokens
tokens = word_tokenize(text)
print(tokens)
# %% fix the lookup error

import nltk
nltk.download('punkt')

# %% 
word_list = []
import string
for token in tokens:
    print("the token is:", token)
    if token not in string.punctuation:
        print("Found a token that is not punctuation:", token)
        word_list.append(token)

# %%
print(string.punctuation)
# %%
from nltk.sentiment.vader import SentimentIntensityAnalyzer
nltk_sentiment = SentimentIntensityAnalyzer()
"""
import nltk
nltk.download('vader_lexicon')
"""

# %%
nltk_sentiment.polarity_scores('This is TERRIBLE. :)')
# %%
