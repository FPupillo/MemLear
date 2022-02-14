#------------------------------------------------------------------------------#
# 
# Analyze Data Expra
# 
# created: "Wed Jan 19 19:18:16 2022"
# 
# Francesco Pupillo, Goethe University Frankfurt
#
#------------------------------------------------------------------------------#
library(data.table)
library(dplyr)

rm(list=ls())

# retrieve the data

# puth the path with the data
inPath <- "..."

# clean data files
inPath<-"all_file_encoding"

# how many subjects?
subjects<-list.files(inPath)

# import the files
inFiles <- list.files(inPath, pattern="*.csv", full.names=TRUE)

data <- rbindlist(lapply(inFiles,fread),fill=TRUE) 

# create accuracy
#data$accuracy<-ifelse(data$recog_resp.keys == data$corr_ans, 1, 0)

data.agg<-data %>%
  group_by(participant, condition) %>%
  summarise(recog.acc = mean(recogAcc), 
            encoding.acc = mean(task_response.corr))
  

# exlcude participants due to problems with lists 
part.list.exc<-c(12, 13, 21)

# threshold for excluding participants at encoding
thres.encoding<-0.50

# threshold for excluding participants at retrieval
thres.retrieval<-0.50

# in order to have overall perf, let's aggregate without condition
data.agg.all<- data %>%
  group_by(participant) %>%
  summarise(recog.acc = mean(recogAcc, na.rm=T), 
            encoding.acc = mean(task_response.corr))

# which participants to exclude according to encoding performance
part.exc.encod<-data.agg.all$participant[data.agg.all$encoding.acc<thres.encoding ]

# which participants to exclude according to retrieval performance
part.exc.retrieval<-data.agg.all$participant[data.agg.all$recog.acc<thres.retrieval ]

excl.all<-unique(c(part.list.exc, part.exc.encod,part.exc.retrieval ))



dataAgg %>%
  group_by( condition) %>%
  summarise(recogMean = mean(recogAcc, na.rm = T))
# aggregate at the participant level

# summarise, check distribution
