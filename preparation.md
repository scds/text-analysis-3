---
layout: default
title: Preparation
nav_order: 2
---


# Workshop Preparation 

Preparation for this tutorial consists of two steps: [Getting the data](#get-the-data) and [Getting the software](#get-the-software). Please follow the steps below before beginning the lesson.

<hr />
  
## Get the data

The corpus - or collection of documents - we will be working with in the lesson is comprised of the platforms of the major political parties in Canada presented in advance of the 2021 federal election. They can be downloaded from the web as PDF documents; the first tool we will be using, Voyant, reads PDF files and converts them to plain text. If the documents are no longer available online, we have made [preservation copies of them](https://github.com/scds/text-analysis-3/blob/main/assets/lesson-corpus.zip) (as plain text files) for future access and use. 

* 2021 platform - [Conservative Party of Canada](https://web.archive.org/web/20210922084914/https://cpcassets.conservative.ca/wp-content/uploads/2021/09/08200659/e4cd8c0115c3ea0.pdf)
* 2021 platform - [Green Party](https://www.greenparty.ca/sites/default/files/gpc_platform_en_v-02.pdf)
* 2021 platform - [Liberal Party](https://liberal.ca/wp-content/uploads/sites/292/2021/09/Platform-Forward-For-Everyone.pdf)
* 2021 platform - [New Democratic Party](https://xfer.ndp.ca/2021/Commitments/Ready%20for%20Better%20-%20NDP%202021%20commitments.pdf)
* 2021 platform - [People's Party of Canada](assets/2021-platform_PPC.txt)

On a political spectrum, the Liberal Party is generally thought of as Canada's centre-left party and the Conservative Party (CPC)  as centre-right; typically, one or the other party is in power at the federal level. The New Democratic Party (NDP) has historically been the labour party while the Green Party foregrounds environmental issues; both tend towards progressive policy-making and would be regarded as left of the Liberal Party. The People's Party of Canada (PPC) is a newly established populist party and considered politically right of the CPC.

If you are downloading the PDF files directly, no pre-processing steps have been performed (the one exception is the People's Party of Canada platform, which was not made available as a single PDF document, and was instead copied from the webpages of a version on the [Internet Archive's Wayback Machine](https://archive.org/web/) crawled the evening before the 2021 federal election). There might be errors in the document as a result of being formatted as a PDF but they are likely to have a negligible effect on our (quick, for demonstration purposes only) analysis.

When working with your own documents, take some time to review them and address spelling errors or other anomalies that may affect your analysis. Topic modeling, like many other computational text analysis techniques, ultimately relies on counting words - and the words must be identical to be counted together (e.g. "labor" and "labour" will be considered two unique words).

<hr />

## Get the software

This hands-on workshop uses three separate tools to perform topic modelling: Voyant Tools, MALLET and Python. You do not have to use all of them, but the intent is for you to get a sense of each with a small sample from your own corpus so that you can choose an approach that works best for you. You can skip this step for now, read ahead in the lesson and come back to the "Preparation" page to download applications as necessary.

[Download Voyant Server](https://voyant-tools.org/docs/#!/guide/server)

[Download MALLET](https://mimno.github.io/Mallet/)

[Download Anaconda](https://www.anaconda.com/products/individual)* (includes Spyder, integrated development environment - or IDE - for Python).

* If you completed the *[Identifying Proper Nouns with Named Entity Recognition](https://scds.github.io/text-analysis-2/)* workshop, you will already have downloaded Anaconda; you may wish to [update Anaconda](https://docs.anaconda.com/anaconda/install/update-version/) or [uninstall and reinstall it](https://docs.anaconda.com/anaconda/install/uninstall/) if you prefer or if you are getting an error message regarding setup-tools.

**If you are not able to download and/or install Anaconda,** you can alternatively follow the lesson via the [Jupyter notebook version of the workshop in Google Colab](https://colab.research.google.com/drive/1biLTOz5Va-824g7o94Le9QIRM0jxx2ty?usp=sharing). You will need to upload the platform text files (after having [exported them from Voyant]([tmv.html#2-explore-the-voyant-dashboard)) to the file area in Google Colab as described in [Jay Brodeur's "Basic Text Prep with Python" Colab notebook](https://colab.research.google.com/drive/1ynkHM3WOQUGj9mj8R060p3BYqI6ThbAj?usp=sharing), step 3. Run the code cell by cell using the "play" button at the left of each cell. 

**If you have programming experience with Python,** you are welcome to use the IDE you are familiar with as an alternative.

Please contact the [Sherman Centre](mailto:scds@mcmaster.ca) if you have any difficulties downloading or opening the software.

<hr />

### Software versions

For the lesson as it is currently written, the software versions are as follows:

**Python:** 3.9

**Anaconda Navigator:** 2.3.2

**Spyder:** 5.4.3

**MALLET:** 202108

If the versions differ from your own, that's ok! There's no need to track down older versions of the software to complete the lesson. The steps should remain the same, but there might be some small variations that can be attributed to using a later version (with the exception of your Python version, which \*might\* break the code; Python 3.9 will be supported until October 2025).

<hr />

## Assemble your own corpus (optional)

In advance of the lesson, we also recommend that you assemble a collection of documents to work with for the *Try it with your data* sections. We will use the texts provided above to practice the techniques demonstrated in the lesson but each dataset brings its own unique features. Even if you are not going through the lesson with a specific project in mind, having a different corpus to experiment with will help to reinforce the concepts and enrich your knowledge of the topic.

If you have not already gone through your corpus to get a sense of what errors it might contain, now is a good time! If key words are misspelled, they may not be emerge as relevant themes through topic modelling.

<br />
Next --> [Start the Topic Modeling Lesson](instructions.html)
