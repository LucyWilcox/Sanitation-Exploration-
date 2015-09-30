import RAD_Sanitation as RADS
import countryList as RADCL
import pickle
import matplotlib.pyplot as plt
import pprint
import numpy as np
import matplotlib.pyplot  as pyplot
import pylab
import scipy.stats


little_plots = True #Plot the little plots of the scatter data with different time offsets

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


def crossCorrelateValuesForPlotting(data1, data2, countryIndex, yearOffset):
	#pprint.pprint(data2[countryIndex])
	d1,d2,years = RADS.yearCorrelate(data1[countryIndex], data2[countryIndex], yearOffset = yearOffset)

	d1 = np.array(d1); d2=np.array(d2)
	if (len(d1)>1) and (len(d2)>1):
		m,b = np.polyfit(d1, d2, 1)
		return d1, d2, m, b
	else:
		#print 'Country ', countryIndex, ' has no data for given indicator.'
		return d1, d2, False, False


rsquaredCumulative = []; pvalCumulative = []; stderrorCumulative = []; yearOffsetCumulative = []; mCumulative = []
for yearOffset in range(-5,7):
	print '\n Year offset is: ', yearOffset
	d1_all = []; d2_all = []
	for country_index, country_name in enumerate(country_list):
		d1, d2, m, b = crossCorrelateValuesForPlotting(impWaterSrc, prog2ndSclFmlList, country_index, yearOffset)
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
	if little_plots==True:
		plt.plot(d1_log,d2_log, 'o', markersize=13, alpha=.5)
		plt.plot(d1_log, m*d1_log+b, linewidth=5)
	print 'r squared: ', r_value**2
	print 'p val: ', p_value
	print 'standard error: ', std_err
	rsquaredCumulative.append(10*r_value**2); 
	pvalCumulative.append(p_value); 
	stderrorCumulative.append(50*std_err); 
	yearOffsetCumulative.append(yearOffset);
	mCumulative.append(m)

	if little_plots == True:
		plt.ylabel('Female Progression to Secondary School (log base 10 of %)', fontsize=18)
		plt.xlabel('Number of Improved Sanitation Facilities (log base 10)', fontsize=18)
		plt.title('Effect of Improved Sanitation Facilities \n on Female Secondary Schoole Enrollment', fontsize=20)
		plt.text(8.3,1.5, '$R^2$ value of: '+str(r_value**2) + '\n $P$ value of: '+str(p_value), fontsize=18)
		# #plt.legend()

		# # plt.plot(prog2ndSclFmlList[1][3],prog2ndSclFmlList[1][2], linewidth=8)

		plt.show()

# plt.clear()
print 'min r^2 error is: ', min(rsquaredCumulative), ' and occurs at index: ', yearOffsetCumulative[rsquaredCumulative.index(min(rsquaredCumulative))]
print pvalCumulative
print stderrorCumulative

plt.plot(yearOffsetCumulative, rsquaredCumulative, linewidth=8, label='$R^2  (x10)$')
plt.plot(yearOffsetCumulative, pvalCumulative, linewidth=8, label='p value')
plt.plot(yearOffsetCumulative, stderrorCumulative, linewidth=8, label='standard error ($x50$)')
plt.title('Error From OLS Fitting With Variable Time Offset \n for % Female Secondary School Enrollment and Number Improved Sanitation Facilities', fontsize=24)
plt.xlabel('Year Offset (years)', fontsize=18)
plt.ylabel('Error Value', fontsize=18)
plt.legend(fontsize=16)
plt.show()

plt.plot(yearOffsetCumulative,mCumulative, linewidth=8, label='slope')
plt.show()