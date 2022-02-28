checkCont<-function(df, nTrials){
#------------------------------------------------------------------------------#
# functions that counts the number of trials per characters
#   INPUT: df - a dataframe
#          nTrials - number of trials per characte
#   OUTPUT: two separate tables (one for each character), 
#            with the character, category, number of trials, contingencies
#------------------------------------------------------------------------------#

  table<-data.frame(matrix(NA, nrow= 2, ncol = 5))
  names(table)<-c("character", categ[1], categ[2], categ[3], categ[4])
  
  corrAns<-NA
  character<-NA
  for (j in 1:(nrow(df))){
    corrAns[j]<- as.character(df[j, (df$corr_ans_num[j])+1])
    character[j]<-as.character(df$character[j])
  }
  
  table<-data.frame(cbind(character, corrAns))
  
  table<- table %>%
    arrange(desc(character))
  
  firstChar<-table[1:nTrials,]  %>%
    count (character, corrAns) %>%
    mutate(prop = prop.table(n))
  
  secondChar<-table[(nTrials+1):(nTrials*2),]  %>%
    count (character, corrAns) %>%
    mutate(prop = prop.table(n))
  
  
  return(list("firstChar" =firstChar, "secondChar" = secondChar))
  
}