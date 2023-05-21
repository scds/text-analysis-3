---
layout: default
title: Topic Modeling with Voyant Tools
parent: Lesson
nav_order: 2
---

# Topic Modeling with Voyant Tools

Voyant Tools is a visual text analysis environment designed by (and for!) digital humanists. It is a feature-rich yet accessible tool for performing a range of analytical tasks with text data. Later in the lesson, we will use the Python programming language for topic modeling; although the Python approach offers a greater number of parameters to experiment with, it can also require a greater level of comfort with writing code to troubleshoot errors. Voyant has a graphical interface, and - in addition to modeling topics - can map text data to scatterplots, network graphs, stream graphs and more.

You might find that Voyant Tools is entirely sufficient for your purposes. In which case, you can forego the rest of the lesson - but you may also want to try the other methods out for comparison sake, even if they require an increasing degree of comfort with programming concepts and the command line interface. Working with practical and meaningful examples is a great way to learn those skills!

## Voyant Tools - using the web app

[Voyant Tools](https://voyant-tools.org/) is a web application that is free to use and does not require creating an account. You simply upload your texts - Voyant can read text from [a wide number of file formats](https://voyant-tools.org/docs/#!/guide/corpuscreator-section-input-format) - and analyze to your heart's content! You can even return to the dashboard that you created with your corpus by making note of the URL; Voyant will store your documents for a period of time, but they will be deleted after a certain point - so you may wish to use Voyant Server (below) if you want to be able to come back to your corpus again and again.



## Voyant Tools - using the server

Voyant Tools has a downloadable version of the application available in the form [Voyant Server](https://github.com/voyanttools/VoyantServer/releases/tag/2.6.5). Voyant Server can be run from your computer without an Internet connection, and accessed via your web browser. The user experience of Voyant Server is identical to that of the web app we used in the previous section.

Using Voyant Server is the preferred approach if you will be working with very large corpora or if you are working with documents that should not be publically accessible due to privacy or copyright concerns (although you can password protect your corpus). One drawback of Voyant Server, however, is that it relies on a very narrow window of Java versions - between Java 8 and Java 11.

If you have Java 8, 9, 10 or 11 installed on your computer, Voyant Server will be relatively easy to use. Otherwise, you may need to run multiple versions of Java on your machine - which is doable! - but more involved. Refer to instructions on running multiple versions of Java [in Windows (Sven Woltmann)](https://www.happycoders.eu/java/how-to-switch-multiple-java-versions-windows/) or [on Mac (Jayson Minard on StackOverflow)](https://stackoverflow.com/questions/52524112/how-do-i-install-java-on-mac-osx-allowing-version-switching/52524114#52524114).


Next --> [Topic Modeling with MALLET](mallet.html)


<br />
