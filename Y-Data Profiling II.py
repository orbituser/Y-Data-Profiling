# -*- coding: utf-8 -*-
"""
Created on Mon Dec 18 01:55:02 2023

@author: mozea
"""

import pandas as pd
from ydata_profiling import ProfileReport


#DATA EXPLORATION WITH PANDAS
dataset = pd.read_csv('Tunisair_flights_dataset.csv')
dataset.info()
data_head = dataset.head()
data_null_count = dataset.isnull().sum()
data_descriptive_statistic = dataset.describe()


#DATA EXPLORATION WITH Y-DATA PROFILING
Flights_data = pd.read_csv('Tunisair_flights_dataset.csv')

# Generate the profile report
profile = ProfileReport(Flights_data, title='Tunisair flights Report')

# Generating an HTML report to view it
profile.to_file("Tunisair flights Report.html")