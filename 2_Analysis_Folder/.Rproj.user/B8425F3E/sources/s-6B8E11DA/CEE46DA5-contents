# screen data, deleting unuseful data
rm(list=ls())

cd<-getwd()

setwd("raw_data")

# list files
files<-list.files()

# loop through the files
for (f in files){
if (!grepl( "MemLear",f)) { # if this file does not contain "MemLear"
  file.remove(f)
}
}

# delete the files that start with "Participant"
for (f in files){
  if (grepl( "PARTICIPANT",f)) { # if this file does not contain "premceCat2"
    file.remove(f)
  }
}
