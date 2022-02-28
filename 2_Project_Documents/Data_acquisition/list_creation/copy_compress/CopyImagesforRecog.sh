#!/bin/bash

# script to copy the images

task="MemLear_ses-01_part-02_label-phase2"
list="lists/Images_recognition.txt"

while read -r img
do 

echo $img
#cp /home/francesco/PowerFolders/MemLear/2_Project_Documents/Data_acquisition/list_creation/Images/Normative/$img\
 #/home/francesco/PowerFolders/MemLear/2_Project_Documents/Data_acquisition/task/$task/stimuli/objects/

cp /home/francesco/PowerFolders/MemLear/2_Project_Documents/Data_acquisition/list_creation/Images/Normative/$img\
 /home/francesco/PowerFolders/MemLear/2_Project_Documents/Data_acquisition/task/$task/html/resources/stimuli/objects/

done< $list

