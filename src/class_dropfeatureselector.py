from sklearn.base import BaseEstimator, TransformerMixin
import pandas as pd

class DropFeatureSelector(BaseEstimator, TransformerMixin):
    # def __init__(self):
    #     pass

    def fit(self, X, y = None):
        return self
    
    # def get_feature_names_out(self, feature_names_out):
    #     return feature_names_out
    
    def fit_transform(self, X, y = None, **fit_params):
        return super().fit_transform(X, y, **fit_params)
    
    def transform(self, X):
        X_cop = X.copy()
        bins = [0, 18, 25, 30, 35, 40 , 50, 1000]
        labels=['sous poids' ,'poids normal','surpoids','obésité modérée','obésité sévère','obésité morbide','obésité massive']
        X_cop['BMI_cat']=pd.cut(X_cop['bmi'], bins=bins, labels=labels, right=False)
        X_cop= X_cop.drop(['bmi'], axis=1)
        return X_cop