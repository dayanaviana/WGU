import io
from matplotlib import pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd
from scipy.stats import norm

class MyPyUtils:

    @staticmethod 
    def writeDFToFile(df, fileName):
        buffer = io.StringIO()
        df.info(buf=buffer)
        s = buffer.getvalue()
        with open(fileName, "w", encoding="utf-8") as f:  
            f.write(s)
        print('\nComplete details in '+fileName+' file')
    
    @staticmethod
    def changeDtypesToCategorical(df, listOfColumnNames):
        for column_name in listOfColumnNames:
            df[column_name] = df[column_name].astype('object')
        return df

    # Confusion Matrix function
    @staticmethod
    def plot_confusion_matrix_normalized(cm, model=None, title='Confusion matrix'):
        cm_norm = cm / cm.sum(axis=1).reshape(-1,1)
        """Plots a confusion matrix."""
        if classes is not None:
            classes = model.classes_
            sns.heatmap(cm_norm, cmap="YlGnBu", xticklabels=classes, yticklabels=classes, vmin=0., vmax=1., annot=True, annot_kws={'size':20})
        else:
            sns.heatmap(cm_norm, vmin=0., vmax=1.)
        plt.title(title)
        plt.ylabel('True label')
        plt.xlabel('Predicted label')
        plt.show()
    
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

    @staticmethod
    def plot_roc_curve(logreg, X_test, y_test):
        from sklearn.metrics import roc_curve
        y_pred_prob = logreg.predict_proba(X_test)[:,1]
        fpr, tpr, theresholds = roc_curve(y_test, y_pred_prob)
        plt.plot([0,1],[0,1],'k--')
        plt.plot(fpr, tpr, label='Logistic Regression')
        plt.xlabel('False Positive Rate')
        plt.ylabel('True Positive Rate')
        plt.title('Logistic Regression ROC Curve')
        plt.show()

    @staticmethod
    def plot_confusion_matrix(cnf_matrix):
        class_names=[0,1] # name  of classes
        fig, ax = plt.subplots()
        tick_marks = np.arange(len(class_names))
        plt.xticks(tick_marks, class_names)
        plt.yticks(tick_marks, class_names)
        # create heatmap
        sns.heatmap(pd.DataFrame(cnf_matrix), annot=True, cmap="YlGnBu" ,fmt='g')
        ax.xaxis.set_label_position("top")
        plt.tight_layout()
        plt.title('Confusion matrix', y=1.1)
        plt.ylabel('Actual label')
        plt.xlabel('Predicted label') 
        plt.show()