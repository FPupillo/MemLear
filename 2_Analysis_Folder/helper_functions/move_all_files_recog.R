#------------------------------------------------------------------------------#
# 
# Analyze Data Expra
# 
# created: "Wed Jan 19 19:18:16 2022"
# 
# Francesco Pupillo, Goethe University Frankfurt
#
#------------------------------------------------------------------------------#

rm(list=ls())

# retrieve the data

# puth the path with the data
inPath <- "..."

# clean data files
inPath<-"clean_data"

# how many subjects?
subjects<-list.files(inPath)

# move the files
dir.create("all_file_recog")
for (s in subjects){
  file<-paste0(inPath, "/", s, "/", substr(s, 5,6), "_recog.csv" )
  file.copy(file, paste0("all_file_recog/",  substr(s, 5,6), "_recog.csv") , overwrite = F)
}
