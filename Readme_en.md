marge.exe
# Overview
This is a tool for merging multiple annotation files (XML files) created with Aperio ImageScope and displaying them on a single image.

# Contents
## marge.exe
The main program. Double-click to run.
A black screen will appear briefly, and a file named marge.xml will be created.

## input (folder)
Place the annotation files created with Aperio ImageScope in this folder.
The annotation files placed here will be merged.
This tool does not support annotations with more than one color (layer).
Only one color should be used per annotation file.

## source (folder)
Contains the Python source code files for marge.exe.

## Readme_en.md
This file.

## Readme.txt
Japanese readme file.

## marge.xml
This file is created when the program is executed. It is the merged annotation file.
Load it from Aperio ImageScope to use as an annotation file.

# How to Use
※ This tool will not work on cloud storage folders such as Google Drive.
Please download all files to your local environment and run them from there.

Place the annotation data (XML files) created with Aperio ImageScope into the input folder.
The XML files in this folder will be merged.

Double-click marge.exe. The merging process will be completed automatically.
A black screen (command prompt) will briefly appear and then disappear, which indicates normal operation.

A file named marge.xml will be created. This is the merged annotation data.
Each XML file is saved as a single layer (e.g., if 8 XML files are processed, a single marge.xml file with 8 layers will be created).

Load the marge.xml file from Aperio ImageScope.
Open the file where you want to display the annotation information, then select:
"Annotations" → "Import Annotations from File" and load the marge.xml file.

# Notes
- This program is designed to work with annotations related to .svs files.
It has been tested with .svs and .tiff files, but it may not work with other formats.

- This program does not guarantee compatibility with all annotation formats.
Some annotation files may not be readable.

- This program is intended for merging single-layer annotations only.
If annotations with more than one layer (multiple colors) are used, the display may be corrupted.

- This program was created based on Aperio ImageScope Version 12.3.3.5048.
If the annotation file format is changed in other versions, this program may not work properly.

- It has been confirmed to work on Windows 7, but compatibility with other operating systems is not guaranteed.

- This program comes with no warranty.
The author assumes no responsibility for any damage that may occur from using this program.

- Modification of this program is allowed. However, please inform the author if you redistribute the modified version.

# Change Log
- 2020-06-06 - ver 1.0: Created.
- 2020-06-07 - ver 1.1: Minor fixes.

Author
@satyosh

Email: egetprep@gmail.com

