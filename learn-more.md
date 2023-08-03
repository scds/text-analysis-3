---
layout: default
title: Learn More
nav_order: 5
---

# Learn more
If you would like to take your learning further, we have provided some additional resources below:

## Diving Deeper into Topic Modeling

In the lesson, we briefly discussed how topic modeling works without getting into the mathematical basis for the practice. Latent Dirchlet allocation (LDA) [David M. Blei, Andrew Y. Ng and Michael I. Jordan] (https://www.jmlr.org/papers/volume3/blei03a/blei03a.pdf).   including [an interesting article](https://mimno.infosci.cornell.edu/papers/schofield_eacl_2017.pdf) that suggests removing stopwords *after* training is as effective as removing them before, by Alexandra Schofield, M˚ans Magnusson and David Mimno (yes, the David Mimno who is the primary maintainer of MALLET). 

## Building on your Topic Modeling Skills in Python

If you already familiar or have enjoyed working with Python, William J.B. Mattingly -- a historian and digital humanist -- has created [a playlist of video tutorials](https://www.youtube.com/watch?v=N0crN8YnF8Y&list=PL2VXyKi-KpYttggRATQVmgFcQst3z6OlX) that go into greater depth about topic modeling, including another package ([Top2Vec](https://top2vec.readthedocs.io/en/latest/Top2Vec.html)) that Mattingly insists is the best way to do topic modeling in Python. The script in the "Topic Modeling with Python" part of the lesson owes a debt to [Mattingly's experiments with Gensim](https://github.com/wjbmattingly/topic_modeling_textbook/blob/main/03_03_lda_model_demo.ipynb) - which may have been abandoned to pursue Top2Vec!

If you wish to continue using Gensim for topic modeling, however, you may wish to [explore the Gensim documentation](https://radimrehurek.com/gensim/models/ldamodel.html) further.

 ## Alternatives to Visualizing Topic Modeling Values
Visualization is one modality for exploratory data analysis, but it privileges the visual sense and may not be accessible for all audiences. Shawn Graham has created a [Programming Historian lesson on sonification](https://programminghistorian.org/en/lessons/sonification), or the mapping of dataset features to sound. Graham demonstrates several tools for sonifying data in the lesson, and [the part of the lesson that explores Sonic Pi](https://programminghistorian.org/en/lessons/sonification#sonic-pi) uses the probalistic weights of topics from a topic model - data that you will have available to try out from your experiments with Voyant, MALLET and Gensim.

<!--

## More info and other tools

- Tableau [free training videos](https://www.tableau.com/learn/training/20201)
- LinkedIn Learning [Tableau training page](https://www.linkedin.com/learning/topics/tableau)
- Data visualization design considerations for beginners: [Berkeley Library](https://guides.lib.berkeley.edu/data-visualization/design) | [University of Guelph Library](https://guides.lib.uoguelph.ca/c.php?g=700755&p=4976239)

-->
