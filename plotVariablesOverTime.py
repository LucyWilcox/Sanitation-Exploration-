import RAD_Sanitation as RADS
import countryList as RADCL
import pickle
import matplotlib.pyplot as plt
import pprint
import numpy as np
import matplotlib.pyplot  as pyplot
import pylab
import scipy.stats

plt.rcParams["figure.figsize"] =[12,12]

data_values = {'% Gross Female Secondary School Enrollment': "dataPickles/grossSecondarySchoolEnrolment.p",
	'Improved Water Source (% access)':"dataPickles/improvedWaterSource.p",
	'Improved Sanitation Facilities (% access)':"dataPickles/ImprovedSan.p",
	'% Access to Contraceptives': "dataPickles/contraceptivePrevalance.p"
}


little_plots = True # :Plot the little plots of the scatter data with different time offsets
axies_scale = 'linear' # :Plot nad compute the values with log/log axies. Options include: 'log_log'

variable_name_plot_dependent = 'Improved Water Source (% access)'#'Improved Sanitation Facilities (% access)'#
variable_name_plot_independent = '% Gross Female Secondary School Enrollment'

#[(Country, indicator, [values],[years]), (Country, indicator, [values],[years]),...]


dependent = pickle.load( open( data_values[variable_name_plot_dependent], "rb" ) )
independent = pickle.load( open( data_values[variable_name_plot_independent], "rb" ) )


country_list = RADCL.countryList()

dependent = RADS.ourCountries(dependent, country_list)
independent = RADS.ourCountries(independent, country_list)



def crossCorrelateValuesForPlotting(data1, data2, countryIndex, yearOffset=0):
	#pprint.pprint(data2[countryIndex])
	d1,d2,years = RADS.yearCorrelate(data1[countryIndex], data2[countryIndex], yearOffset = yearOffset)

	d1 = np.array(d1); d2=np.array(d2)
	if (len(d1)>1) and (len(d2)>1):
		return d1, d2
	else:
		#print 'Country ', countryIndex, ' has no data for given indicator.'
		return d1, d2



d1_all = []; d2_all = []
for country_index, country_name in enumerate(country_list):
	d1, d2 = crossCorrelateValuesForPlotting(dependent, independent, country_index)
	if  (len(d1)>0):
		d1_all.append(d1); d2_all.append(d2)


d1_log = []
d2_log = []	

d1_values = []
d2_vlaues = []

for array in d1_all:
	for nested_value in array:
		d1_log.append(np.log10(nested_value))
		d1_values.append(nested_value)

for array in d2_all:
	for nested_value in array:
		d2_log.append(np.log10(nested_value))
		d2_vlaues.append(nested_value)

# pprint.pprint(d2_log)
d1_log = np.array(d1_log)
d2_log = np.array(d2_log)
d1_values = np.array(d1_values)
d2_vlaues = np.array(d2_vlaues)


# line, = ax.plot(d1, m*d1+b, marker = 'o', color='red', lw=8)#plt.plot(d1,m*d1+b, linewidth=8)
if axies_scale=='log_log':
	x = d1_log
	y = d2_log
if axies_scale=='linear':
	x=d1_values
	y=d2_vlaues
m, b, r_value, p_value, std_err = scipy.stats.linregress(x, y)
pearsonCorrelation = scipy.stats.pearsonr(x, y)	
print 'r squared: ', r_value**2
print 'p val: ', p_value
print 'standard error: ', std_err
print 'line slope: ', m
print 'line intercept: ', b
print 'Pearson correlation: ', pearsonCorrelation
print '\n'


plt.clf()
plt.plot(x, y, 'o', markersize=13, alpha=.5)
plt.plot(x, m*x+b, linewidth=5)
# plt.show()
plt.ylabel(variable_name_plot_independent, fontsize=18)
plt.xlabel(variable_name_plot_dependent, fontsize=18)
plt.suptitle('Effect of '+variable_name_plot_dependent+' \n on '+variable_name_plot_independent, fontsize=20)
subtitle = '$R^2$ value of: '+str(r_value**2) + ', $P$ value of: '+str(p_value)
plt.title(subtitle, fontsize=13) ##TODO: Fix text so it shows up all the time!!!
# plt.legend()
# plt.plot(independent[1][3],independent[1][2], linewidth=8)

plt.show()
#plt.savefig(variable_name_plot_dependent+'_offsetScatterPlot_offsetOf'+str(yearOffset)+'.png', papertype='letter')
		
	
