# Overview

These notes give some guidance on how to update and write the reveal.js slides for the PCC unit as well as some of the different plugins and other tools that have been installed. 

## Getting started

Each of the Core lecture folders contains a markdown file called slides.md, this is read by the index.html file which will also setup the basic reveal.js system and some custom functions to allow different slide templates and code styles.

The main webpage title can be set using the html ```<title>``` tag, but in general it is not required to edit this file much.

## Revel markdown files

Most slides can be written in standard markdown and should work, there are two core tags that allow the slides to be changed. 

The ``--`` tag gives a new vertical slide, at triple ```---``` indicates a new horizontal slide.


# How to add to Slides

For simplicity it is best to create a branch for each slide update you make, this will make tracking and merging easier. I reccomend