from sklearn.linear_model import LinearRegression, Ridge, Lasso, ElasticNet
from sklearn.preprocessing import OneHotEncoder, LabelBinarizer, MinMaxScaler, StandardScaler, PolynomialFeatures, Binarizer, KBinsDiscretizer, OrdinalEncoder
from sklearn.model_selection import train_test_split, cross_val_score, learning_curve, GridSearchCV
from sklearn.pipeline import make_pipeline
from sklearn.compose import make_column_transformer, make_column_selector
from sklearn.base import BaseEstimator, TransformerMixin
import sys
import os
sys.path.append(os.getcwd())
from src.data_pd import data
from src.class_dropfeatureselector import DropFeatureSelector


X = data.drop(['charges'], axis=1)
y = data['charges']
X_train, X_test, y_train, y_test = train_test_split(X, y, shuffle=True, train_size=0.85, random_state=42, stratify=X['smoker'])

preprocessor = make_pipeline(DropFeatureSelector(),make_column_transformer((StandardScaler(), ['children','age']),
                                                     (OrdinalEncoder(), ['smoker', 'sex']), (OneHotEncoder(),['region',"BMI_cat"])), PolynomialFeatures(2))


model = make_pipeline(preprocessor, LinearRegression())


param_grid = {
    'pipeline__polynomialfeatures__degree': [1,2,3]
}

grid_search = GridSearchCV(
    model,
    param_grid,
    cv=5,
    scoring='r2'
)

grid_search.fit(X_train, y_train)

print(grid_search.score(X_test,y_test))