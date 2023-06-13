# -*- coding: utf-8 -*-
"""
A script that:
* reads text files in a directory and writes their contents to a list
* preprocesses the text: tokenizes, lemmatizes, removes stopwords, etc.
* creates a topic model using LDA (via gensim)
* visualizes the topics

@author: D Mordell, largely modeled after William Mattingly's Jupyter notebook - https://github.com/wjbmattingly/topic_modeling_textbook/blob/main/03_03_lda_model_demo.ipnyb

Preparation (run commands in Spyder console):
pip install gensim
pip install spacy
pip install https://github.com/explosion/spacy-models/releases/download/en_core_web_sm-3.5.0/en_core_web_sm-3.5.0-py3-none-any.whl (a more recent version may exist)
pip install pyLDAvis

Note: there are a number of lines that are commented out for a variety of reasons, primarily the option to print out the contents of 
certain variables that can instead be verified in Spyder's Variable Explorer pane.

"""

# Import internal libraries: glob for grabbing docs from directory
import glob

# Import external libraries: gensim for preprocessing and LDA
import gensim
import gensim.corpora as corpora
from gensim.utils import simple_preprocess
from gensim.models import CoherenceModel

# Import external libraries: spaCy for lemmatization and stopwords
from spacy.lang.en import English                 # For other languages, refer to the SpaCy website: https://spacy.io/usage/models
from spacy.lang.en.stop_words import STOP_WORDS   # Also need to update stopwords for other languages (e.g. spacy.lang.uk.stop_words for Ukrainian)

# Import external libraries: pyLDA for vis
import pyLDAvis
import pyLDAvis.gensim_models as gensimvis

# Read files from directory and create list from contents
# Varies between Mac and Windows OS; uncomment the line as appropriate 
# file_list = glob.glob('./corpus' + '/*.txt') # directory containing text (.txt) files # uncomment for Mac OS or Linux
# file_list = glob.glob(r'[path to folder]\*.txt') # uncomment for Windows OS and replace "[path to folder]" with the path to the "corpus" folder
                                                   # e.g. C:\Users\username\corpus

texts = []

for filename in file_list:
    with open(filename, mode = 'r', encoding = 'utf-8') as f: # specify encoding as appropriate
        texts.append(f.read())

# --Uncomment line below to rint the first .txt file in the list to confirm files were read        
# print(texts[0])

# Print the initial set of stopwords from SpaCy
# Also available at: https://github.com/explosion/spaCy/blob/master/spacy/lang/en/stop_words.py
print(STOP_WORDS)

# --Uncomment lines below to remove or add (first line) or remove (second line) from the stopword list
# STOP_WORDS.add("[word]")          # Replace [word] with your word to add to the list; only takes one argument at a time.
# STOP_WORDS.remove("[word]")       # Replace [word] with your word to remove from the list; only takes one argument at a time.

# --Uncomment line to print the stopword list again to confirm that your word has been added or removed
# print(STOP_WORDS)

# Lemmatize tokens
def lemmatization(texts, allowed_postags=["NOUN", "ADJ", "VERB", "ADV"]):
    nlp = spacy.load("en_core_web_sm", disable=["parser", "ner"])
    texts_out = []
    for text in texts:
        doc = nlp(text)
        new_text = []
        for token in doc:
            if token.pos_ in allowed_postags:
                new_text.append(token.lemma_)
        final = " ".join(new_text)
        texts_out.append(final)
    return (texts_out)


lemmatized_texts = lemmatization(texts)

# --Uncomment line below to print the contents of the lemmatized_texts variable
# print(lemmatized_texts[0][0:90])


# Preprocess texts
def gen_words(texts):
    final = []
    for text in texts:
        new = gensim.utils.simple_preprocess(text, deacc = True)
        final.append(new)
    return (final)

data_words = gen_words(lemmatized_texts)

# --Uncomment line below to print contents of the data_words variable
# print(data_words[0][0:20])

bigram_phrases = gensim.models.Phrases(data_words, min_count=3, threshold=50)
trigram_phrases = gensim.models.Phrases(bigram_phrases[data_words], threshold=50)

bigram = gensim.models.phrases.Phraser(bigram_phrases)
trigram = gensim.models.phrases.Phraser(trigram_phrases)

def make_bigrams(texts):
    return [bigram[doc] for doc in texts]

def make_trigrams(texts):
    return [trigram[bigram[doc]] for doc in texts]

data_bigrams = make_bigrams(data_words)
data_bigrams_trigrams = make_trigrams(data_bigrams)

# --Uncomment to print list of words showing bigrams and trigrams
# print (data_bigrams_trigrams[0])

# Create dictionary of all words in texts
id2word = corpora.Dictionary(data_bigrams_trigrams)

# Represent dictionary words as tuples (index, frequency)
corpus = []
for text in data_bigrams_trigrams:
    new = id2word.doc2bow(text)
    corpus.append(new)

# --Uncomment line below to print a list of (index, frequency) pairs 
# print(corpus[0][0:20])

# --Uncomment two lines below to retrieve individual words from dictionary if wishing to explore term frequency
# word = id2word[[0][:1][0]]
# print(word)

# Specify number of topics (clusters of words)

num_topics = 10     # Change numeric value for more or fewer topics.

# Create LDA model
lda_model = gensim.models.ldamodel.LdaModel(corpus=corpus,
                                            id2word=id2word,
                                            num_topics=num_topics,
                                            per_word_topics = True;
                                            random_state=100,       # randomState object or a seed to generate one
                                            update_every=1,         # Number of documents to be iterated through for each update - 0 (batch) or 1 (iterative)
                                            chunksize=100,          # Number of documents to be used in each training chunk
                                            passes=10,              # Number of passes through the corpus during training
                                            alpha="auto")


# Output visualization to HTML file and open in browser to view
vis_data = gensimvis.prepare(lda_model, corpus, id2word, R=15)  # R variable holds the number of topics to print in bar charts
vis_data
pyLDAvis.display(vis_data)
pyLDAvis.save_html(vis_data, './topicVis' + str(num_topics) + '.html')
