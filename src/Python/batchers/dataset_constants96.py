DHS_COUNTRIES = ['angola', 'benin', 'burkina_faso', 'cameroon', 'cote_d_ivoire','democratic_republic_of_congo', 'ethiopia', 'ghana', 'guinea', 'kenya','lesotho', 'madagascar', 'malawi', 'mali', 'mozambique', 'nigeria', 'rwanda', 'senegal', 'sierra_leone', 'tanzania', 'togo', 'uganda', 'zambia', 'zimbabwe', 'comores'],


#OOC folds
#A 'ethiopia', 'ghana', 'guinea','mali','senegal',  7115
#B 'burkina_faso','lesotho','madagascar', 'tanzania','zimbabwe' 7185
#C 'angola', 'benin', 'cameroon','malawi', 'zambia' 7057
#D 'democratic_republic_of_congo', 'mozambique', 'nigeria', 'rwanda', 'togo', 7206
#E  'kenya','cote_d_ivoire', 'sierra leone','uganda', 7120



_SURVEY_NAMES_DHS_OOC_A = {
    'train': ['angola', 'benin', 'cameroon','malawi', 'zambia',
             'democratic_republic_of_congo', 'mozambique', 'nigeria', 'rwanda', 'togo',
             'kenya','cote_d_ivoire', 'sierra_leone','uganda','comores'],
    'val': ['burkina_faso','lesotho','madagascar', 'tanzania','zimbabwe'],
    'test': ['ethiopia', 'ghana', 'guinea','mali','senegal'],
}
_SURVEY_NAMES_DHS_OOC_B = {
    'train': ['ethiopia', 'ghana', 'guinea','mali','senegal',
              'democratic_republic_of_congo', 'mozambique', 'nigeria', 'rwanda', 
              'togo','kenya','cote_d_ivoire', 'sierra_leone','uganda'],
    'val': ['angola', 'benin', 'cameroon','malawi', 'zambia','comores'],
    'test': ['burkina_faso','lesotho','madagascar', 'tanzania','zimbabwe'],
}
_SURVEY_NAMES_DHS_OOC_C = {
    'train': ['ethiopia', 'ghana', 'guinea','mali','senegal',
             'burkina_faso','lesotho','madagascar', 'tanzania','zimbabwe',
             'kenya','cote_d_ivoire', 'sierra_leone','uganda'],
    'val': ['democratic_republic_of_congo', 'mozambique', 'nigeria', 'rwanda', 'togo'],
    'test': ['angola', 'benin', 'cameroon','malawi', 'zambia', 'comores'],
}
_SURVEY_NAMES_DHS_OOC_D = {
    'train': ['ethiopia', 'ghana', 'guinea','mali','senegal',
             'burkina_faso','lesotho','madagascar', 'tanzania','zimbabwe',
             'angola', 'benin', 'cameroon','malawi', 'zambia', 'comores'],
    'val': ['kenya','cote_d_ivoire', 'sierra_leone','uganda'],
    'test': ['democratic_republic_of_congo', 'mozambique', 'nigeria', 'rwanda', 'togo'],
}


_SURVEY_NAMES_DHS_OOC_E = {
    'train': ['burkina_faso','lesotho','madagascar', 'tanzania','zimbabwe',
             'angola', 'benin', 'cameroon','malawi', 'zambia',
             'democratic_republic_of_congo', 'mozambique', 'nigeria', 'rwanda', 'togo','comores'],
    'val': ['ethiopia', 'ghana', 'guinea','mali','senegal'],
    'test': ['kenya','cote_d_ivoire', 'sierra_leone','uganda'],

}

SURVEY_NAMES = {  
    'DHS_OOC_A': _SURVEY_NAMES_DHS_OOC_A,
    'DHS_OOC_B': _SURVEY_NAMES_DHS_OOC_B,
    'DHS_OOC_C': _SURVEY_NAMES_DHS_OOC_C,
    'DHS_OOC_D': _SURVEY_NAMES_DHS_OOC_D,
    'DHS_OOC_E': _SURVEY_NAMES_DHS_OOC_E,
    
}

