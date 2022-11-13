import pandas as pd

class Cleaning:
    '''
        Treating dataset
    '''
    
    def __init__(self, df):
        self._df = df
        print('\nCleaning init')
    
    def remove_columns(self, listOfColumns):
        ''' axis = 1 -> columns '''
        self._df = self._df.drop(listOfColumns, axis=1)
        print('Columns Removed.')
        self._show_info()
        
    def remove_lines(self, listOfLines):
        ''' axis = 0 -> lines '''
        self._df = self._df.drop(listOfLines, axis=0)
        print('Rows Removed.')

    # df_test.fillna(df_test.mean())

    def fix_column_type_to_numeric(self, column_name: str):
        '''Valores que estão reconhecidos de forma errada '''
        self._df[column_name] = pd.to_numeric(self._df[column_name], errors="coerce")

    def delete_empty_columns(self):
        ''' Delete column if all values are null
        axis = 1 -> columns '''
        self._df = self._df.dropna(how="all", axis=1)

    def delete_empty_lines(self):
        ''' Delete line if any column is null
        axis = 0 -> lines '''
        self._df = self._df.dropna(how="any", axis=0)

    def _show_columns_list(self):
            print(self._df.columns.tolist())
            
    def _show_info(self):
        self._show_columns_list()
        # print(self._df.info())
        import io
        buffer = io.StringIO()
        self._df.info(buf=buffer)
        s = buffer.getvalue()
        with open("df_info.txt", "w",
                encoding="utf-8") as f:  
            f.write(s)
        # print('\nDF first line\n')
        # print(self._df.iloc[0])
        print('\nComplete details in df_info.txt file')

        
