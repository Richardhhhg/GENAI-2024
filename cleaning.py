import pickle
import pandas as pd
import numpy as np
import gzip

with gzip.open('variables.pkl.gz', 'rb') as f:
    X_train, X_test, y_train, y_test = pickle.load(f)

print(X_train[:20])