#------------------------------------------------------------------------------#
#
# script to check that all images of the lists are in the folders
#
# created:  "Mon Dec 20 21:17:19 2021"
#
#------------------------------------------------------------------------------#
rm(list=ls())

# retrieve the lists
cd<-getwd()

setwd("lists")

files<-list.files()

listN<-4

# counter for the objects
count<-1

# file that stores the images in case they are not found
images<-vector()

for (n in 1:4){
  encod<-read.csv(paste0("task_list_", n, ".csv"))
  
  ret1<-read.csv(paste0("ImagesforRecog", n, "_1.csv"))
  ret2<-read.csv(paste0("ImagesforRecog", n, "_2.csv"))
  
  # bind the two
  ret<-rbind(ret1, ret2)
  
  # first encoding
  taskPath<-"/Users/francesco/PowerFolders/MemLear/2_Project_Documents/Data_acquisition/task/MemLear_ses-01_part-01_label-phase1/html/resources/"
  
  for (j in 1:nrow(encod)){
    image<-encod$img[j]
    
    # check if it exist
    test<-file.exists(paste0(taskPath, image))
    
    if (test==F){
      images[count]<-image
      count<-count+1
    }
  }
  
  # now recognition
  taskPath<-"/Users/francesco/PowerFolders/MemLear/2_Project_Documents/Data_acquisition/task/MemLear_ses-01_part-02_label-phase2/html/resources/"
  
  for (j in 1:nrow(ret)){
    image<-ret$images[j]
    
    # check if it exist
    test<-file.exists(paste0(taskPath, image))
    
    if (test==F){
      images[count]<-image
      count<-count+1
    }
  }
  

}


