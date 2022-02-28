#!/bin/bash

# script to copy the images
folder="/home/francesco/PowerFolders/MemLear/2_Project_Documents/Data_acquisition/task/MemLear_ses-01_part-02_label-phase2/html/resources/stimuli"
while read -r img
do 

echo $img
convert $folder/objects/$img \
-colorspace Gray $folder/objects/$img

done < lists/Images_recognition.txt



