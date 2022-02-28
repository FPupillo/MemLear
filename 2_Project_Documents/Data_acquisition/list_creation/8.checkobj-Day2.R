# check object
# check if the objects on the lists are in the txt file
rm(list=ls())
#load the lists

lists<-c("tasklistAplus1.csv", "tasklistAplus2.csv",
         "tasklistAplus3.csv", "tasklistAplus4.csv",
         "tasklistB1.csv", "tasklistB2.csv",
         "tasklistB3.csv", "tasklistB3.csv",
         "tasklistC1.csv", "tasklistC2.csv",
         "tasklistC3.csv","tasklistC4.csv", 
         "tasklistD1.csv", "tasklistD2.csv", "tasklistD3.csv", "tasklistD4.csv")

#lists<-"ImagesDay2"

# load them 
for (l in 1:length(lists)){
  

allLists<-vector()
for (l in 1:length(lists)){
  allLists<- rbind(allLists, read.csv(paste("lists/", lists[l], sep="")))
}

# load object lists
objlist<-read.table("lists/ImagesDay2.txt")

# now check if any of objectrs in the lists is present in the object list
present<-vector()
notpresent<-vector()
for (n in 1:nrow(allLists)){
  object<-as.character(allLists$image[n])
  # substringthe object
  object<-substr(object, 17, nchar(object))
  
  #check if the object is present in the object list
 if (object %in% objlist$V1 ){
   present[n]<-1
 } else{
   present[n]<-0
   notpresent<-c(notpresent, object)
 }
}
}
