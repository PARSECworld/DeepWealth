#library

library(rdhs)
library(census.tools)
library(haven)
library(gtools)
library(reshape2)
library(ggplot2)
library(dplyr)
library(FNN)
library(FactoMineR)
library(factoextra)
library(dplyr)
library(psych)

#terminal

set_rdhs_config(email = "ali.benabbes@fondationbiodiversite.fr",
                project = "Poverty estimation using deep learning approaches and remote sensing data")

#countries
country_ids <- c("AO", "BJ", "BF","CM","CI","CD","ET","GH","GN","KE","LS","MD",
                 "MW","ML","MZ", "NG","RW","SN","SL","TZ","TG","UG","ZM", "ZW","KM")


#start_date and end_date
survs <- rdhs::dhs_surveys(countryIds =country_ids , surveyYearStart = 1996,
                           surveyYearEnd = 2020)



datasets <- rdhs::dhs_datasets(surveyIds = survs$SurveyId, fileFormat = "FL")

dataset_names <- datasets$FileName[datasets$FileType == "Household Recode"]


d <- rdhs::get_datasets(dataset_names)

qus <- rdhs:::search_variable_labels(dataset_names,
                                     search_terms = "Number of household members|household number|Cluster number|Region of residence|Main material of floor|Type of place of residence|Electricity|Floor|Water|Toilet|mobile telephone|Radio|television|Car|motorcycle|Rooms|refrigerator|Has telephone")




variable <- qus$variable[1:15]



vars <- rdhs:::search_variables(dataset_names, variable)


extract <- rdhs::extract_dhs(vars, add_geo = TRUE)


final_df_all1 <- plyr::rbind.fill(extract)


write.csv(final_df_all1,"dhs2000.csv")



final_df_all1 <- read.csv("dhs2000.csv")


final_df_all1$hv221 = ifelse(final_df_all1$hv221==0 | is.na(final_df_all1$hv221), final_df_all1$hv243a, final_df_all1$hv221)


final_df_all1<- final_df_all1[,-c(16, 18, 21, 22)] # On supprime la 6eme colonne


final_df_all1[final_df_all1==99] = NA



final_df_all1 = final_df_all1[complete.cases(final_df_all1), ]


final_df_all1$country <- substr(final_df_all1$SurveyId,1,2)
final_df_all1$year <- substr(final_df_all1$SurveyId,3,6)



x <- rep(NA, nrow(final_df_all1))
x <- ifelse(final_df_all1$country == "AO", "angola", x)
x <- ifelse(final_df_all1$country == "BJ", "benin",  x)
x <- ifelse(final_df_all1$country == "BF", "burkina_faso", x)
x <- ifelse(final_df_all1$country == "CM", "cameroon", x)
x <- ifelse(final_df_all1$country == "CI", "cote_d_ivoire", x)
x <- ifelse(final_df_all1$country == "CD", "democratic_republic_of_congo", x)
x <- ifelse(final_df_all1$country == "ET", "ethiopia", x)
x <- ifelse(final_df_all1$country == "GH", "ghana", x)
x <- ifelse(final_df_all1$country == "GN", "guinea", x)
x <- ifelse(final_df_all1$country == "KE", "kenya", x)
x <- ifelse(final_df_all1$country == "LS", "lesotho", x)
x <- ifelse(final_df_all1$country == "MW", "malawi", x)
x <- ifelse(final_df_all1$country == "ML", "mali", x)
x <- ifelse(final_df_all1$country == "MD", "madagascar", x)
x <- ifelse(final_df_all1$country == "MZ", "mozambique", x)
x <- ifelse(final_df_all1$country == "NG", "nigeria", x)
x <- ifelse(final_df_all1$country == "RW", "rwanda", x)
x <- ifelse(final_df_all1$country == "SN", "senegal", x)
x <- ifelse(final_df_all1$country == "SL", "sierra_leone", x)
x <- ifelse(final_df_all1$country == "TZ", "tanzania", x)
x <- ifelse(final_df_all1$country == "TG", "togo", x)
x <- ifelse(final_df_all1$country == "UG", "uganda", x)
x <- ifelse(final_df_all1$country == "ZM", "zambia", x)
x <- ifelse(final_df_all1$country == "ZW", "zimbabwe", x)



