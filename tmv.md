---
layout: default
title: Topic Modeling with Voyant Tools
parent: Lesson
nav_order: 2
---

# Topic Modeling with Voyant Tools

Voyant Tools is an open-source visual text analysis environment designed by (and for!) digital humanists. It is a feature-rich yet accessible tool for performing a range of analytical tasks with text data. Later in the lesson, we will use the Python programming language for topic modeling; although the Python approach offers a greater number of parameters to experiment with, it can also require a greater level of comfort with writing code to troubleshoot errors. Voyant has a graphical interface, and - in addition to modeling topics - can map text data to scatterplots, network graphs, stream graphs and more.

You might find that Voyant Tools is entirely sufficient for your purposes. In which case, you can forego the rest of the lesson - but you may also want to try the other methods out for comparison sake, even if they require an increasing degree of comfort with programming concepts and the command line interface. Working with practical and meaningful examples is a great way to learn those skills!

## Voyant Tools

[Voyant Tools](https://voyant-tools.org/) is a web application that is free to use and does not require creating an account. You simply upload your texts and analyze to your heart's content! You can even return to the dashboard that you created with your corpus by making note of the URL; Voyant will store your documents for a period of time, though they will be deleted after a certain point - so you may wish to use Voyant Server (below) if you want to be able to come back to your corpus again and again.

<hr />

Jump to step >

1. [Upload documents](#1-upload-documents)
2. [Explore the Voyant dashboard](#2-explore-the-voyant-dashboard)
3. [Focus on topic modeling](#3-focus-on-topic-modeling)

<hr />

## **1.** Upload documents

We will first upload the documents to Voyant Tools. The Voyant Tools homepage is very simple in its design and, again, does not prompt you to do anything or provide any information aside from the documents of the corpus itself:

![Screenshot of Voyant homepage, which is primarily blank except for a rectangle at the center of the page that reads "Add texts" with a large blue "Reveal" button and, at the top of a page, a large Voyant Tool logo where the "O" in Voyant is an adorable cartoon owl.](assets/img/voyant-home.png)

Voyant can read text from [a wide number of file formats](https://voyant-tools.org/docs/#!/guide/corpuscreator-section-input-format), including HTML, MS Word, ODT, Pages and PDF. It can even attempt to read text in tables, and you can provide additional directions on how to treat the tabular data by using the "Options" button hightlighted with an arrow in the screenshot of available options below:

![](assets/img/voyant-password.png)

In the options menu, you will also note the ability to protect a corpus from public access by creating a password. You may wish to explore the other options in the menu working with your own corpus; being able to start and / or stop reading when Voyant encounters a specified regular expression, for example, is helpful when working with texts that have preambles or postscripts you want to omit (e.g. files from Project Gutenberg).

**Important note:** if you need to set options, do so before uploading your documents. You will not be able to go back to the options after the dashboard is created, a process that begins as soon as the documents are uploaded.  

We will be using our own texts ("Upload") and not the pre-loaded corpora ("Open"), so Voyant will prompt us to upload them using a system dialog box. You can select multiple files by selecting the first option, holding the Shift key and selecting the last option in your list of documents. If you miss or forget a document, there will be an option to upload additional documents from the Voyant dashboard.

![](assets/img/voyant-upload.png)

When you have selected your documents, Voyant will set about creating the dashboard immediately - which is why you will want to set any option parameters you need to adjust before uploading. It may take a few minutes for Voyant to create the dashboard initially, however, as it must read the PDF files; plain text files are relatively easy for Voyant to work with but if you have a large corpus, it may also take a while. A good time to grab a snack!

If you have any trouble creating the corpus, you can use [the pre-loaded corpus with the lesson documents](https://voyant-tools.org/?corpus=e3e0d4140c53fc8ab68e19521f0ba24a) - although the link will at some point become inactive (corpus created May 21, 2023).

**Another important note:** when your dashboard is ready, **bookmark (or otherwise record) the URL**. Pasting the URL in your browser is the only way to return to it later; there is no global corpus search mechanism in Voyant, and no information is gathered from you to identify your corpus.  

## **2.** Explore the Voyant dashboard

You will eventually be directed to the Voyant dashboard with your documents loaded, which will appear similar to the screenshot below:

![Voyant dashboard divided into five rectangular areas - three on top and two below - that each contain the visualization for a different tools. In the default arrangement, the tools are (in clockwise order starting from top left): Cirrus, Reader, Trends, Summary and Contexts.](assets/img/voyant-full-dash.png)

There is much to explore! We encourage you to take a few minutes to try out some of the text analysis tools within Voyant. In particular, you may want to perform a bit of initial data analysis to identify any errors that may affect our results.

The Summary tool in the bottom left corner gives us an overview of the text data in each document. If we scroll down in the tool, we will come across information about words, or tokens, in the corpus. The Summmary tool highlights the most used words in the corpus - canada, government, canadians, new and support - as well as the most distinctive words within each document.

![](assets/img/voyant-summary.png)

For the Green Party, "reen" and "inctive" are distinctive words within the document... but not words within the English language! Using the Reader tool, found at the centre of the top row of tools, we can search for "reen" and observe a formatting error in the PDF related to a reoccurring header - that we would probably want to omit from our analysis anyway.

![](assets/img/voyant-reader.png)

Of course, we have not performed any pre-processing steps on our documents because we are using them as a quick example to demonstrate the use of Voyant. Normally, we would try to catch and correct such errors before uploading the documents to Voyant (although you may want to use Voyant as an initial data analysis tool to surface repeated spelling errors). When you are working with your own documents, you can likely appreciate the importance of taking the time to verify the accuracy of the data!

The other task we strongly recommend performing is actually to *download* the corpus documents for use in later steps of the lesson. Voyant has handily converted the PDF documents to a text format that we can export to a plain text file, which will make using them with MALLET and Python easier.

You can download the documents in plain text format by replacing the Summary tool with the Documents tool in the bottom left corner of the default Voyant dashboard. The "Download" button depicted in the screenshot below will then become visible. When choosing download options, 
ensure the "plain text" option is selected. Voyant will provide you with a .zip file containing each of the documents in .txt file format.

![Screenshot of Documents tool download dialog box, highlighting "Documents", "Download" and "plain text" buttons.](assets/img/voyant-download.png)

## **3.** Focus on topic modeling

## Voyant Tools Server

Voyant Tools has a downloadable version of the application available in the form [Voyant Server](https://github.com/voyanttools/VoyantServer/releases/tag/2.6.5). Voyant Server can be run from your computer without an Internet connection, and accessed via your web browser. The user experience of Voyant Server is identical to that of the web app we used in the previous section.

Using Voyant Server is the preferred approach if you will be working with very large corpora or if you are working with documents that should not be publically accessible due to privacy or copyright concerns (although you can password protect your corpus). One drawback of Voyant Server, however, is that it relies on a very narrow window of Java versions - between Java 8 and Java 11.

If you have Java 8, 9, 10 or 11 installed on your computer, Voyant Server will be relatively easy to use. Otherwise, you may need to run multiple versions of Java on your machine - which is doable! - but more involved. Refer to instructions on running multiple versions of Java [in Windows (Sven Woltmann)](https://www.happycoders.eu/java/how-to-switch-multiple-java-versions-windows/) or [on Mac (Jayson Minard on StackOverflow)](https://stackoverflow.com/questions/52524112/how-do-i-install-java-on-mac-osx-allowing-version-switching/52524114#52524114).


Next --> [Topic Modeling with MALLET](mallet.html)


<br />
