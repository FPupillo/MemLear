# check object
# check if the objects on the lists are in the txt file
rm(list=ls())
#load the lists

lists<-c("ImagesforRecog1_1.csv", "ImagesforRecog1_2.csv", 
         "ImagesforRecog2_1.csv", "ImagesforRecog2_2.csv", 
         "ImagesforRecog3_1.csv", "ImagesforRecog3_2.csv", 
         "ImagesforRecog4_1.csv", "ImagesforRecog4_2.csv")

# load them 
for (l in 1:length(lists)){
  

allLists<-vector()
for (l in 1:length(lists)){
  allLists<- rbind(allLists, read.csv(paste("lists/", lists[l], sep="")))
}

# load object lists
objlist<-read.table("lists/ImagesforRecog.txt")

# now check if any of objectrs in the lists is present in the object list
present<-vector()
notpresent<-vector()
for (n in 1:nrow(allLists)){
  object<-as.character(allLists$images[n])
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
