---
layout: default
title: Preparation
nav_order: 2
---


# Workshop Preparation 

Preparation for this tutorial consists of two steps: [Getting the data](#get-the-data) and [Getting the software](#get-the-software). Please follow the steps below before beginning the lesson.

<hr />
  
## Get the data

The corpus we will be working with in the lesson is comprised of the platforms of the major political parties in Canada that were presented in advance of the 2021 federal election. They can be downloaded from the web as PDF documents; the first tool we will be using, Voyant, can read PDF files and convert them to plain text. If the documents are no longer available online, we have made preservation copies of them for later access and use. 


With topic modeling, we would normally be working with a larger corpus - tens, hundres or even thousands of documents - but we will use a small selection of documents. . Training machine learning systems with small datasets, of course, yields a coarser and brittler model that may not produce useful results outside of the context of its training (i.e. not generalizable to other datasets). Ideally, you will use the skills and techniques you learn in the workshop on an actual corpus you would be using in your research.

<hr />

## Get the software

This hands-on workshop uses several tools to perform topic modelling: Voyant Tools, MALLET and Python. You do not have to use all of them, but the intent is for you to get a sense of each with a small sample from your own corpus so that you can choose an approach that works best for you. You can skip this step for now, read ahead in the lesson and come back to the "Preparation" page to download applications as necessary.

[Download Voyant Server](https://voyant-tools.org/docs/#!/guide/server)

[Download MALLET](https://mimno.github.io/Mallet/)

[Download Anaconda](https://www.anaconda.com/products/individual)* (includes Spyder, integrated development environment - or IDE - for Python).

* If you completed the *[Identifying Proper Nouns with Named Entity Recognition](https://scds.github.io/text-analysis-2/)* workshop, you will already have downloaded Anaconda; you may wish to [update Anaconda](https://docs.anaconda.com/anaconda/install/update-version/) or [uninstall and reinstall it](https://docs.anaconda.com/anaconda/install/uninstall/) if you prefer or if you are getting an error message regarding setup-tools.

**If you are not able to download and/or install Anaconda,** you can alternatively follow the lesson via the [Jupyter notebook version of the workshop in Google Colab](https://colab.research.google.com/drive/1biLTOz5Va-824g7o94Le9QIRM0jxx2ty?usp=sharing). You will need to upload the Douglass text file to the file area in Google Colab as described in [Jay Brodeur's "Basic Text Prep with Python" Colab notebook](https://colab.research.google.com/drive/1ynkHM3WOQUGj9mj8R060p3BYqI6ThbAj?usp=sharing), step 3. Run the code cell by cell using the "play" button at the left of each cell. 

**If you have programming experience with Python,** you are welcome to use the IDE you are familiar with as an alternative.

Please contact the [Sherman Centre](mailto:scds@mcmaster.ca) if you have any difficulties downloading or opening the software.

<hr />

### Software versions

For the lesson as it is currently written, the software versions are as follows:

**Python:** 3.9

**Anaconda Navigator:** 2.3.2

**Spyder:** 5.4.2

**Voyant Server:** 2.6.3

**MALLET:** 202108

If the versions differ from your own, that's ok! There's no need to track down older versions of the software to complete the lesson. The steps should remain the same, but there might be some small variations that can be attributed to using a later version (with the exception of your Python version, which \*might\* break the code; Python 3.9 will be supported until October 2025).

<hr />

## Assemble your own corpus (optional)

In advance of the lesson, we also recommend that you assemble a collection of documents to work with for the *Try it with your data* sections. We will use the texts provided above to practice the techniques demonstrated in the lesson but each dataset brings its own unique features. Even if you are not going through the lesson with a specific project in mind, having a different corpus to experiment with will help to reinforce the concepts and enrich your knowledge of the topic.

If you have not already gone through your corpus to get a sense of what errors it might contain, now is a good time! If key words are misspelled, they may not be emerge as relevant themes through topic modelling.

<br />
Next --> [Start the Topic Modeling Lesson](instructions.html)
