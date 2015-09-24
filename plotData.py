import RAD_Sanitation as RADS
import pickle
import matplotlib.pyplot as plt
import pprint
import numpy as np

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


def crossCorrelateValuesForPlotting(data1, data2, countryIndex):
	d1,d2,years = RADS.yearCorrelate(data1[countryIndex], data2[countryIndex])

	plt.plot(d1,d2, '*', markersize=20)

	d1 = np.array(d1); d2=np.array(d2)
	m,b = np.polyfit(d1, d2, 1)
	return d1, d2, m, b

d1, d2, m, b = crossCorrelateValuesForPlotting(prog2ndSclFmlList, impSanitation, 0)
plt.plot(d1,m*d1+b, linewidth=8)
plt.xlabel('Female Progression to Secondary School (%)', fontsize=18)
plt.ylabel('Number of Improved Sanitation Facilities', fontsize=18)
plt.title('Effect of Improved Sanitation Facilities \n on Female Secondary Schoole Enrollment in Chad', fontsize=20)

# plt.plot(prog2ndSclFmlList[1][3],prog2ndSclFmlList[1][2], linewidth=8)
plt.show()