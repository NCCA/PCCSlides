# Overview

These notes give some guidance on how to update and write the reveal.js slides for the PCC unit as well as some of the different plugins and other tools that have been installed. 

## Getting started

Each of the Core lecture folders contains a markdown file called slides.md, this is read by the index.html file which will also setup the basic reveal.js system and some custom functions to allow different slide templates and code styles.

The main webpage title can be set using the html ```<title>``` tag, but in general it is not required to edit this file much.

## Revel markdown files

Most slides can be written in standard markdown and should work, there are two core tags that allow the slides to be changed. 

The ``--`` tag gives a new vertical slide, at triple ```---``` indicates a new horizontal slide.

See the SampleLecture/slides.md file for examples of how to write slides and all the current features / modules added. If you need more put it into a new branch and I will try to add it.


## How to add to Slides

For simplicity it is best to create a branch for each slide update you make, this will make tracking and merging easier. Due to the layout of the javascript projects everything must be pathed relative, or with ../js/ etc.

# Labs

The labs will get rendered from the README.md file in the labs folder, this is a standard markdown file and should be updated in the same way as the slides.md file only this will be rendered using the github markdown renderer. 

It is possible to add script tags in the top for things like asciinema etc, but again this must be pathed relative to the index.html file.