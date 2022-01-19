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

# aggregate at the participant level
data_aggr<-data%>%
      group_by(participant) %>%
    summarise(accuracy = mean(recogAcc))

hist(data_aggr$accuracy)