final_df_all1$country <- x


final_df_all1$country_year= paste(sep="_", final_df_all1$country, final_df_all1$year)


# ajouter attribut rooms




# TZ2003AIS-Hv 216

survs <- rdhs::dhs_surveys(countryIds = "TZ", surveyYearStart = 2003,
                           surveyYearEnd = 2003)

datasets <- rdhs::dhs_datasets(surveyIds = survs$SurveyId, fileFormat = "FL")
dataset_names <- datasets$FileName[datasets$FileType == "Household Recode"]
d <- rdhs::get_datasets(dataset_names)
qus1 <- rdhs:::search_variable_labels(dataset_names, search_terms = "household number|Cluster number|Rooms")
variable <- qus1$variable[1:3]
vars <- rdhs:::search_variables(dataset_names, variable)
extract <- rdhs::extract_dhs(vars)
rooms1 <- plyr::rbind.fill(extract)



# ZW2005DHS hv 216
survs <- rdhs::dhs_surveys(countryIds = "ZW", surveyYearStart = 2005,
                           surveyYearEnd = 2005)

datasets <- rdhs::dhs_datasets(surveyIds = survs$SurveyId, fileFormat = "FL")
dataset_names <- datasets$FileName[datasets$FileType == "Household Recode"]
d <- rdhs::get_datasets(dataset_names)
qus1 <- rdhs:::search_variable_labels(dataset_names, search_terms = "household number|Cluster number|Rooms")
variable <- qus1$variable[1:3]
vars <- rdhs:::search_variables(dataset_names, variable)
extract <- rdhs::extract_dhs(vars)
rooms2 <- plyr::rbind.fill(extract)

colnames(rooms2)<- c("hv001","hv002","hv216","SurveyId")
# CM2004DHS sh26a

survs <- rdhs::dhs_surveys(countryIds = "CM", surveyYearStart = 2004,
                           surveyYearEnd = 2004)

datasets <- rdhs::dhs_datasets(surveyIds = survs$SurveyId, fileFormat = "FL")
dataset_names <- datasets$FileName[datasets$FileType == "Household Recode"]
d <- rdhs::get_datasets(dataset_names)
qus1 <- rdhs:::search_variable_labels(dataset_names, search_terms = "household number|Cluster number|Rooms")
variable <- qus1$variable[1:4]
vars <- rdhs:::search_variables(dataset_names, variable)
extract <- rdhs::extract_dhs(vars)
rooms3 <- plyr::rbind.fill(extract)
rooms3<- rooms3[,-c(3)]
colnames(rooms3)<- c("hv001","hv002","hv216","SurveyId")

#ET2000DHS sh27b

survs <- rdhs::dhs_surveys(countryIds = "ET", surveyYearStart = 2000,
                           surveyYearEnd = 2000)

datasets <- rdhs::dhs_datasets(surveyIds = survs$SurveyId, fileFormat = "FL")
dataset_names <- datasets$FileName[datasets$FileType == "Household Recode"]
d <- rdhs::get_datasets(dataset_names)
qus1 <- rdhs:::search_variable_labels(dataset_names, search_terms = "household number|Cluster number|Rooms")
variable <- qus1$variable[1:3]
vars <- rdhs:::search_variables(dataset_names, variable)
extract <- rdhs::extract_dhs(vars)
rooms4 <- plyr::rbind.fill(extract)
colnames(rooms4)<- c("hv001","hv002","hv216","SurveyId")

#ET2005DHS sh40
survs <- rdhs::dhs_surveys(countryIds = "ET", surveyYearStart = 2005,
                           surveyYearEnd = 2005)

