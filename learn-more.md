---
layout: default
title: Learn More
nav_order: 5
---

# Learn More
If you would like to take your learning further, we have provided some additional resources below:
## Diving Deeper into Topic Modeling

In the lesson, we briefly discussed how topic modeling works without getting into the mathematical basis for the practice. David Blei gives [an overview of topic modeling](https://journalofdigitalhumanities.org/2-1/topic-modeling-and-digital-humanities-by-david-m-blei/), with a plain language description of latent Dirchlet allocation (LDA), in the Winter 2012 issue of the Journal of Digital Humanities. The entire issue of the journal is dedicated to topic modeling and may also be of interest!

If you wish to read more about the specifics of LDA, the [seminal article](https://www.jmlr.org/papers/volume3/blei03a/blei03a.pdf) by David M. Blei, Andrew Y. Ng and Michael I. Jordan is a good place to start. Or, if you prefer to head off on a tangent that might enrich your understanding, Alexandra Schofield, Måns Magnusson and David Mimno (yes, the David Mimno who is the primary maintainer of MALLET) have written [a provocative paper](https://mimno.infosci.cornell.edu/papers/schofield_eacl_2017.pdf) that suggests removing stopwords *after* training is as effective as removing them before in topic modeling. 

## Building on your Topic Modeling Skills in Python

If you already familiar or have enjoyed working with Python, William J.B. Mattingly -- a historian and digital humanist -- has developed [a playlist of video tutorials](https://www.youtube.com/watch?v=N0crN8YnF8Y&list=PL2VXyKi-KpYttggRATQVmgFcQst3z6OlX) that go into greater depth about topic modeling, including another package ([Top2Vec](https://top2vec.readthedocs.io/en/latest/Top2Vec.html)) that Mattingly insists is the best way to do topic modeling in Python. The script in the "Topic Modeling with Python" part of the lesson owes a debt to [Mattingly's experiments with Gensim](https://github.com/wjbmattingly/topic_modeling_textbook/blob/main/03_03_lda_model_demo.ipynb) - which may have been abandoned to pursue Top2Vec!

If you wish to continue using Gensim for topic modeling, however, you may wish to [explore the Gensim documentation](https://radimrehurek.com/gensim/models/ldamodel.html) further.

## Topic Modeling in R

We used the Python programming language for topic modeling but if you are more familiar or comfortable with the R programming language, which is popular in academic and data science contexts, there are an abundance of resources to guide you:

* Julia Silge's video on [Topic modeling with R and tidy data principles](https://www.youtube.com/watch?v=evTuL-RcRpc) (uses the [tidytext](https://juliasilge.github.io/tidytext/reference/index.html) -- developed by Silge -- and [stm](https://cran.r-project.org/web/packages/stm/index.html) packages)
* [a series of R tutorials](https://github.com/ccs-amsterdam/r-course-material/tree/master) from a team at Vrije Universiteit Amsterdam, including [Fitting LDA models in R](https://github.com/ccs-amsterdam/r-course-material/blob/master/tutorials/r_text_lda.md) with [an accompanying video](https://www.youtube.com/watch?v=4YyoMGv1nkc) (uses the [quanteda](https://quanteda.io/) and [topicmodels](https://www.rdocumentation.org/packages/topicmodels/versions/0.2-8) packages)
* if you prefer a notebook approach, Martin Schweinberger of the University of Queensland [has developed one](https://ladal.edu.au/topicmodels.html)
* Thomas W. Jones' [textmineR library](https://cran.r-project.org/web/packages/textmineR/vignettes/c_topic_modeling.html), which allows for the use of different modeling techniques including and beyond LDA.

There is much more out there if R is your language of choice!

## Alternatives to Visualizing Topic Modeling Values
Visualization is one modality for exploratory data analysis, but it privileges the visual sense and may not be accessible for all audiences. Shawn Graham has created a [Programming Historian lesson on sonification](https://programminghistorian.org/en/lessons/sonification), or the mapping of dataset features to sound. Graham demonstrates several tools for sonifying data in the lesson, and [the part of the lesson that explores Sonic Pi](https://programminghistorian.org/en/lessons/sonification#sonic-pi) uses the probalistic weights of topics from a topic model - data that you will have available to try out from your experiments with Voyant, MALLET and Gensim.
