---
layout: default
title: What is Topic Modeling?
parent: Lesson
nav_order: 1
---

# What is Topic Modeling?

In a digital scholarship context, topic modeling is typically used to get a sense of what a document, set of documents (corpus) or subset of documents is about in a broad sense. “Documents” here could be articles, archives, web pages, tweets, transcripts of interviews and so on. 

You may have used term frequencies - that is, counts of how many times a specific word or words appear in a corpus - for the same purpose. For example, in a political party's platform, the frequent mention of words like "climate," "green" and "environment" may allow you to hypothesize that climate action is one of their priorities. However, while we humans can infer the semantic relatedness of words like "climate," "green" and "environment," a computer cannot make the same connections between words unless explicitly programmed. Writing rules to capture every group of meaningful  would be . 

Term frequencies can be less helpful without context. If "board" is one of the most commonly occurring words in the text, how is it intended: a Board of Directors? To board a vessel? A board of wood? And so on. Knowing that the word "board" often appears near "directors," "ship" or "hammer" would help  

Topic modeling adds nuance by grouping terms (words) that appear in the text together to a greater degree than others; in a way, topic modeling creates a context in which to understand the term(s). Or, put another way:

“A topic can be thought of as the cluster of words that tend to come up in a discussion and therefore to co-occur more frequently than they otherwise would, whenever the topic is being discussed.” (Ignatow & Mihalcea, 2)

Topic modeling can be an elusive concept to grasp relative to other text analysis techniques like named entity recognition or part-of-speech (POS) tagging. If it is still a bit hazy, you may find it helpful to actually go through the process. Visit David Mimno's [jsLDA](https://mimno.infosci.cornell.edu/jsLDA/) web application to try it out yourself!

On

It may be clear from describing how topic modeling is undertaken that it would be difficult if not impossible to perform on texts at scale without computational means. At the same time, there are evident trade-offs in automating tasks through the use of general rules: words in a related topic may be split between segments and so, appear less related.


<br />

Next --> [Topic Modeling with Voyant Tools](tmv.html)
