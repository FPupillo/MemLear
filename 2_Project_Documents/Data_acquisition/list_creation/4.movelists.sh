#!/bin/bash

# script to assign lists to the tasks
root="/home/francesco/PowerFolders/MemLear/2_Project_Documents/Data_acquisition"
practlist="practlist.csv"
listenc="task_list_1.csv task_list_2.csv task_list_3.csv task_list_4.csv"
listrecog="ImagesforRecog1_1.csv ImagesforRecog1_2.csv ImagesforRecog2_1.csv ImagesforRecog2_2.csv ImagesforRecog3_1.csv ImagesforRecog3_2.csv ImagesforRecog4_1.csv ImagesforRecog4_2.csv"

#practlist
# copy practlist
cp $root/list_creation/lists/$practlist\
 $root/task/MemLear_ses-01_part-01_label-phase1/

# paste it to the html folder as well
cp $root/list_creation/lists/$practlist\
 $root/task/MemLear_ses-01_part-01_label-phase1/html/resources/

# copy encoding_lists

# lists encoding
for files in $listenc
	do echo $files

# in the psychopy path
cp $root/list_creation/lists/$files\
 $root/task/MemLear_ses-01_part-01_label-phase1/

# in the html path
cp $root/list_creation/lists/$files\
 $root/task/MemLear_ses-01_part-01_label-phase1/html/resources/
done

# lists recogn
for files in $listrecog
	do echo $files

# in the psychopy path
cp $root/list_creation/lists/$files\
 $root/task/MemLear_ses-01_part-02_label-phase2/condition_files/

# in the html path
cp $root/list_creation/lists/$files\
 $root/task/MemLear_ses-01_part-02_label-phase2/html/resources/condition_files/
done