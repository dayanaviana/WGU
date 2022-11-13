import pandas as pd

class Importing:
    
    def __init__(self):
        print('Importing init')
        
    @staticmethod
    def import_from_google(docId):
        #churn_clean_altered.csv
        # docId= "1-WjyGAwXhgkEMSGk1PHKMjIASkVgn-YO"
        googleDriveFile = "https://docs.google.com/uc?id="+docId+"&export=download"
        # import into data frame
        df = pd.read_csv(googleDriveFile, index_col=0)
        return df

    def _show_columns_list(self, df):
        print(df.columns.tolist())

    def _get_columns_list(self, df):
        return df.columns.tolist()
    
    def import_from_url(self, url):
        # import into data frame
        df = pd.read_csv(url, index_col=0)
        print('Imported')
        self._show_columns_list(df)
        return df

    def get_categorical_columns_list(self, df):
        df = df.select_dtypes(include='object')
        print('\nCategorical Columns')
        self._show_columns_list(df)
        return self._get_columns_list(df)

    def get_numerical_columns_list(self, df):
        df = df.select_dtypes(include=['int64','float64','uint8'])
        print('\nNumerical Columns')
        self._show_columns_list(df)
        return self._get_columns_list(df)

    @staticmethod
    def filter_df_by_columns(df, columns_list):
        #Select columns
        df_filtered = df.loc[:, columns_list]
        return df_filtered

