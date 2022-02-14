#------------------------------------------------------------------------------#
# merging dataframes
#
#
#
#------------------------------------------------------------------------------#
# first, set the path where you have the "group_data"
path<-"..."

# set in the working directory
setwd(path)

# retrieve the nback
nback<-read.csv("group_data/all.nback.csv")
# select only participant and hit rate
VoI<-c("participant", "hitRate")
nback<-nback[,VoI]

# rename the hit rate
names(nback)[2]<-"hitRate_nBack"

recog<-read.csv("group_data/all.nback.csv")

# merge
All <- merge(recog, nback, by="participant")

# the "hitRate_nBack" has been attached to the recognition dataset