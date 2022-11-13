import pandas as pd

class Transforming:
    '''
        Transforming data
    '''
    
    def __init__(self, df):
        self._df = df
        print('\nTransforming init')

    def categorical_columns_to_dummy(self, categorical_columns_list):
        #Select columns
        df_filtered = self._df.loc[:, categorical_columns_list]
        # X = df[['Gender','Marital']]
        df_dummies = pd.get_dummies(data=df_filtered, drop_first=True).rename(columns=lambda x:x.replace(" ", "_").replace("(","").replace(")",""))
        print('\nGot Dummy variables')
        self.__show_columns_list(df_dummies)
        print(df_dummies.head())
        self._df = self._df.join(df_dummies)
        self.__show_info()

    def __show_columns_list(self, df):
            print(df.columns.tolist())
            
    def __show_info(self):
        import io
        buffer = io.StringIO()
        self._df.info(buf=buffer)
        s = buffer.getvalue()
        with open("df_with_dummies.txt", "w",
                encoding="utf-8") as f:  
            f.write(s)
        # print('\nDF first line\n')
        # print(self._df.iloc[0])
        print('\nComplete details in df_with_dummies.txt file')

    def delete_column(self, column_name):
        self.df.drop(['column_name'], axis=1)
        print('\nColumn deleted', column_name)