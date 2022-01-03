#------------------------------------------------------------------------------#
#
# script to check that the encoding images are are in the recognition lists
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
for (n in 1:4){
  encod<-read.csv(paste0("task_list_", n, ".csv"))
  
  ret1<-read.csv(paste0("ImagesforRecog", n, "_1.csv"))
  ret2<-read.csv(paste0("ImagesforRecog", n, "_2.csv"))
  
  # bind the two
  ret<-rbind(ret1, ret2)
  
  # check
  check<-NA
  for (j in 1:nrow(encod)){
    check[j]<-sum(ret$images== encod$img[j]) 
    
  }
  
  
  assign(paste0("check", n), check)
  
}


