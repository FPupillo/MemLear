# File description

This document contains a description of all the files in this folder.
Note that each ".Rmd" output has a corrispondent ".html" file that prints the output and displays it on the browser. 

### all_file_encoding
This folder contains the file for each participant in which the encoding and the recognition tasks have been merged. The merging was created by the script "3.Analysis_recognition.Rmd".

### clean_data
Data by participant for the three parts (encoding, nback, recognition) with only variables of interest selected. The "analyze.data.R" script creates this file. 

### data_files
Temporary folder where the name of the raw files is changed to make it easier to analyze them. the script "renameFiles.R" in the "helper_functions" folder 
exectutes the renaming. 

### other_files
Files that have been used previously but that are not object of the main analyses. 

### raw data
Raw data files


### 1.Analysis_pract
Analysis of the practice trials

### 2.Analysis_task
Analysis of the statistical learning task

### 3. Analysis_recognition
Analysis of the recognition dasta

### 4. Analysis_nBack
Analysis of the n_back trials

### 2_Analysis_folder.Rproj
R project file. It allows for version control and assigns the working directory to this directory. 

### Analysis.expra.R
Script for the expra students. 

### analyze_data.R
This script cleans the data by selecting only the variables of interest. 