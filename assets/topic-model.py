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
file_list = glob.glob('./dir' + '/*.txt') # directory containing text (.txt) files

texts = []

for filename in file_list:
    with open(filename, mode = 'r', encoding = 'mac-roman') as f: # specify encoding as appropriate
        texts.append(f.read())

# Print the first .txt file in the list to confirm files were read        
# print(texts[0])

# Print the initial set of stopwords from SpaCy
# Also available at: https://github.com/explosion/spaCy/blob/master/spacy/lang/en/stop_words.py
print(STOP_WORDS)

# Add a word to remove or add from the list
# STOP_WORDS.add("[word]") 
# STOP_WORDS.remove("[word]")

# Print again to confirm that your word has been added or removed
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
# print(lemmatized_texts[0][0:90])


# Preprocess texts
def gen_words(texts):
    final = []
    for text in texts:
        new = gensim.utils.simple_preprocess(text, deacc = True)
        final.append(new)
    return (final)

data_words = gen_words(lemmatized_texts)

# print(data_words[0][0:20])


"""

# Account for bigrams and trigrams - Prabhakaran via Mattingly, https://www.machinelearningplus.com/nlp/topic-modeling-gensim-python/#9createbigramandtrigrammodels
bigram_phrases = gensim.models.Phrases(data_words, min_count=3, threshold=50)
trigram_phrases = gensim.models.Phrases(bigram_phrases[data_words], threshold=50)

bigram = gensim.models.phrases.Phraser(bigram_phrases)
trigram = gensim.models.phrases.Phraser(trigram_phrases)

def make_bigrams(texts):
    return (bigram[doc] for doc in texts)

def make_trigrams(texts):
    return (trigram[bigram[doc]] for doc in texts)

data_bigrams = make_bigrams(data_words)
data_bigrams_trigrams = make_trigrams(data_bigrams)

print (data_bigrams_trigrams[0])
"""

# Create dictionary of all words in texts
id2word = corpora.Dictionary(data_words)

# Represent dictionary words as tuples (index, frequency)
corpus = []
for text in data_words:
    new = id2word.doc2bow(text)
    corpus.append(new)

# print(corpus[0][0:20])

# Retrieve individual words from dictionary
# word = id2word[[0][:1][0]]
# print(word)

# Specify number of topics (clusters of words)

num_topics = 10

# Create LDA model
lda_model = gensim.models.ldamodel.LdaModel(corpus=corpus,
                                           id2word=id2word,
                                           num_topics=num_topics,
                                           random_state=100,
                                           update_every=1,
                                           chunksize=100,
                                           passes=10,
                                           alpha="auto")


# Output visualization
vis_data = gensimvis.prepare(lda_model, corpus, id2word, R=15)
vis_data
pyLDAvis.display(vis_data)
pyLDAvis.save_html(vis_data, './topicVis' + str(num_topics) + '.html')
