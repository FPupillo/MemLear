#!/bin/bash

# get current folder
wd="/home/francesco/PowerFolders/MemLear"

# assign directories' names
folders="MemLear_ses-01_part-01_label-phase1 MemLear_ses-01_part-02_label-phase2 
MemLear_ses-01_part-02_label-nBack"

for f in $folders
do

# go to the first directory
cd $wd/2_Project_Documents/Data_acquisition/task/$f

pwd

# pull data
git pull

# synchronize with the working folder
rsync -v -r $wd/2_Project_Documents/Data_acquisition/task/$f/data/ \
$wd/2_Analysis_Folder/raw_data

rsync -v -r $wd/2_Project_Documents/Data_acquisition/task/$f/data/ \
$wd/2_Holy_Folder/raw_data

done