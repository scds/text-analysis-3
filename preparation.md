---
layout: default
title: Preparation
nav_order: 2
---


# Workshop Preparation 

Preparation for this tutorial consists of two steps: [Getting the data](#get-the-data) and [Getting the software](#get-the-software). Please follow the steps below before beginning the lesson.

<hr />
  
## Get the data

The corpus we will be working with in the lesson is Frederick Douglass' "[My Bondage and My Freedom](https://www.gutenberg.org/files/202/202-h/202-h.htm)," available via Project Gutenberg: 
* save the web page as a text file (.txt file extension) and, 
* remove the preamble, table of contents, postscript and other text that we will be omitting from our topic model.

With topic modelling, we would normally be working with a larger corpus - tens, hundres or even thousands of documents - but we will use a single document (with two parts) for the sake of speed and simplicity. Training machine learning systems with small datasets, of course, yields a coarser and brittler model that may not produce useful results outside of the context of its training (i.e. not generalizable to other datasets). Ideally, you will use the skills and techniques you learn in the workshop on an actual corpus you would be using in your research.

<hr />

## Get the software

This hands-on workshop uses several tools to perform topic modelling: Voyant Tools, MALLET and Python. You do not have to use all of them, but the intent is for you to get a sense of each with a small sample from your own corpus so that you can choose an approach that works best for you.

[Download Voyant Server](https://voyant-tools.org/docs/#!/guide/server)

[Download MALLET](https://mimno.github.io/Mallet/)

[Download Anaconda](https://www.anaconda.com/products/individual)* (includes Spyder, integrated development environment - or IDE - for Python).

* If you completed the *[Identifying Proper Nouns with Named Entity Recognition](https://scds.github.io/text-analysis-2/)* workshop, you will already have downloaded Anaconda.

**If you have programming experience with Python,** you are welcome to use the IDE you are familiar with as an alternative.

Please contact the [Sherman Centre](mailto:scds@mcmaster.ca) if you have any difficulties downloading or opening the software.

<hr />

### Software versions

For the lesson as it is currently written, the software versions are as follows:

**Python:** 3.9

**Anaconda Navigator:** 2.3.2

**Spyder:** 5.1.5

<hr />

## Assemble your own corpus (optional)

In advance of the lesson, we also recommend that you assemble a collection of documents to work with for the *Try it with your data* sections. We will use the texts provided above to practice the techniques demonstrated in the lesson but each dataset brings its own unique features. Even if you are not going through the lesson with a specific project in mind, having a different corpus to experiment with will help to reinforce the concepts and enrich your knowledge of the topic.

If you have not already gone through your corpus to get a sense of what errors it might contain, now is a good time! If key words are misspelled, they may not be emerge as relevant themes through topic modelling.

<br />
Next --> Lesson: [Topic Modelling](instructions.html)
