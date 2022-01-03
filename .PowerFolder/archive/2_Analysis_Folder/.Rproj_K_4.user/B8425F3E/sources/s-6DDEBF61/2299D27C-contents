
# clean the data for the participants

cd<-getwd()
source("helper_functions/cleanData.R")
source("helper_functions/analyzeRecog.R")
# set the folder in the raw data
setwd("raw_data")

# get the number of participant
files<-list.files()

#participants
participants<-c(11, 12, 13,14, 21, 22)

setwd(cd)
# clean the files for the participants
for (p in participants){
  cleanData(p)
  assign(paste0("recog_", p), analyzeRecog(p))
         
}

# now analyse the results

