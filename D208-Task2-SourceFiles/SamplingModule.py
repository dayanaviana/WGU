#pip install -U scikit-learn

class Sampling:
    '''
        Sampling data
    '''
    
    def __init__(self):
        print('\nSampling init')

    @staticmethod
    def ramdom_sampling(df):
        '''
            Syntax: DataFrame.sample(n=None, frac=None, replace=False, weights=None, random_state=None, axis=None)
            Parameters:
            n: int value, Number of random rows to generate.
            frac: Float value, Returns (float value * length of data frame values ). frac cannot be used with n.
            replace: Boolean value, return sample with replacement if True.
            random_state: int value or numpy.random.RandomState, optional. if set to a particular integer, will return same rows as sample in every iteration.
            axis: 0 or ‘row’ for Rows and 1 or ‘column’ for Columns.
        '''
        rows = round(df.size * 0.75)
        sample_data = df.sample(n=rows, random_state=42)
        return sample_data

    @staticmethod
    def stratified_sampling(df, target: str, stratif_by: str):
        ''' Return (x_train, x_test, y_train, y_test)'''
        y = df[target]
        x_predictors = df.drop(target, axis=1)
        split_by = df[stratif_by]
        from sklearn.model_selection import train_test_split
        x_train, x_test, y_train, y_test = train_test_split(x_predictors, y, test_size=0.3, random_state=42, stratify=split_by)
        print('x_train:', x_train.shape)
        print('y_train:', y_train.shape)
        print('x_test:', x_test.shape)
        print('y_test:', y_test.shape)
        return x_train, x_test, y_train, y_test
    
    @staticmethod
    def split_sampling(df, target: str):
        ''' Return (x_train, x_test, y_train, y_test)'''
        y = df[target]
        x_predictors = df.drop(target, axis=1)
        from sklearn.model_selection import train_test_split
        x_train, x_test, y_train, y_test = train_test_split(x_predictors, y, test_size=0.3, random_state=42)
        print('x_train:', x_train.shape)
        print('y_train:', y_train.shape)
        print('x_test:', x_test.shape)
        print('y_test:', y_test.shape)
        return x_train, x_test, y_train, y_test