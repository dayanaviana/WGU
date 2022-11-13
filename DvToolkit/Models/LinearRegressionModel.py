## ! pip install statsmodels
## pip install statsmodels --upgrade

# Ordinary Least Squares (OLS) 
from statsmodels.formula.api import ols
import numpy as np
import matplotlib.pyplot as plt

class LinearRegression:
    '''
        Machine Learning: Computer learning without being programmed
            Supervised Leaning: Train model, and test in unseen data
                Regression: Predict results based on a linear trend
    '''
    
    def __init__(self):
        _model = None
        _train_df = None
        print('\nLinearRegression init')

    @staticmethod
    def lasso_for_feature(x, y, candidates_columns):
        from sklearn.linear_model import Lasso
        lasso = Lasso(alpha=0.1)
        lasso_coef = lasso.fit(x, y).coef_
        _ = plt.figure(figsize=(20,8))
        _ = plt.plot(range(len(candidates_columns)), lasso_coef)
        _ = plt.xticks(range(len(candidates_columns)), candidates_columns, rotation=90)
        _ = plt.ylabel('Coefficients')
        plt.grid()
        plt.show()


    def multiple_linear_regression_by_formula(self, formula: str, train_df):
        #formula =  "MonthlyCharge ~ Outage_sec_perweek + Yearly_equip_failure + 0"
        print("\nformula = ", formula)
        self._train_df = train_df
        self._model = ols(formula, data=train_df).fit()
        self.__print_model_results()

    def multiple_linear_regression(self, target: str, numeric_columns, train_df):
        formula = self.__get_formula(numeric_columns, target)
        print("\nformula = ", formula)
        self._train_df = train_df
        self._model = ols(formula, data=train_df).fit()
        self.__print_model_results()

    def __get_formula(self, numeric_columns, target: str):
        x_predictors = "" # explanatory variables
        for column_name in numeric_columns:
            x_predictors += column_name + " + "
        x_predictors = x_predictors[:-3] 

        #Generating a linear regression formula
        # y = intercept + slope * x
        formula = target + " ~ " + x_predictors + " + 0" # +0 does not include a global interceptor
        return formula

    def __print_model_results(self):
        # print("\nModel= \n", self._model.params)
        # intercept, slope = model.params

        # Coefficient of deternination: 
        # How well the linear regression line fits the observed values [0-1] (larger is better)
        print("\nR-squared = ", self._model.rsquared)

        # Adjusted coefficient of determination
        # Adds penalty when more predictors are added
        print("R-squared adjusted = ", self._model.rsquared_adj)

        # Mean squared error MSE = RSE^2
        mse = self._model.mse_resid
        print("MSE = ", mse)

        # Residual standard error:
        # The tipical sie of the residuals (smaller is better)
        sum_residuals_sq = sum(self._model.resid**2)#model.resid**2
        df = len(self._train_df)-2
        print("RSE = ", sum_residuals_sq/df)#sum of residuals squared
        print("MRSE = ", np.sqrt(sum_residuals_sq/len(self._train_df)))

        print("RSE = ", np.sqrt(mse))
        # We typically get the X wrong by about RSE_number     

            

        with open('model_summary.txt', 'w') as fh:
            fh.write(self._model.summary().as_text())     
        print("\nModel summary saved on model_summary.txt")  