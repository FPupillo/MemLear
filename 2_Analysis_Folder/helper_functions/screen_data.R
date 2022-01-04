# screen data, deleting unuseful data
rm(list=ls())

cd<-getwd()

setwd("raw_data")

# list files
files<-list.files()

# loop through the files
for (f in files){
if (!grepl( "MemLear",f)) { # if this file does not contain "MemLear"
  print(paste0("removed file", f)) # print a message with the file removed
  file.remove(f)
}
}

# delete the files that start with "Participant"
for (f in files){
  if (grepl( "PARTICIPANT",f)) { # if this file does not contain "premceCat2"
    print(paste0("removed file: ", f)) # print a message with the file removed
    file.remove(f)
  }
}

# removed files that are not .csv
csv_files<-files[grep(".csv$", files)]

for (f in files){
  if (any(f==csv_files)==F) { # if this file does not contain "premceCat2"
    print(paste0("removed file: ", f)) # print a message with the file removed
    file.remove(f)
  }
}

# now remove the files that start with 999
for (f in files){
  if (sub("\\_MemLear.*", "", f)==999) { # if this file does not contain "premceCat2"
    print(paste0("removed file: ", f)) # print a message with the file removed
    file.remove(f)
  }
}

# now remove the files bigger than 100
for (f in files){
  if (!is.na(as.numeric(sub("\\_MemLear.*", "", f)))){
  if (as.numeric(sub("\\_MemLear.*", "", f))>100) { # if this file does not contain "premceCat2"
    print(paste0("removed file: ", f)) # print a message with the file removed
    file.remove(f)
  }
  }
}

# remove the files that start with zeros
for (f in files){
  if (!is.na(as.numeric(sub("\\_MemLear.*", "", f)))){
    if (as.numeric(sub("\\_MemLear.*", "", f))<0) { # if this file does not contain "premceCat2"
      print(paste0("removed file: ", f)) # print a message with the file removed
      file.remove(f)
    }
  }
}

# now remove the files that start with an empty string
for (f in files){
  if (sub("\\_MemLear.*", "", f)=="") { # if this file does not contain "premceCat2"
    print(paste0("removed file: ", f)) # print a message with the file removed
    file.remove(f)
  }
}

# now remove the files that are too small
# get the files that remains
files_new<-list.files()

# delete the files that are less that 2000 byte
for (f in files_new){
 if (file.size(f)<8000){
  print(file.size(f))
    print(paste0("removed file: ", f)) # print a message with the file removed
    file.remove(f)
 }
}

# set the working directory in the parent folder
setwd(cd)
