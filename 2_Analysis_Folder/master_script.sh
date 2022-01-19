# First, pull data from pavlovia and move them to the raw_data folder
#sh pulldata.sh

# then remove unnecessary files
Rscript helper_functions/screen_data.R

# finally rename the files so that the first participants are "01" rather than "0" and copy to the "data_files" folder
Rscript helper_functions/renameFiles.R

Rscript helper_functions/cleanData.R

# Run the analysis scripts
#Rscript -e "rmarkdown::render('analysis_files/01.analysis_day1.Rmd')" 
#Rscript -e "rmarkdown::render('analysis_files/02.analysis_day2-contingencies.Rmd')" 
#Rscript -e "rmarkdown::render('analysis_files/03.analysis_day2-recog.Rmd')" 

#Rscript analysis_files/02.analysis_day2-contingencies.R
#Rscript analysis_files/03.item_analysis.R

#Rscript -e "rmarkdown::render('analysis_files/analysis.Rmd')" 
