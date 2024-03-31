import pandas as pd
from sklearn.preprocessing import StandardScaler
import seaborn as sns
# Mount Google Drive

# Path to the CSV file in Google Drive
file_path = 'table.csv'
df = pd.read_csv(file_path)
#file_pathh = '/content/drive/My Drive/table_app.csv'
#df_og = pd.read_csv(file_pathh)

import pandas as pd
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, roc_auc_score, roc_curve, auc

df2 = df.copy()
features_to_drop = ['Unnamed: 0', 'population', 'minority_population', 'number_of_owner_occupied_units', 'number_of_1_to_4_family_units', 'census_tract_number', 'tract_to_msamd_cat', 'co_appl_sex_vs_NA_cat_1', 'co_appl_sex_vs_NA_cat_2', 'appl_gender_vs_NA_1', 'appl_gender_vs_NA_2',
                   'is_majority_1', 'is_majority_2', 'is_majority_3', 'is_black_1', 'is_black_2','hoepa_status_cat_1', 'hoepa_status_cat_2',
                   'appl_ethnicity_cat_1','tract_to_msamd_income','appl_ethnicity_cat_2','appl_ethnicity_cat_3','appl_ethnicity_cat_4',
                   ]
more_to_drop = df.columns[42:len(df.columns)]
all_to_drop = []
for i in range(len(features_to_drop)):
   all_to_drop.append(features_to_drop[i])
for i in range(len(more_to_drop)):
   all_to_drop.append(more_to_drop[i])
for column in df.columns:
   if column in all_to_drop:
       df = df.drop(labels = [column], axis = 1)
print(df.columns)



X = df.drop('loan_approved', axis=1)  # Features
y = df['loan_approved']  # Target variable

# Split the data into training and testing sets

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
for data in [X_train, X_test, y_train, y_test]:
    data.reset_index(drop=True,inplace=True)

scaler = StandardScaler()

X_train_norm = scaler.fit_transform(X_train)

X_test_norm = scaler.transform(X_test)
model = LogisticRegression(random_state=42, max_iter=1000)

# Fit the model on the training data
model.fit(X_train_norm, y_train)

# Make predictions on the testing data (probabilities)
y_pred_proba = model.predict_proba(X_test_norm)[:, 1]

# Calculate ROC curve
fpr, tpr, thresholds = roc_curve(y_test, y_pred_proba)
roc_auc = auc(fpr, tpr)

# Find the optimal threshold based on Youden's J statistic which is sensitivity + specificity -1
optimal_idx = np.argmax(tpr - fpr)
optimal_threshold = thresholds[optimal_idx]

# Make predictions using the optimal threshold if the oprobability is bigger than the threshold then we do TRUE
y_pred_optimal = (y_pred_proba >= optimal_threshold).astype(int)

# Calculate evaluation metrics with optimal threshold
accuracy_optimal = accuracy_score(y_test, y_pred_optimal)
precision_optimal = precision_score(y_test, y_pred_optimal)
recall_optimal = recall_score(y_test, y_pred_optimal)
f1_optimal = f1_score(y_test, y_pred_optimal)
roc_auc_optimal = roc_auc_score(y_test, y_pred_optimal)

print("Accuracy:", accuracy_optimal)
print("Precision:", precision_optimal)
print("Recall:", recall_optimal)
print("F1 Score:", f1_optimal)
print("ROC AUC Score (Optimal Threshold):", roc_auc_optimal)
print("Optimal Threshold:", optimal_threshold)

X2 = df2.drop('loan_approved', axis=1)  # Features
y2 = df2['loan_approved']  # Target variable

from joblib import dump
dump(model, 'logistic_regression_model.joblib')

df2.columns
features_to_drop = ['Unnamed: 0', 'population', 'minority_population', 'number_of_owner_occupied_units', 'number_of_1_to_4_family_units', 'census_tract_number', 'tract_to_msamd_cat', 'co_appl_sex_vs_NA_cat_1', 'co_appl_sex_vs_NA_cat_2',
                   'is_majority_1', 'is_majority_2', 'is_majority_3', 'hoepa_status_cat_1', 'hoepa_status_cat_2','tract_to_msamd_income', 'appl_gender_vs_NA_1', 'appl_gender_vs_NA_2']
# for df_selected.loc[:,'appl_gender_vs_NA'] = df_selected.loc[:,'applicant_sex_name']\.apply(lambda x:1 if ((x == 'Female')| ( x == 'Male')) else 0)
more_to_drop = df2.columns[42:len(df2.columns)]
all_to_drop = []
for i in range(len(features_to_drop)):
   all_to_drop.append(features_to_drop[i])
for i in range(len(more_to_drop)):
   all_to_drop.append(more_to_drop[i])
for column in df2.columns:
   if column in all_to_drop:
       df2 = df2.drop(labels = [column], axis = 1)
print(df2.columns)

X2 = df2.drop('loan_approved', axis=1)  # Features
y2 = df2['loan_approved']  # Target variable

X_train2, X_test2, y_train2, y_test2 = train_test_split(X2, y2, test_size=0.2, random_state=42)
for data in [X_train2, X_test2, y_train2, y_test2]:
    data.reset_index(drop=True,inplace=True)

scaler2 = StandardScaler()

X_train_norm2 = scaler2.fit_transform(X_train2)

X_test_norm2 = scaler2.transform(X_test2)
model2 = LogisticRegression(random_state=42, max_iter=1000)

# Fit the model on the training data
model2.fit(X_train_norm2, y_train2)

# Make predictions on the testing data (probabilities)
y_pred_proba2 = model2.predict_proba(X_test_norm2)[:, 1]

# Calculate ROC curve
fpr2, tpr2, thresholds2 = roc_curve(y_test2, y_pred_proba2)
roc_auc2 = auc(fpr, tpr)

# Find the optimal threshold based on Youden's J statistic which is sensitivity + specificity -1
optimal_idx2 = np.argmax(tpr2 - fpr2)
optimal_threshold2 = thresholds[optimal_idx2]

# Make predictions using the optimal threshold if the oprobability is bigger than the threshold then we do TRUE
y_pred_optimal2 = (y_pred_proba2 >= optimal_threshold2).astype(int)

# Calculate evaluation metrics with optimal threshold
accuracy_optimal2 = accuracy_score(y_test2, y_pred_optimal2)
precision_optimal2 = precision_score(y_test2, y_pred_optimal2)
recall_optimal2 = recall_score(y_test2, y_pred_optimal2)
f1_optimal2 = f1_score(y_test2, y_pred_optimal2)
roc_auc_optimal2 = roc_auc_score(y_test2, y_pred_optimal2)

print("Accuracy:", accuracy_optimal2)
print("Precision:", precision_optimal2)
print("Recall:", recall_optimal2)
print("F1 Score:", f1_optimal2)
print("ROC AUC Score (Optimal Threshold):", roc_auc_optimal2)
print("Optimal Threshold:", optimal_threshold2)

