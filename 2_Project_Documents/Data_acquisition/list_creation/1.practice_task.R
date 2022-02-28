#------------------------------------------------------------------------------#
#
# script to select the images practice task
#
# created: "Mon Nov  8 11:48:37 2021"
#------------------------------------------------------------------------------#
rm(list=ls())
#------------------------------------------------------------------------------#
Pcong<-0.70   # 75 for the conguent ones, the preferred category
Pincong<-(1-Pcong)/3
#------------------------------------------------------------------------------#

# load the libraries
library("readxl")
library(gtools) # for permutations
library(dplyr)

# source the helper functions
source("helper_functions/checkCont.R")
source("helper_functions/getSum.R")

# retrieve info of the category
category<-read_excel("SI1.xlsx", sheet = "Sheet2")

# check how many categories
# change fourth and fifth name
names(category)[4:5]<-c("modal_categ", "cat_agreement")

# get the number of objects per category
table<-category %>% 
  group_by(modal_categ) %>% 
  tally()

# order by modal categ and name agreement
table<-table[order(table$n, decreasing=T),]

head(table, n=50)

# select the categories
selCat<-c("Gamestoy & entertainment", "Clothing", "Vehicle", 
          "Food")

# create a dataset with only the categories
dataSel<-category[category$modal_categ %in% selCat, ]

# select the the first 60 images with the highest category agreement level 
# for each category, 
# assign them to the relative dataset
for (cat in 1:length(selCat)){
  # subset the database
  datapract<- dataSel[dataSel$modal_categ==selCat[cat],]
  # order it
  datapract<-datapract[order(datapract$cat_agreement, decreasing = T),]
  # select first 40 
  datapractsel<-datapract[1:60,]
  # assign to a dataset
  assign(paste(selCat[cat],"_pract",sep=""), datapractsel)
  
}

# merget the datasets 
data_pract<-rbind(`Gamestoy & entertainment_pract`, `Clothing_pract`, 
                  `Vehicle_pract`, `Food_pract`)

# create a list of characters 
characters<-c("m_red", "m_blue")
categ<-selCat

# for the categories, to have alle the possible permutations of category 
# and position we need 4 factorial (4*3*2*1) =24
categPermut<-permutations(n=4,r=4,v=categ,repeats.allowed=F)

# now we need to have 60 per character and repeat them twice (two characters)
# then repeat the combinations two times (character).
# In total, 96 trials
allcombin<-cbind(character=rep(characters, each=nrow(categPermut)*2))

# now bind the characters with the categories
allList<-data.frame(cbind(allcombin, do.call(rbind, replicate(4, categPermut,
                                                              simplify=FALSE))))

names(allList)[2:5]<-c("left_categ", "centleft_categ", "centright_categ",
                       "right_categ")

#------------------------------------------------------------------------------#
# create the correct choice for the first character
# initialize the variable

AllCharList<-vector()
# contingencies
cont<-list(c(Pincong, Pincong, Pincong,
             Pcong), c(Pcong, Pincong, Pincong, Pincong))

for (n in 1:length(characters)){

# subset the first character's trials
charactList<-allList[(allList$character==characters[n] ),]  

set.seed(12345)

# take 60only per character randomly
charactList<-sample_n(charactList, 40)

# sample the correct answer
corr_ans<-sample(categ,nrow(charactList), prob = c(cont[[n]]), replace = T)

# check how many times it appears
probs<-vector()
for (f in 1:length(categ)){
  probs[f]<-(length(corr_ans[corr_ans==categ[f]]) / length(corr_ans))
}

print(probs)

# function to redistribute the correct responses for butterfly
while (max(probs) != 0.70  | any(probs[! probs %in% max(probs)]<0.10)){ 
 #set.seed(sample(seq(1:1000), 1))
  corr_ans<-sample(categ,nrow(charactList), prob = c(cont[[n]]), replace = T)
  probs<-vector()
  for (f in 1:length(categ)){
    probs[f]<-(length(corr_ans[corr_ans==categ[f]]) / length(corr_ans))
  }
  
  print(probs)
  
}

# we need a variable to indicate whether it is the congruent or not
charactList$trial_cond<-as.numeric(corr_ans==categ[which(probs==max(probs))])

# bind it to the final dataset
charactList$corr_ans<- corr_ans
AllCharList<-rbind(AllCharList,charactList )

}

# now we need to indicate which number is the correct character
AllCharList$corr_ans_num<-NA
for (j in 1: nrow(AllCharList)){
  AllCharList$corr_ans_num[j]<- which(AllCharList[j,2:5]==AllCharList$corr_ans[j])
}

#------------------------------------------------------------------------------#
# check that the number across the characters is okay

# make a table of frequencies
checkCont(AllCharList, 40)

#------------------------------------------------------------------------------#
# now that we have created the list, we can shuffle the order
# shuffle the list : create random numbers of the length of the list
set.seed(12345)

# sample from the list created to create the practice list
pract_list<-sample_n(AllCharList, nrow(AllCharList))

# we don't want two consecutive incongruent trials for each 
# character
pract_list$type<-pract_list$trial_cond
add<-getSum(pract_list)

while(any(add<1, na.rm=T)){
  pract_list<-sample_n(AllCharList, nrow(AllCharList))
  pract_list$type<-pract_list$trial_cond
  
  add <-getSum(pract_list)
}

# check contingencies again
checkCont(pract_list, 40)

#------------------------------------------------------------------------------#
# select the object

# retrieve the objects of the categories of the practice task
objectPract<-data_pract

# store the objects selected
objsel<-vector()
pract_list$image<-NA
set.seed(12345)
for (n in 1:nrow(pract_list)){
  # which category?
  cat<-pract_list$corr_ans[n]
  # subset it
  objects<-objectPract[objectPract$modal_categ==cat,]
  # sample one of them
  objsel[n]<-sample(objects$Filename, 1)
  # assign to the data
  pract_list[n, "image"]<-paste("stimuli/objects/", objsel[n], ".jpg", sep="")
  # delete that object from the objectPract
  objectPract<-objectPract[objectPract$Filename!=objsel[n],]
  
}

# character as .jpg
pract_list$character<-paste("stimuli/",pract_list$character, ".jpg", sep="")

# correct response as key
corr_response<-c("left_categ", "centleft_categ", "centright_categ", "right_categ")

# convert to character
for (c in 1:length(corr_response)){
  pract_list[[corr_response[c]]]<-as.character(pract_list[[corr_response[c]]])
}

# convert to png
for (n in 1:nrow(pract_list)){
  for (c in 1:length(corr_response)){
    pract_list[n, corr_response[c]]<-paste("stimuli/", 
                  as.character(pract_list[n, corr_response[c]]), ".png", sep="")
  }
}

#------------------------------------------------------------------------------#
# print the files

cd<-getwd()

setwd("lists")

# write objects
objsel<-noquote(paste(objsel, ".jpg", sep=""))

write.table(objsel, "images4pract.txt", col.names = F, row.names = F,quote=F)
# write practice list
# but first, rename the "image" variable, as otherwise there will be
# a conflict in pavlovia
names(pract_list)[10]<-"img"

write.table(pract_list, "practlist.csv", 
            col.names = T,row.names = F, quote=F, sep=",")

setwd(cd)

#-----------------------------end----------------------------------------------#

