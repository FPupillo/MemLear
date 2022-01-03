#------------------------------------------------------------------------------#
# Check the answers
#
#"Sat Dec 18 12:19:50 2021"
#------------------------------------------------------------------------------#
rm(list=ls())

# source the functions
source("helper_functions/cleanData.R")

library(dplyr)
participant<-12

# delete first rows
cleanData(c(participant))

# retrieve the file
file<-read.csv(paste0("clean_data/sub-", participant, "/", participant, "_encoding.csv"))
names(file)

# select the practice trial
practice<-filter(file, !is.na(trial_cond))

# compute the response made by participants
practice$resp_cat<-NA
for (n in 1:nrow(practice)){
practice$resp_cat[n]<-as.character(practice[n,8:11][,practice$pract_resp.keys[n]])
}

# get cumulative accuracy
practice$cumAcc<- cumsum(practice$pract_resp.corr) / seq_along(practice$pract_resp.corr)


names(practice)
VoI<-c("trial_cond","character", "left_categ", "centleft_categ","centright_categ" ,  
       "right_categ" ,  "corr_ans", "img", "corr_ans_num", "pract_resp.keys", "resp_cat",
       "pract_resp.corr", "cumAcc"
       )
practice<-practice[, VoI]               
write.csv(practice,paste0("check_practice_participant_", participant, ".csv"), row.names = F)

#------------------------------------------------------------------------------#
# now the real task
# retrieve the file

# select the main task trial
task<-filter(file, !is.na(task_response.corr))

# compute the response made by participants
task$resp_cat<-NA
for (n in 1:nrow(task)){
  if (!is.na(task$task_response.keys[n])){
  task$resp_cat[n]<-as.character(task[n,8:11][,task$task_response.keys[n]])
}
}
# get cumulative accuracy
task$cumAcc<- cumsum( ifelse(is.na(task$task_response.corr), 0,  task$task_response.corr)) / seq_along(task$task_response.corr)

names(task)
VoI<-c("type","character", "left_categ", "centleft_categ","centright_categ" ,  
       "right_categ" ,  "corr_ans", "img", "corr_ans_num", "task_response.keys", "task_response.corr", "resp_cat",
       "cumAcc", "condition"
)
task<-task[, VoI]               
write.csv(task,paste0("check_task_participant_", participant, ".csv"), row.names = F)
