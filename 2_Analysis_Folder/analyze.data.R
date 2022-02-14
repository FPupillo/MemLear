#------------------------------------------------------------------------------#
# script that analyze the data of the participants
#------------------------------------------------------------------------------#

# clean the data for the participants
rm(list=ls())

cd<-getwd()
source("helper_functions/renameFiles.R")
setwd(cd)
source("helper_functions/cleanData.R")
source("helper_functions/analyzeRecog.R")

# set the folder in the raw data
setwd("data_files")

# get the number of participant
files<-list.files()

#participants
participants<- unique(sub("\\_.*", "", files))

setwd(cd)

# clean the files for the participants

for (p in participants){
  tryCatch({
  cleanData(p)
  #assign(paste0("recog_", p), analyzeRecog(p))
  #all_data<-rbind(all_data, get(paste0("recog_", p)))
  
    error= function(e) {print(paste("problem with participant", p))}
  })
      
}

# # now analyse the results
# # render the Rmd file
# for (p in participants){
# rmarkdown::render('analysis_part1.Rmd', params = list(ID = p), output_dir = 
#                     paste0("clean_data/sub-", p))
# }

# do the group analysis
