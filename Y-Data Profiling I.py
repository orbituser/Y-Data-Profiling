# -*- coding: utf-8 -*-
"""
Created on Mon Dec 18 01:22:52 2023

@author: mozea
"""

import pandas as pd
from ydata_profiling import ProfileReport


#DATA EXPLORATION WITH PANDAS
dataset = pd.read_csv('EDUCATION_ATTAINMENT.csv')
dataset.info()
data_descriptive_statistic = dataset.describe()


#DATA EXPLORATION WITH Y-DATA PROFILING
Education_data = pd.read_csv('EDUCATION_ATTAINMENT.csv')

# Generate the profile report
profile = ProfileReport(Education_data, title='Education Attainment Report')

# Generating an HTML report to view it
profile.to_file("Education Attainment Report.html")