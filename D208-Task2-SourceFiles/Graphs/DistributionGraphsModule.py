
import matplotlib.pyplot as plt 

class DistributionGraphs:
    '''
        Histogram & BoxPlot graph
    '''
    
    def __init__(self):
        print('\nDistribution Graphs init')

    
    def show_2x3_graphs(self, df1, df2, df3, column_name):
        print("\n")

        # Histogram and show plot 
        # Plot size: 1900px x 800px
        plt.subplots(figsize=(19, 8))
        # configure supplot(nrows,ncols,nsubplots) 
        plt.subplot(2,3,1) 
        plt.hist(df1[column_name]) 
        plt.grid(True)
        plt.title(column_name)
        plt.subplot(2,3,2) 
        plt.hist(df2[column_name]) 
        plt.grid(True)
        plt.title("Churn=YES")
        plt.subplot(2,3,3) 
        plt.hist(df3[column_name]) 
        plt.grid(True)
        plt.title("Churn=NO")
        # Boxplots
        plt.subplot(2,3,4) 
        plt.boxplot(df1[column_name])
        plt.grid(True)
        plt.subplot(2,3,5) 
        plt.boxplot(df2[column_name])
        plt.grid(True)
        plt.subplot(2,3,6) 
        plt.boxplot(df3[column_name])
        plt.grid(True)
        plt.show() 