import matplotlib.pyplot as plt 

class Scatterplot:
    '''
        Scatterplot graph
    '''
    
    def __init__(self):
        print('Scatterplot init')
    
    def show_graph(self, df, column_name_x, column_name_y):
        # Scatter plot
        # Plot size: 1000px x 600px
        plt.subplots(figsize=(10, 6))
        plt.scatter(df[column_name_x], df[column_name_y])
        # Put the x-axis on a logarithmic scale
        # plt.xscale('log')
        #A correlation will become clear when you display the x-axis on a logarithmic scale.
        # plt.xscale('log')
        # Show plot
        plt.title(column_name_x + ' VS ' + column_name_y)
        plt.xlabel(column_name_x)
        plt.ylabel(column_name_y)
        plt.grid()
        plt.show()
        plt.clf() #clear current figure