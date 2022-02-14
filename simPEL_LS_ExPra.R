# Read in and preprocess raw data: simPEL Lifespan
# Sophie Nolden
# Jan 19,2022

remove(list = ls())

library(data.table)
library(dplyr)
library(plyr)
library(psych)
library(ggpubr)
library(ggplot2)
library(rstatix)
library(Rcpp)
library(Rmisc)
library(lattice)

# Define data paths

inPath_recog <- "/media/sophie/6A3EE9913EE9569B/LinkToHessenbox/SophTeaching/2021EmpExPra/Material/6_Data_Analysis/simPEL-LS-ses-3_part-4_label-recog/"

# outPath <- "/"

# Read part 4 - recog
file_names_recog <- list.files(inPath_recog, pattern = "*.csv", full.names = TRUE)
data_recog <- rbindlist(lapply(file_names_recog, fread),fill=TRUE)

#Vector older adults
ID_ya <- c(140, 141, 142, 143, 125, 126, 127, 128, 145, 146, 147, 148, 302, 303, 304, 129)

#Adding a variable for the age group
data_recog$age_group <- "children" 
data_recog$age_group[data_recog$ID %in% ID_ya] <- "youngAdults"

#Remove empty lines
data_recog <- data_recog[!is.na(data_recog$trials.thisIndex)]

#Correcting wrong counterbalancing of "newResp" und "oldResp" for the specific participants
#Changing the levels in oldResp and newResp
data_recog$oldResp[data_recog$ID %in% c(13,21,22,201,210,221,222,250)] <- data_recog$newResp[data_recog$ID %in% c(13,21,22,201,210,221,222,250)]
data_recog$newResp[data_recog$ID %in% c(13,21,22,201,210,221,222,250) & data_recog$oldResp == "left"] <- "right"
data_recog$newResp[data_recog$ID %in% c(13,21,22,201,210,221,222,250) & data_recog$oldResp == "right"] <- "left"
#Changing the levels in corrResp
data_recog$corrResp[data_recog$oldLureFoil == "old"] <- data_recog$oldResp[data_recog$oldLureFoil == "old"]
data_recog$corrResp[data_recog$oldLureFoil == "new/foil"] <- data_recog$newResp[data_recog$oldLureFoil == "new/foil"]
#Changing the levels in recog_resp.corr to see if participants made the right decision
data_recog$recog_resp.corr[data_recog$recog_resp.keys == data_recog$corrResp] <- 1
data_recog$recog_resp.corr[data_recog$recog_resp.keys != data_recog$corrResp] <- 0




#Exclusion criterion:
#Remove participants with very poor recognition memory performance (hit rates for old items – false alarm rates < .05)
#Hits are defined as old or similar responses to old items; false alarms are old or similar responses to new items

#Creating a new variable to determine the hit rate
data_recog$recog_resp.for_exclusion <- 0
data_recog$recog_resp.for_exclusion[data_recog$oldLureFoil=="old" & data_recog$resp=="old"] <- 1
data_recog$recog_resp.for_exclusion[data_recog$oldLureFoil=="old" & data_recog$resp=="sim"] <- 1
data_recog$recog_resp.for_exclusion[data_recog$oldLureFoil=="new/foil" & data_recog$resp=="sim"] <- 1
data_recog$recog_resp.for_exclusion[data_recog$oldLureFoil=="new/foil" & data_recog$resp=="old"] <- 1

#Creating a new data frame with the relevant variables
data_recog_exclusion <- aggregate(data_recog$recog_resp.for_exclusion
                                  ,list(data_recog$oldLureFoil,data_recog$ID)
                                  ,mean)
names(data_recog_exclusion)[1]<-"Item_type"
names(data_recog_exclusion)[2]<-"ID"
names(data_recog_exclusion)[3]<-"old_resp_rate"

data_recog_exclusion <- data_recog_exclusion[!data_recog_exclusion$Item_type == "sim/lure",]

#Grouping the dataframe and computing the recognition memory performance
data_recog_exclusion <- group_by(data_recog_exclusion,ID)
data_recog_exclusion <- mutate(data_recog_exclusion,hits_m_fa = old_resp_rate-(old_resp_rate[1]))
data_recog_exclusion <- data_recog_exclusion[!data_recog_exclusion$Item_type=="new/foil",]

#defining participants that have to be excluded
excluded_recog <- data_recog_exclusion[data_recog_exclusion$hits_m_fa<.05,]$ID
show(excluded_recog)

# Add participant exclusion info to all participants
data_recog$excl_recog <- 0
data_recog$excl_recog[data_recog$ID %in% excluded_recog] <- 1

# Export csv
# write.csv(data_recog, paste(outPath, "data_recog.csv", sep = ""))

#Creating a new variable for what participants indicated (in the terms "new/sim/old")
str(data_recog$recog_resp.keys)
data_recog$recog_resp.keys[data_recog$recog_resp.keys == ""] <- "none"
data_recog$resp <- "old" 
data_recog$resp[data_recog$recog_resp.keys == data_recog$newResp]<- "new"
data_recog$resp[data_recog$recog_resp.keys == data_recog$simResp] <- "sim"
data_recog$resp[data_recog$recog_resp.keys == "none"] <- "none"

# Create variable that codes for old responses
data_recog$old_resp <- 0
data_recog[data_recog$resp == "old"]$old_resp <- 1

# Aggregate raw data
recog_agg <- aggregate(old_resp ~
                      ID + age_group + violation
                    ,data = data_recog[(data_recog$excl_recog == 0 & data_recog$oldLureFoil == "old"),]
                    ,mean)

# Descriptives
by(recog_agg$old_resp, list(recog_agg$violation, recog_agg$age_group), summary)

# ANOVA
ezANOVA(data=recog_agg
        ,dv=old_resp
        ,wid=ID
        ,between = age_group
        ,within=.violation,oldLureFoil)
