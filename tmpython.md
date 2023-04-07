---
layout: default
title: Topic Modeling with Python
parent: Lesson
nav_order: 4
---

# Topic Modeling with Python (Gensim & SpaCy)

Our third approach to topic modeling uses the Python programming language. The lesson that follows uses the open source integrated development environment (IDE) Spyder, which is bundled in with Anaconda data science platform that you were encouraged to download at the beginning of the lesson. If you are new to programming (and perhaps not too keen to learn), you may alternatvely wish to use the [Jupyter notebook instance of the script](https://colab.research.google.com/drive/1biLTOz5Va-824g7o94Le9QIRM0jxx2ty?usp=sharing). Instructions on how to run the script are included in the notebook, and there is a [video recording of how to use the script](https://echo360.ca/media/12af901f-4582-4b13-92c5-6e7915e99dcd/public?startTimeMillis=7706430) from a previous workshop (topic modeling starts around 2:08:15); the videos and screenshots below demonstrate the Spyder IDE workflow.   

You can compare the results that you get from running the script in Jupyter Notebooks on your corpus subset with your results from MALLET and Voyant. If you get the richest and most coherent topics in Python, that is the tool you will want to work with for you full corpus. You may even wish to compare results between Jupyter Notebooks and the Spyder IDE, as outlined below.

<hr />

Jump to step >

1. [Install the required packages](#1-install-the-required-packages)
2. [Import internal and external libraries (i.e. dependencies)](#2-import-internal-and-external-libraries-ie-dependencies)
3. [Read the files containing the text data](#3-read-the-files-containing-the-text-data)
4. [Identify stopwords for the corpus](#4-identify-stopwords-for-the-corpus)
5. [Tokenize and lemmatize text data, and remove stopwords](#5-tokenize-and-lemmatize-text-data-and-remove-stopwords)
6. [Preprocess texts using the Gensim library](#6-preprocess-texts-using-the-gensim-library)
7. [Create a dictionary of words used in the corpus](#7-create-a-dictionary-of-words-used-in-the-corpus)
8. [Retrieve words from corpus dictionary](#8-retrieve-words-from-corpus-dictionary)
9. [Create topics in Gensim](#9-create-topics-in-gensim)
10. [Create topic modeling visualization with LDAvis](#10-create-topic-modeling-visualization-with-ldavis)

<hr />

<hr />

## **1.** Install the required packages
Our Python script is dependent on a few external packages that are not by default installed on Anaconda. We must install them before we can start writing our script, as our next step is to import them!

Type (or copy-paste) each of the commands below in the iPython console, which - in the default view of the Spyder IDE - is in the bottom right corner. After each command, hit enter to run. You should see a message that tells you the status of the installation, and you may be instructed to restart the kernel. You can restart the kernel using the shortcut key `Ctrl` + `.` on Windows, `Cmd` + `.` on a Mac, or by selecting it from the hamburger menu at the top right of the iPython console window.

* Install Gensim<br>
`pip install gensim`

* Install SpaCy<br>
`pip install spacy`

* Install the trained language model from SpaCy (required to be able to use the SpaCy library)<br>
`pip install https://github.com/explosion/spacy-models/releases/download/en_core_web_sm-3.5.0/en_core_web_sm-3.5.0-py3-none-any.whl`

* Install pyLDAvis<br>
`pip install pyLDAvis`

<hr />

## **2.** Import internal and external libraries (i.e. dependencies)
Now, we will start writing our script in the Spyder editor (left pane in the default interface). Our first step is to import the libraries we just installed to let the console know that we require them. We will highlight when we use the various libraries in our code to give you a sense of where they fit in to the picture!

After the initial code comments that Spyder provides for you (and which you can elaborate upon), type or copy / paste the following commands and comments:

    # Import internal libraries: glob for grabbing docs from directory
    import glob

    # Import external libraries: gensim for preprocessing and LDA
    import gensim
    import gensim.corpora as corpora
    from gensim.utils import simple_preprocess
    from gensim.models import CoherenceModel

    # Import external libraries: spaCy for tokenization, lemmatization and stopwords
    import spacy
    from spacy.lang.en import English                 # For other languages, refer to the SpaCy website: https://spacy.io/usage/models
    from spacy.lang.en.stop_words import STOP_WORDS   # Also need to update stopwords for other languages (e.g. spacy.lang.uk.stop_words for Ukrainian)

    # Import external libraries: pyLDA for vis
    import pyLDAvis
    import pyLDAvis.gensim_models as gensimvis

You will note in the code above there is the option of working with texts in languages other than English.

If you have not saved the script yet, go ahead and do so. Make a note of where you are saving the script, because you will as described below.

<hr />

## **3.** Read the files containing the text data
Our next step is to load our text files in a manner that they can be used; i.e. storing them in a list data structure in Python. We will employ the [`glob` library](https://docs.python.org/3/library/glob.html) we imported in the previous step. The `glob` library allows us to grab the contents of a directory using pattern matching.

In order to use the lines of code below, you will need to create a new directory (folder) in the folder that contains the python script you are creating called "corpus" and copy your text files to it. For the lines of code below to run, the files must end with the `.txt` file extension - a commonly used file format in text analysis. Alternatively, you can replace `'/*.txt'` below with `'/*.doc'` or `'/*.docx'` but all your text files must have the same file extension. The script will also work with a single text file in the "corpus" folder. 

    # Read files from directory and create list from contents
    file_list = glob.glob('./corpus' + '/*.txt') # directory containing text (.txt) files

    texts = []

    for filename in file_list:
        with open(filename, mode = 'r', encoding = 'mac-roman') as f: # specify encoding as appropriate
            texts.append(f.read())

    print(texts[0]) # print the first .txt file in the list to confirm

You may need to adjust the encoding value.    

Hit the F5 key to run the script thus far in the console. In the console area, the text from the first document should print. In the variable explorer pane (top right, second tab), new variables named file_list and texts should appear with expected text data values.

<hr />

## **4.** Identify stopwords for the corpus
<hr />

## **5.** Tokenize and lemmatize text data, and remove stopwords
<hr />

## **6.** Preprocess texts using the Gensim library
<hr />

## **7.** Create a dictionary of words used in the corpus
<hr />

## **8.** Retrieve words from corpus dictionary
<hr />

## **9.** Create topics in Gensim
<hr />

## **10.** Create topic modeling visualization with LDAvis
<hr />

<br />
Next --> 