datasets <- rdhs::dhs_datasets(surveyIds = survs$SurveyId, fileFormat = "FL")
dataset_names <- datasets$FileName[datasets$FileType == "Household Recode"]
d <- rdhs::get_datasets(dataset_names)
qus1 <- rdhs:::search_variable_labels(dataset_names, search_terms = "household number|Cluster number|Rooms")
variable <- qus1$variable[1:3]
vars <- rdhs:::search_variables(dataset_names, variable)
extract <- rdhs::extract_dhs(vars)
rooms5 <- plyr::rbind.fill(extract)
colnames(rooms5)<- c("hv001","hv002","hv216","SurveyId")
#KE2003DHS sh25a


survs <- rdhs::dhs_surveys(countryIds = "KE", surveyYearStart = 2003,
                           surveyYearEnd = 2003)

datasets <- rdhs::dhs_datasets(surveyIds = survs$SurveyId, fileFormat = "FL")
dataset_names <- datasets$FileName[datasets$FileType == "Household Recode"]
d <- rdhs::get_datasets(dataset_names)
qus1 <- rdhs:::search_variable_labels(dataset_names, search_terms = "household number|Cluster number|Rooms")
variable <- qus1$variable[1:3]
vars <- rdhs:::search_variables(dataset_names, variable)
extract <- rdhs::extract_dhs(vars)
rooms6 <- plyr::rbind.fill(extract)
colnames(rooms6)<- c("hv001","hv002","hv216","SurveyId")
#MW2004DHS sh29a

survs <- rdhs::dhs_surveys(countryIds = "MW", surveyYearStart = 2004,
                           surveyYearEnd = 2004)

datasets <- rdhs::dhs_datasets(surveyIds = survs$SurveyId, fileFormat = "FL")
dataset_names <- datasets$FileName[datasets$FileType == "Household Recode"]
d <- rdhs::get_datasets(dataset_names)
qus1 <- rdhs:::search_variable_labels(dataset_names, search_terms = "household number|Cluster number|Rooms")
variable <- qus1$variable[1:3]
vars <- rdhs:::search_variables(dataset_names, variable)
extract <- rdhs::extract_dhs(vars)
rooms7 <- plyr::rbind.fill(extract)
colnames(rooms7)<- c("hv001","hv002","hv216","SurveyId")
#MZ2003DHS sh55

survs <- rdhs::dhs_surveys(countryIds = "MZ", surveyYearStart = 2003,
                           surveyYearEnd = 2003)

datasets <- rdhs::dhs_datasets(surveyIds = survs$SurveyId, fileFormat = "FL")
dataset_names <- datasets$FileName[datasets$FileType == "Household Recode"]
d <- rdhs::get_datasets(dataset_names)
qus1 <- rdhs:::search_variable_labels(dataset_names, search_terms = "household number|Cluster number|Rooms")
variable <- qus1$variable[1:3]
vars <- rdhs:::search_variables(dataset_names, variable)
extract <- rdhs::extract_dhs(vars)
rooms8 <- plyr::rbind.fill(extract)
colnames(rooms8)<- c("hv001","hv002","hv216","SurveyId")
# NG2003DHS sh26a
survs <- rdhs::dhs_surveys(countryIds = "NG", surveyYearStart = 2003,
                           surveyYearEnd = 2003)

datasets <- rdhs::dhs_datasets(surveyIds = survs$SurveyId, fileFormat = "FL")
dataset_names <- datasets$FileName[datasets$FileType == "Household Recode"]
d <- rdhs::get_datasets(dataset_names)
qus1 <- rdhs:::search_variable_labels(dataset_names, search_terms = "household number|Cluster number|Rooms")
variable <- qus1$variable[1:3]
vars <- rdhs:::search_variables(dataset_names, variable)
extract <- rdhs::extract_dhs(vars)
rooms9 <- plyr::rbind.fill(extract)
colnames(rooms9)<- c("hv001","hv002","hv216","SurveyId")
#TZ2004DHS sh27c



