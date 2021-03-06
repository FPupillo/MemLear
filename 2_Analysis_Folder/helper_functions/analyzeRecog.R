analyzeRecog<-function(ID){
#----------------------------------------------------------------------------#
# function that analyse participants' performacne
# INPUT - ID
# OUTPUT - general recognition performance
#----------------------------------------------------------------------------#

# get the file recog
file<-read.csv(paste0("clean_data/sub-", ID,"/", ID, "_recog.csv" ))
              
# get the file enc
fileEnc<-read.csv(paste0("clean_data/sub-", ID,"/", ID, "_encoding.csv" ))

# compute accuracy
file$acc<-ifelse(file$recog_resp.keys==file$corr_ans, 1,0)

# calculate hit, miss, rej, and FA
file$recog_type<-NA
for ( i in 1:nrow(file)){
  if (file$corr_ans[i]=="left"& file$recog_resp.keys[i]=="left" ){
    file$recog_type[i]<-"HIT"
  } else if (file$corr_ans[i]=="left"& file$recog_resp.keys[i]=="right" ){
    file$recog_type[i]<-"Miss"
  } else if(file$corr_ans[i]=="right"& file$recog_resp.keys[i]=="right" ){
    file$recog_type[i]<-"CorrRej"
  } else if (file$corr_ans[i]=="right"& file$recog_resp.keys[i]=="left" ){
    file$recog_type[i]<-"FA"
  }
}

VoI<-c("recog_type")

# wide dataset
wideData<-table(file[,VoI])

# convert it to a data.frame
wideData<-as.data.frame(rbind(wideData))

# include row names
#wideData$SubNum<-rownames(wideData)

# reorder the columns to make the id variable the first one
#wideData<-wideData[, c(5,1:4)]

# compute percentage HIT
wideData$HITrate<-wideData$HIT/(wideData$HIT+wideData$Miss)

# percentage false alarm
wideData$FArate<-wideData$FA/(wideData$FA+wideData$CorrRej)

# calculate dprime
library(psycho)

indices <- psycho::dprime(wideData$HIT, wideData$FA, wideData$Miss, wideData$CorrRej)
wideData<-cbind(wideData, indices)

# PR
wideData$hitMinFA<-wideData$HITrate-wideData$FArate

# now the long dataframe
fileEnc$recogAcc<-NA
for (n in 1:nrow(fileEnc)){
  if (length(file$acc[file$images==fileEnc$img[n]])!=0){
  fileEnc$recogAcc[n]<-file$acc[file$images==fileEnc$img[n]]
  }
}

return(wideData)
}

