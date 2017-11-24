#!/usr/bin/env python3

import numpy as np
import scipy.stats as stats
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from pprint import  pprint

# this line tells jupyter notebook to put the plots in the notebook rather than saving them to file.
#%matplotlib inline

# this line makes plots prettier on mac retina screens. If you don't have one it shouldn't do anything.
#%config InlineBackend.figure_format = 'retina'

df_sat = pd.read_csv('sat_scores.csv')

# Outliers are an interesting problem in statistics, in that there is not an agreed upon best way to define them. Subjectivity in selecting and analyzing data is a problem that will recur throughout the course.

# Pull out the rate variable from the SAT dataset.
outliers = df_sat.copy()
outliers.drop('Rate', inplace=True, axis=1)

# Get Regression line
plt.clf()
slope, intercept, r_value, p_value, std_err = stats.linregress(outliers['Verbal'],outliers['Math'])

x = np.linspace(450, 620, 200)
y = slope*x + intercept

ax = outliers.plot(x='Verbal', kind='hist')
#ax.plot(x,y,'r')
#ax.set_ylim(450, 620)
#ax.set_xlim(475, 600)

plt.show()



# Are there outliers in the dataset? Define, in words, how you numerically define outliers.
# Print out the outliers in the dataset.
# Remove the outliers from the dataset.
# Compare the mean, median, and standard deviation of the "cleaned" data without outliers to the original. What is different about them and why?

