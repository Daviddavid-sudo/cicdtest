import sys
import os
sys.path.append(os.getcwd())
from src.pipeline import grid_search, X_test, y_test, X

def test_model_score():
    score = grid_search.score(X_test, y_test)
    assert score > 0.80


def test_model_charges_dropped():
    assert "charges" not in X.columns

    
def test_age_type():
    assert X['age'].dtype == 'int64'

