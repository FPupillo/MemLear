#!/bin/bash

# script to copy the images

list="object_merlinda.txt"

while read -r img
do 

echo $img
cp /home/francesco/PowerFolders/MemLear/2_Project_Documents/Data_acquisition/list_creation/Images/Normative/$img\
 /home/francesco/PowerFolders/MemLear/2_Project_Documents/Data_acquisition/list_creation/piloting/img_mer/

done< $list