-----------------------------



#2006-2019

country_ids <- c("AO", "BJ", "BF","CM","CI","CD","ET","GH","GN","KE","LS","MD",
                 "MW","ML","MZ", "NG","RW","SN","SL","TZ","TG","UG","ZM", "ZW")

survs <- rdhs::dhs_surveys(countryIds = country_ids, surveyYearStart = 2006,
                           surveyYearEnd = 2019)

datasets <- rdhs::dhs_datasets(surveyIds = survs$SurveyId, fileFormat = "FL")
dataset_names <- datasets$FileName[datasets$FileType == "Household Recode"]
d <- rdhs::get_datasets(dataset_names)
qus1 <- rdhs:::search_variable_labels(dataset_names, search_terms = "household number|Cluster number|Rooms")
variable1 <- qus1$variable[1]
variable2 <- qus1$variable[2]
variable3 <- qus1$variable[8]
variable=c(variable1,variable2,variable3)
vars <- rdhs:::search_variables(dataset_names, variable)
extract <- rdhs::extract_dhs(vars)
rooms12 <- plyr::rbind.fill(extract)

rooms12<-rooms12[,c(1,2,4,3)]


allrooms=rbind(rooms1,rooms2,rooms3,rooms4,rooms5,rooms6,rooms7,rooms8,rooms9,rooms12)




dhs<-right_join(allrooms, final_df_all1)
dhs<-dhs[, -c(5,18)]


dhs<-dhs[,c(4,21,19,20,6,17,18,1,2,5,3,7,8,9,10,11,12,13,14,15,16)]




colnames(dhs)<- c("SurveyId","country_year","contry","year","urban","lat","lon","cluster","household_number","household_members","rooms",
                  "water_code", "toilet_code", "electric","radio", "tv","fridge","motorcycle","car","floor_code","phone")





dhs$roomspp = dhs$rooms/ifelse(dhs$household_members==0, 1, dhs$household_members)


#transform the variables that aren’t numeric to be numeric

toiletcode <-read_dta("/home/ali/Documents/rdhs/toilet_recode.dta")
floortcode <-read_dta("/home/ali/Documents/rdhs/floor_recode.dta")
watercode <-read_dta("/home/ali/Documents/rdhs/water_recode.dta")

dhs = merge(dhs, floortcode, by="floor_code", all.x=T)

dhs = merge(dhs, watercode, by="water_code", all.x=T)

dhs = merge(dhs, toiletcode, by="toilet_code", all.x=T)

#Select the input of the PCA
dhs = dhs %>% dplyr::select(SurveyId, country_year,country, year, cluster, urban, roomspp, electric, tv, car,
                            phone, radio, fridge, motorcycle, floor_qual, toilet_qual, water_qual,lat,lon)


dhs[dhs==99] = NA

dhs = dhs[complete.cases(dhs), ]




#PCA


prn <- psych::principal(dhs[,7:17])


#Loading weight

loadings(prn)


#Wealth index from the  first component
dhs$Wealth_index =prn$scores[, 1]



dhs_agg = dhs %>% dplyr::group_by(contry, year, cluster,lat,lon) %>%
  dplyr::summarize(urban=unique(urban),
                   Wealth_index=mean(Wealth_index), n=n())


pos_0 <- which(dhs_agg$lat == 0)

if (length(pos_0) > 0)
  dhs_agg <- dhs_agg[-pos_0, ]

for (i in 3:ncol(dhs)) {

  pos_NA <- which(is.na(dhs_agg[ , i]))

  if (length(pos_NA) > 0)
    dhs_agg<- dhs_agg[-pos_NA, ]

}


dhs_agg$urban=ifelse(dhs_agg$urban==2,0,dhs_agg$urban)

dhs_agg = dhs_agg[dhs_agg$Wealth_index<2.66,]





