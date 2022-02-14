
cleanData<-function(ID){
  #----------------------------------------------------------------------------#
  # function that cleans the data
  #   INPUT: 
  #           ID: participant
  #   OUTPUT: - dataframe withonly the variable of interest selected
  #             printed in the output folder
  #----------------------------------------------------------------------------#
  # it requries dplyr
  
  library(dplyr)
  # set to raw data
  cd<-getwd()
  
  # create the folder for the participants' data
  dir.create(paste0("clean_data/sub-", ID), showWarnings = FALSE)
  
  #subject path
  subpath<-paste0(cd, "/clean_data/sub-", ID)
  
  setwd("data_files")  

  # select participants' file
  files<-list.files(pattern = paste0("^", ID,  ".*.csv$"))
  
for (f in files){
    
  tryCatch({
    # if this is the first part
    if (length(grep(pattern="ses-01_part-01", x = f))==1){
      
      file<-read.csv(f)
      
      VoI<- c("participant","Expra.Code" ,"pract_resp.keys","pract_resp.corr",
              "pract_resp.rt","myownaccuracyCORR","character" , "left_categ"  ,               
              "centleft_categ", "centright_categ",
              "right_categ" ,"trial_cond"    ,             
               "corr_ans" , "corr_ans_num"   ,            
             "type" , "img"  ,"task_response.keys"      ,   
     "task_response.corr" ,   "task_response.rt"      ,  "condition"      )
      
      file<- select(file,all_of(VoI ))
      
      # del;ete first rows
      file<-dplyr::filter(file, nchar(as.character(character))>0)
      
      # print the files
      setwd(cd)
      write.csv(file, paste0(subpath,"/", ID, "_encoding.csv"), row.names = F)
      setwd("data_files")  
      
    } else if (length(grep(pattern="nBack", x=f))==1){
    
      file<-read.csv(f)
      VoI<-c("participant", "Expra.Code", "key_resp_4.keys", "key_resp_4.corr" ,
             "key_resp_4.rt" , "word", "CORRanswer","trialtype","hit_NoHit" )
      file<- select(file,all_of(VoI ))
    
      # delete first rows
      file<-filter(file, !is.na(key_resp_4.corr))
      
      # print the files
      setwd(cd)
      write.csv(file, paste0(subpath,"/", ID, "_nBack.csv"), row.names = F)
      setwd("data_files")  
      
    } else if (length(grep(pattern="phase2", x=f))==1){
        file<-read.csv(f)
        VoI<-c("participant", "Expra.Code","recog_resp.keys","recog_resp.rt", "conf_resp.keys","conf_resp.rt",
               "images", "type","corr_ans") 
        file<- select(file,all_of(VoI ))
        # exclude the NA
        file<-filter(file, !is.na(recog_resp.rt))
        # print the files
        setwd(cd)
        write.csv(file, paste0(subpath,"/", ID, "_recog.csv"), row.names = F)
        setwd("data_files")  
        
    }
  
},error=function(e){cat("ERROR :",conditionMessage(e), "\n", f)}) 

}
  
  setwd(cd)
}  