#davidtest= ["comores_2002", "comores_2003", "comores_2004", "comores_2005","comores_2006",
           #"comores_2007", "comores_2008", "comores_2009", "comores_2010","comores_2011",
           #"comores_2012", "comores_2013", "comores_2014", "comores_2015","comores_2016",
           #"comores_2017", "comores_2018", "comores_2019", "comores_2020","comores_2021", 
           #"mozambique_2002", "mozambique_2003", "mozambique_2004", "mozambique_2005","mozambique_2006",
           #"mozambique_2007", "mozambique_2008", "mozambique_2009", "mozambique_2010","mozambique_2011",
           #"mozambique_2012", "mozambique_2013", "mozambique_2014", "mozambique_2015","mozambique_2016",
           #"mozambique_2017", "mozambique_2018", "mozambique_2019", "mozambique_2020","mozambique_2021", "tanzania_2002",                  #"tanzania_2003", "tanzania_2004", "tanzania_2005","tanzania_2006",
           #"tanzania_2007", "tanzania_2008", "tanzania_2009", "tanzania_2010","tanzania_2011",
           #"tanzania_2012", "tanzania_2013", "tanzania_2014", "tanzania_2015","tanzania_2016",
           #"tanzania_2017", "tanzania_2018", "tanzania_2019", "tanzania_2020","tanzania_2021", 
           #"madagascar_2002", "madagascar_2003", "madagascar_2004", "madagascar_2005","madagascar_2006",
           #"madagascar_2007", "madagascar_2008", "madagascar_2009", "madagascar_2010","madagascar_2011",
           #"madagascar_2012", "madagascar_2013", "madagascar_2014", "madagascar_2015","madagascar_2016",
           #"madagascar_2017", "madagascar_2018", "madagascar_2019", "madagascar_2020","madagascar_2021"]

#davidtest= ["Brazil_2000","Brazil_2001","Brazil_2002","Brazil_2003","Brazil_2004","Brazil_2005","Brazil_2006",
           #"Brazil_2007","Brazil_2008","Brazil_2009","Brazil_2010","Brazil_2011","Brazil_2012","Brazil_2013",
           #"Brazil_2014","Brazil_2015","Brazil_2016","Brazil_2017","Brazil_2018","Brazil_2019","Brazil_2020",
           #"Brazil_2021"]
            
            
davidtest= ["Australie_1996","Australie_2001","Australie_2011","Australie_2012","Australie_2016",]



#davidtest= ["comores_1998","comores_1999","comores_2000","comores_2001",
            #"madagascar_1997","madagascar_1998","madagascar_1999","madagascar_2000","madagascar_2001",
            #"mozambique_1997","mozambique_1998","mozambique_1999","mozambique_2000","mozambique_2001",
           #"tanzania_1997","tanzania_1998","tanzania_1999","tanzania_2000","tanzania_2001",]
            
            
 #change all to 36182 because we have deleted comores from the training 36424-242=36182


SIZES = {
    '2009-17': {'train': 24798, 'val': 5057, 'test': 6057, 'all': 36424},    
    'DHS_OOC_A': {'train':22124 , 'val': 7185, 'test': 7115, 'all': 36424},
    'DHS_OOC_B': {'train': 21940, 'val': 7299, 'test': 7185, 'all': 36424},
    'DHS_OOC_C':  {'train':21420 , 'val': 7705, 'test': 7299, 'all': 36424},
    'DHS_OOC_D':  {'train':21599 , 'val': 7120, 'test': 7705, 'all': 36424},
    'DHS_OOC_E': {'train': 22189, 'val': 7115, 'test': 7120, 'all': 36424},
    'DHS_incountry_A': {'train': 21854 , 'val': 7285, 'test': 7285, 'all': 36424},
    'DHS_incountry_B': {'train': 21854, 'val': 7285 , 'test': 7285, 'all': 36424},
    'DHS_incountry_C': {'train': 21854, 'val': 7285, 'test': 7285, 'all': 36424},
    'DHS_incountry_D': {'train': 21855, 'val': 7284, 'test': 7285, 'all': 36424},
    'DHS_incountry_E': {'train': 21855, 'val': 7285, 'test': 7284, 'all': 36424},
    
}

   
    
    
    

