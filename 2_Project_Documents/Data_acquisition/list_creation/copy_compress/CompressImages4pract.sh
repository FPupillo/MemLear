#!/bin/bash

# script to copy the images
folder="/home/francesco/PowerFolders/MemLear/2_Project_Documents/Data_acquisition/task/MemLear_ses-01_part-01_label-phase1/html/resources/stimuli"

while read -r img
do 

echo $img
jpegoptim --size=150k $folder/objects/$img

done < lists/images4pract.txt



