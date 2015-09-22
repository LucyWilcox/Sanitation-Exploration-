import RAD_Sanitation as RADS
import pickle
import matplotlib.pyplot as plt
import pprint

#[(Country, indicator, [values],[years]), (Country, indicator, [values],[years]),...]

##Load data from Pickle files of segmented data:
impSanitation = pickle.load( open( "dataPickles/ImprovedSan.p", "rb" ) )
contraceptPrev = pickle.load( open( "dataPickles/contraceptivePrevalance.p", "rb" ) )
impWaterSrc = pickle.load( open( "dataPickles/improvedWaterSource.p", "rb" ) )
progSecndrySclFemale = pickle.load( open( "dataPickles/progSecondarySchoolFemale.p", "rb" ) )

##Declare list of countries we want to plot data for:
country_list = ['Angola', 'Chad', 'Sudan']

sanList = RADS.ourCountries(impSanitation,country_list)
contaceptList = RADS.ourCountries(contraceptPrev,country_list)
impWaterList = RADS.ourCountries(impWaterSrc,country_list)
prog2ndSclFmlList = RADS.ourCountries(progSecndrySclFemale,country_list)

# RADS.yearCorrelate(prog2ndSclFmlList[1], impSanitation[1])

plt.plot(prog2ndSclFmlList[1][3],prog2ndSclFmlList[1][2], linewidth=8)
plt.show()