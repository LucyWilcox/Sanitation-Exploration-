import RAD_Sanitation as RADS
import countryList as RADCL
import pickle
import matplotlib.pyplot as plt
import pprint
import numpy as np
import matplotlib.pyplot  as pyplot
import pylab
import scipy.stats

#[(Country, indicator, [values],[years]), (Country, indicator, [values],[years]),...]

##Load data from Pickle files of segmented data:
impSanitation = pickle.load( open( "dataPickles/ImprovedSan.p", "rb" ) )
contraceptPrev = pickle.load( open( "dataPickles/contraceptivePrevalance.p", "rb" ) )
impWaterSrc = pickle.load( open( "dataPickles/improvedWaterSource.p", "rb" ) )
progSecndrySclFemale = pickle.load( open( "dataPickles/progSecondarySchoolFemale.p", "rb" ) )


country_list = RADCL.countryList()

sanList = RADS.ourCountries(impSanitation,country_list)
contaceptList = RADS.ourCountries(contraceptPrev,country_list)
impWaterList = RADS.ourCountries(impWaterSrc,country_list)
prog2ndSclFmlList = RADS.ourCountries(progSecndrySclFemale,country_list)


def crossCorrelateValuesForPlotting(data1, data2, countryIndex):
	print  '\n data 1 = '
	print 'len data 1',len(data2[countryIndex])
	pprint.pprint( data1[countryIndex])
	print 'data 2 = '

	pprint.pprint(data2[countryIndex])
	d1,d2,years = RADS.yearCorrelate(data1[countryIndex], data2[countryIndex])

	

	d1 = np.array(d1); d2=np.array(d2)
	if (len(d1)>0) and (len(d2)>0):
		m,b = np.polyfit(d1, d2, 1)
		return d1, d2, m, b
	else:
		print 'Country ', countryIndex, ' has no data for given indicator.'
		return d1, d2, False, False


d1_all = []; d2_all = []
for country_index, country_name in enumerate(country_list):
	print country_name, '  ', country_index
	d1, d2, m, b = crossCorrelateValuesForPlotting(impSanitation,prog2ndSclFmlList, country_index)
	print d1, d2, m, b
	print len(d1)
	if  (len(d1)>0):
		# line, = ax.plot(d1, d2, marker = 'o', color='blue', lw=2) #plt.plot(d1,d2, '*', markersize=20, label = country_name)
		d1_all.append(d1); d2_all.append(d2)
	# if (m != False):
		# plt.plot(d1,m*d1+b, linewidth=8)

d1_log = []
for array in d1_all:
	for nested_value in array:
		d1_log.append(np.log10(nested_value))
d2_log = []	
for array in d2_all:
	for nested_value in array:
		d2_log.append(np.log10(nested_value))
d1_log = np.array(d1_log)
d2_log = np.array(d2_log)


# line, = ax.plot(d1, m*d1+b, marker = 'o', color='red', lw=8)#plt.plot(d1,m*d1+b, linewidth=8)
m, b, r_value, p_value, std_err = scipy.stats.linregress(d1_log, d2_log)
plt.plot(d1_log,d2_log, 'o', markersize=10)
plt.plot(d1_log, m*d1_log+b, linewidth=5)
print 'r squared: ', r_value**2
print 'p val: ', p_value
print 'standard error: ', std_err


plt.ylabel('Female Progression to Secondary School (log base 10 of %)', fontsize=18)
plt.xlabel('Number of Improved Sanitation Facilities (log base 10)', fontsize=18)
plt.title('Effect of Improved Sanitation Facilities \n on Female Secondary Schoole Enrollment', fontsize=20)
plt.text(8.3,1.5, '$R^2$ value of: '+str(r_value**2) + '\n $P$ value of: '+str(p_value), fontsize=18)
# #plt.legend()

# # plt.plot(prog2ndSclFmlList[1][3],prog2ndSclFmlList[1][2], linewidth=8)

plt.show()