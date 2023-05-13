---
layout: default
title: What is Topic Modeling?
parent: Lesson
nav_order: 1
---

# What is Topic Modeling?

In a digital scholarship context, topic modeling is typically used to get a sense of what a document, set of documents (corpus) or subset of documents is about in a broad sense. “Documents” here could be articles, archives, web pages, tweets, transcripts of interviews and so on. 

You may have used term frequencies - that is, counts of how many times a specific word or words appear in a corpus - for the same purpose. For example, in a political party's platform, the frequent mention of words like "climate," "green" and "environment" may allow you to hypothesize that climate action is one of their priorities. However, while we humans can infer the semantic relatedness of words like "climate," "green" and "environment," a computer cannot make the same connections between words unless explicitly programmed. Writing rules to capture every group of words in a potential topic would be impossibly onerous, to say the least! 

Term frequency counts are also less helpful without context. Even if "board" is one of the most commonly occurring words in the text, you might ask how it is intended: a Board of Directors? To board a vessel? A board of wood? And so on. Knowing that "board" often appears near the words "directors," "ship" or "hammer" would clarify the meaning for us. 

Topic modeling adds nuance by grouping terms (words) that appear in the text together to a greater degree than others; essentially, topic modeling creates a context in which to understand the term(s). Or, put another way:

> “A topic can be thought of as the cluster of words that tend to come up in a discussion and therefore to co-occur more frequently than they otherwise would, whenever the topic is being discussed.” (Ignatow & Mihalcea, 2)

## Topic modeling in practice

Topic modeling can be an elusive concept to grasp relative to other text analysis techniques like named entity recognition or part-of-speech (POS) tagging. A demonstration might help to clarify: visit David Mimno's [jsLDA](https://mimno.infosci.cornell.edu/jsLDA/jslda.html) web application to try it out yourself!

There will be a demo corpus already loaded that you can experiment with if you like. Try changing the number of topics -- as too many topics can lead to overlap, and too few can make the clusters overly general -- then running a few iterations, which refines the model.

![Screenshot of Mimno's jsLDA interface with topics as described in the next paragraph](assets/img/mimno-eg.png)

Your topics may differ! But you may note a coherence within clusters of words, or topics, such as:
* economic trade foreign production business policy agriculture farm economy international
* budget billion dollars million fiscal federal tax expenditures government increase
* health security care energy social program system development insurance education
* federal government states local state public legislation program administration rights
* nations united states military peace forces security soviet war defense

You can also upload the document we are working with for the lesson, the douglass.txt file. Initially, the topics returned will be filled with common words like "may," "the" and "for," and so, will not tell us much about the text or corpus. In order to remove these words from the analysis, you will need to upload a text file with stopwords to omit. Read more about stopwords in the [*Identifying Proper Nouns with Named Entity Recognition*](https://scds.github.io/text-analysis-2/ner.html#stop-word-removal) workshop.

If you wish to supply your own list of stopwords to the jsLDA web application, you can copy and paste the [list of words used by the Natural Language Toolkit (NLTK) Python library](https://gist.github.com/sebleier/554280) in a text file (i.e. .txt file extension). If you observe words in topics that you would like to ignore after uploading the list, you can add those words to your list and re-upload the stopwords file.

It may be clear from our results with Mimno's tool that it would be difficult if not impossible to model topics on texts at scale without computational means. At the same time, there are evident trade-offs in automating tasks through the use of general rules.

## How topic modeling works

There have been numerous explanatory articles written on topic modeling in the Digital Humanities, including Graham, Weingart and Milligan's "[Getting Started with Topic Modeling and MALLET](https://programminghistorian.org/en/lessons/topic-modeling-and-mallet)" and Ted Underwood's "[Topic Modeling Made Just Simple Enough](https://tedunderwood.com/2012/04/07/topic-modeling-made-just-simple-enough/)" (from which the further simplified explanation provided below borrows). You may wish to read them if you are new to the idea of topic modeling and would like to know more about how it works, as we will only briefly discuss it here in relation to the tasks we will be performing in the lesson. 

Topic modeling is approached by splitting a text into segments of equal length, and counting the occurrence of terms within the segment. Each segment is presumed to contain approximately one topic (though the topic is not usually unique within the corpus); that is, when we write, we typically talk about one main topic or theme for a paragraph or so. It is possible in most tools to adjust the length of the segments, and you can experiment with values according to the format of your text data: for example, segments of 100 for articles or segments of 50 for micro-blog posts. Of course, because we are not manually segmenting the text each time the author changes the subject, there are trade-offs for the coherence of our topics. 

Topics "can be understood as a collection of words that have different probabilities of appearance in passages discussing the topic" (Underwood). In topic modeling, the terms comprising a topic are not usually known in advance so terms are initially assigned randomly . Many topic modeling approaches rely on the Latent Dirichlet Allocation algorithm, though it is not the only algorithm used to perform topic modeling (see also. When we create our Python script to  . 

The overall premise of topic modeling is perhaps best captured by Graham, Weingart and Milligan: 

> \[Topic modeling programs] assume that any piece of text is composed (by an author) by selecting words from possible baskets of words where
> each basket corresponds to a topic. If that is true, then it becomes possible to mathematically decompose a text into the probable baskets
> from whence the words first came. The tool goes through this process over and over again until it settles on the most likely distribution
> of words into baskets, which we call topics.


<!--https://nlp.stanford.edu/courses/cs224n/2007/fp/adarve-kwong-speriosu.pdf-->








<br />

Next --> [Topic Modeling with Voyant Tools](tmv.html)
