DHS_COUNTRIES = ['angola', 'benin', 'burkina_faso', 'cameroon', 'cote_d_ivoire','democratic_republic_of_congo', 'ethiopia', 'ghana', 'guinea', 'kenya','lesotho', 'madagascar', 'malawi', 'mali', 'mozambique', 'nigeria', 'rwanda', 'senegal', 'sierra_leone', 'tanzania', 'togo', 'uganda', 'zambia', 'zimbabwe'],


#OOC folds
#A 'cameroon', 'ethiopia', 'ghana', 'guinea','senegal','togo',  7252
#B 'burkina_faso','lesotho','madagascar', 'tanzania','zimbabwe', 7112
#C 'angola', 'benin', 'mali','malawi', 'zambia', 7291
#D 'democratic_republic_of_congo', 'mozambique', 'nigeria', 'rwanda', 7206
#E  'kenya','cote_d_ivoire', 'sierra leone','uganda', 7067




_SURVEY_NAMES_DHS_OOC_A = {
    'train': ['angola', 'benin', 'mali','malawi', 'zambia', 'democratic_republic_of_congo', 'mozambique', 'nigeria', 'rwanda',
             'kenya','cote_d_ivoire', 'sierra_leone','uganda'],
    'val': ['burkina_faso','lesotho','madagascar', 'tanzania','zimbabwe'],
    'test': ['cameroon', 'ethiopia', 'ghana', 'guinea','senegal','togo'],
}
_SURVEY_NAMES_DHS_OOC_B = {
    'train': ['cameroon', 'ethiopia', 'ghana', 'guinea','senegal','togo','democratic_republic_of_congo', 'mozambique', 'nigeria', 'rwanda', 'kenya','cote_d_ivoire', 'sierra_leone','uganda'],
    'val': ['angola', 'benin', 'mali','malawi', 'zambia'],
    'test': ['burkina_faso','lesotho','madagascar', 'tanzania','zimbabwe'],
}
_SURVEY_NAMES_DHS_OOC_C = {
    'train': ['cameroon', 'ethiopia', 'ghana', 'guinea','senegal','togo', 'burkina_faso','lesotho','madagascar', 'tanzania','zimbabwe', 'kenya','cote_d_ivoire', 'sierra_leone','uganda'],
    'val': ['democratic_republic_of_congo', 'mozambique', 'nigeria', 'rwanda'],
    'test': ['angola', 'benin', 'mali','malawi', 'zambia'],
} 
_SURVEY_NAMES_DHS_OOC_D = {
    'train': ['cameroon', 'ethiopia', 'ghana', 'guinea','senegal','togo', 'burkina_faso','lesotho','madagascar', 'tanzania','zimbabwe', 'angola', 'benin', 'mali','malawi', 'zambia'],
    'val': ['kenya','cote_d_ivoire', 'sierra_leone','uganda'],
    'test': ['democratic_republic_of_congo', 'mozambique', 'nigeria', 'rwanda'],
}


_SURVEY_NAMES_DHS_OOC_E = {
    'train': ['burkina_faso','lesotho','madagascar', 'tanzania','zimbabwe', 'angola', 'benin', 'mali','malawi', 'zambia',
             'democratic_republic_of_congo', 'mozambique', 'nigeria', 'rwanda'],
    'val': ['cameroon', 'ethiopia', 'ghana', 'guinea','senegal','togo'],
    'test': ['kenya','cote_d_ivoire', 'sierra_leone','uganda'],
}

SURVEY_NAMES = {  
    'DHS_OOC_A': _SURVEY_NAMES_DHS_OOC_A,
    'DHS_OOC_B': _SURVEY_NAMES_DHS_OOC_B,
    'DHS_OOC_C': _SURVEY_NAMES_DHS_OOC_C,
    'DHS_OOC_D': _SURVEY_NAMES_DHS_OOC_D,
    'DHS_OOC_E': _SURVEY_NAMES_DHS_OOC_E,
    
}

davidtest=["Tanzania_1996", "Tanzania_1999","Tanzania_2001",]

#davidtest=["Madagascar_2012","Madagascar_2015","Madagascar_2020",
           #"Mozambique_2012","Mozambique_2015","Mozambique_2020",                                   #"Tanzania_2012","Tanzania_2015","Tanzania_2020",]
    
SIZES = {
    'DHS_OOC_A': {'train':21564, 'val':7112 , 'test':7252 , 'all': 35928},
    'DHS_OOC_B': {'train':21525, 'val':7291 , 'test':7112 , 'all': 35928},
    'DHS_OOC_C': {'train':21431, 'val':7206 , 'test':7291 , 'all': 35928},
    'DHS_OOC_D': {'train':21655, 'val':7067 , 'test':7206 , 'all': 35928},
    'DHS_OOC_E': {'train':21609, 'val':7252 , 'test':7067 , 'all': 35928},
    'DHS_incountry_A': {'train':21556  , 'val':7186 , 'test':7186 , 'all': 35928},
    'DHS_incountry_B':{'train':21556 , 'val':7186  , 'test':7186 , 'all': 35928},
    'DHS_incountry_C': {'train':21557 , 'val':7185 , 'test':7186 , 'all': 35928},
    'DHS_incountry_D': {'train':21558 , 'val':7185 , 'test':7185 , 'all': 35928},
    'DHS_incountry_E': {'train':21557 , 'val':7186 , 'test':7185 , 'all': 35928},
    
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
















