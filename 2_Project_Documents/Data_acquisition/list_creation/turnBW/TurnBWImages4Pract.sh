#!/bin/bash

folder="/home/francesco/PowerFolders/MemLear/2_Project_Documents/Data_acquisition/task/MemLear_ses-01_part-01_label-phase1/html/resources/stimuli"
# script to copy the images
while read -r img
do 

echo $img
convert $folder/objects/$img \
-colorspace Gray $folder/objects/$img

done < lists/images4pract.txt



