#!/usr/bin/env python
# coding: utf-8
import pickle
import pandas as pd
import numpy as np
import sklearn

print(f'pandas=={pd.__version__}')
print(f'numpy=={np.__version__}')
print(f'sklearn=={sklearn.__version__}')

from sklearn.feature_extraction import DictVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import make_pipeline 


def load_data():
    data_url = 'https://raw.githubusercontent.com/alexeygrigorev/mlbookcamp-code/master/chapter-03-churn-prediction/WA_Fn-UseC_-Telco-Customer-Churn.csv'
    df = pd.read_csv(data_url)
    df.columns = df.columns.str.lower().str.replace(' ', '_')

    categorical_columns = list(df.dtypes[df.dtypes == 'object'].index)

    for c in categorical_columns:
        df[c] = df[c].str.lower().str.replace(' ', '_')

    df.totalcharges = pd.to_numeric(df.totalcharges, errors='coerce')
    df.totalcharges = df.totalcharges.fillna(0)

    df.churn = (df.churn == 'yes').astype(int)
    return df 


def train_model(df):
    numerical = ['tenure', 'monthlycharges', 'totalcharges']

    categorical = [
        'gender',
        'seniorcitizen',
        'partner',
        'dependents',
        'phoneservice',
        'multiplelines',
        'internetservice',
        'onlinesecurity',
        'onlinebackup',
        'deviceprotection',
        'techsupport',
        'streamingtv',
        'streamingmovies',
        'contract',
        'paperlessbilling',
        'paymentmethod',
    ]
    train_dict = df[categorical + numerical].to_dict(orient='records') #changes to dictionary like structure
    y_train = df.churn
    pipeline = make_pipeline(
        DictVectorizer(),
        LogisticRegression(solver='newton-cg')
    )
    pipeline.fit(train_dict, y_train)
    return pipeline


#save the pipeline

# Save it to a file
def save_model(filename, pipeline):
    with open(filename, "wb") as f_out:
        pickle.dump(pipeline, f_out)  #dump:is a python methode that Serializes(saves) the pipeline and writes it to the file f_out.
        print(f"Model saved to {filename}")

# === Main script ===
df = load_data()
pipeline = train_model(df)
save_model("churn_model.pkl", pipeline)



