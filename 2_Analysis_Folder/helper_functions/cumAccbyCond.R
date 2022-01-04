cumAccbyCond<-function(dataframe){
  # -------------------------------------------------------------------------------------------------#
  # function to create cumulative accuracy for each character separately
  # INPUT: it takes a dataframe for each block (trials between each change point)
  # OUTPUT: it returns a dataframe with the cumulative accuracy
  # -------------------------------------------------------------------------------------------------#
  
  currlist<-dataframe
  
  # create cumulative accuracy per character
  # first, create trial number for ordering later on
  currlist$trialN<-1:nrow(currlist)
  
  # first character
  currlistssub1<-currlist[currlist$condition== 0,]
  
  # create trialnum by char
  currlistssub1$trialNbychar<-1:nrow(currlistssub1)
  
  # calculatecumacc
  currlistssub1$cumAccbyCond<-
    cumsum(currlistssub1$task_response.corr) / seq_along(currlistssub1$task_response.corr)
  
  # second character
  currlistssub2<-currlist[currlist$condition==1,]
  
  # create trialnum by char
  currlistssub2$trialNbychar<-1:nrow(currlistssub2)
  
  # calculatecumacc
  currlistssub2$cumAccbyCond<-
  cumsum(currlistssub2$task_response.corr) / seq_along(currlistssub2$task_response.corr)
  
  # bind it
  currlist<-rbind(currlistssub1, currlistssub2)
  
  # order it
  currlist<-currlist[order(currlist$trialN),]
  
  # delete trialN
  currlist$trialN<-NULL
  
  return(currlist)
  
}
