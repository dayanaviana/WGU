import pandas as pd
import numpy as np
from scipy import stats

class SummaryStatistics:
    '''
        Summary Statistics
    '''
    
    def __init__(self):
        print('\nSummary Statistics init')
    
    def get_series_summary(self, series):
        max = np.max(series)
        print("Max:", max)
        min = np.min(series)
        print("Min:", min)
        mean = "{:.2f}".format(np.mean(series))
        print("Mean:", mean)
        median =  "{:.2f}".format(np.median(series))
        print("Median:", median)

        # Python 3.8
        # import statistics
        # mode =  statistics.multimode(df[column_name])
        mode =  stats.mode(series)
        print("Mode:", mode[0])
        var =  "{:.2f}".format(np.var(series))
        print("Variance:", var)
        stddev =  "{:.2f}".format(np.std(series))
        print("St. Dev:", stddev)
    
    
    def get_df_summary(self, df, column_name):
        print(column_name)
        series = df[column_name]
        self.get_series_summary(series)
        