URBAN_SIZES = {
    'DHS': {'train': 3954, 'val': 1212, 'test': 1635, 'all': 6801},
    'DHS_OOC_A': {'train': 4264, 'val': 1221, 'test': 1316, 'all': 6801},
    'DHS_OOC_B': {'train': 4225, 'val': 1355, 'test': 1221, 'all': 6801},
    'DHS_OOC_C': {'train': 4010, 'val': 1436, 'test': 1355, 'all': 6801},
    'DHS_OOC_D': {'train': 3892, 'val': 1473, 'test': 1436, 'all': 6801},
    'DHS_OOC_E': {'train': 4012, 'val': 1316, 'test': 1473, 'all': 6801},
}

RURAL_SIZES = {
    'DHS': {'train': 8365, 'val': 2045, 'test': 2458, 'all': 12868},
    'DHS_OOC_A': {'train': 7533, 'val': 2688, 'test': 2647, 'all': 12868},
    'DHS_OOC_B': {'train': 7595, 'val': 2585, 'test': 2688, 'all': 12868},
    'DHS_OOC_C': {'train': 7790, 'val': 2493, 'test': 2585, 'all': 12868},
    'DHS_OOC_D': {'train': 7920, 'val': 2455, 'test': 2493, 'all': 12868},
    'DHS_OOC_E': {'train': 7766, 'val': 2647, 'test': 2455, 'all': 12868},
}

# means and standard deviations calculated over the entire dataset (train + val + test),
# with negative values set to 0, and ignoring any pixel that is 0 across all bands

# means and standard deviations calculated over the entire dataset (train + val + test),
# with negative values set to 0, and ignoring any pixel that is 0 across all bands

_MEANS_DHS = {
    'BLUE':  0.059183,
    'GREEN': 0.088619,
    'RED':   0.104145,
    'SWIR1': 0.246874,
    'SWIR2': 0.168728,
    'TEMP1': 299.078023,
    'NIR':   0.253074,
    'DMSP':  4.005496,
    'VIIRS': 1.096089,
    # 'NIGHTLIGHTS': 5.101585, # nightlights overall
}
_MEANS_DHSNL = {
    'BLUE':  0.063927,
    'GREEN': 0.091981,
    'RED':   0.105234,
    'SWIR1': 0.235316,
    'SWIR2': 0.162268,
    'TEMP1': 298.736746,
    'NIR':   0.245430,
    'DMSP':  7.152961,
    'VIIRS': 2.322687,
}
_MEANS_LSMS = {
    'BLUE':  0.062551,
    'GREEN': 0.090696,
    'RED':   0.105640,
    'SWIR1': 0.242577,
    'SWIR2': 0.165792,
    'TEMP1': 299.495280,
    'NIR':   0.256701,
    'DMSP':  5.105815,
    'VIIRS': 0.557793,
}

_STD_DEVS_DHS = {
    'BLUE':  0.022926,
    'GREEN': 0.031880,
    'RED':   0.051458,
    'SWIR1': 0.088857,
    'SWIR2': 0.083240,
    'TEMP1': 4.300303,
    'NIR':   0.058973,
    'DMSP':  23.038301,
    'VIIRS': 4.786354,
    # 'NIGHTLIGHTS': 23.342916, # nightlights overall
}
_STD_DEVS_DHSNL = {
    'BLUE':  0.023697,
    'GREEN': 0.032474,
    'RED':   0.051421,
    'SWIR1': 0.095830,
    'SWIR2': 0.087522,
    'TEMP1': 6.208949,
    'NIR':   0.071084,
    'DMSP':  29.749457,
    'VIIRS': 14.611589,
}
_STD_DEVS_LSMS = {
    'BLUE':  0.023979,
    'GREEN': 0.032121,
    'RED':   0.051943,
    'SWIR1': 0.088163,
    'SWIR2': 0.083826,
    'TEMP1': 4.678959,
    'NIR':   0.059025,
    'DMSP':  31.688320,
    'VIIRS': 6.421816,
}

MEANS_DICT = {
    'DHS': _MEANS_DHS,
    'DHSNL': _MEANS_DHSNL,
    'LSMS': _MEANS_LSMS,
}

STD_DEVS_DICT = {
    'DHS': _STD_DEVS_DHS,
    'DHSNL': _STD_DEVS_DHSNL,
    'LSMS': _STD_DEVS_LSMS,
}
















