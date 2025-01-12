import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.linear_model import Lasso  #for finding importantr features



def fill_data_by_zero(df, columns: list = None):
    if columns is None :
        df = df.fillna(0)
    else:
        
        if isinstance(columns, str):
            columns = [columns]
            
        for col in columns:
            if col in df.columns:
                df[col] = df[col].fillna(0)



def fill_data_by_avg(df, columns: list = None):
    if columns is None or len(columns) == 0:
        return df.fillna(df.mean())
    else:
    
        if isinstance(columns, str):
            columns = [columns]
        
        for col in columns:
            if col in df.columns:
                df[col] = df[col].fillna(df[col].mean())
    
  
    
def remove_duplicates(df):
    return df.drop_duplicates(inplace=True)



def rename_columns(df, columns: dict = None):
    if columns is None or len(columns) == 0:
        return df
    
    df.rename(columns=columns, inplace=True)



def convert_column_type(df, column, type):
    df[column] = df[column].astype(type)
 
 
    
def remove_outliers(df, columns: list = None):
    if columns is None or len(columns) == 0:
        return df
    
    if isinstance(columns, str):
        columns = [columns]
        
    for col in columns:
        if col in df.columns:
            df[col] = df[col].clip(df[col].quantile(0.01), df[col].quantile(0.99))
            
            
            

# encoding 
def encode_categorical_col(df):
    cat_cols = [col for col in df.columns if pd.api.types.is_numeric_dtype(df[col]) == False and not pd.api.types.is_datetime64_any_dtype(df[col])]
       
    for col in cat_cols:
        df[col] = LabelEncoder().fit_transform(df[col])
           
           
           
#scaling
def scale_data(df):
    num_cols = [col for col in df.columns if pd.api.types.is_numeric_dtype(df[col])]
    
    df[num_cols] = StandardScaler().fit_transform(df[num_cols])
    
    

def feature_engineering():
    pass



def merge_new_data(df1, df2, on, how):
    return pd.merge(df1, df2, on=on, how=how)



def feature_importance_by_Lasso(df, target):
    """
    Determine the importance of features using Lasso regression.

    Parameters:
    df (pd.DataFrame): The input dataframe containing features and target.
    target (str): The name of the target column.

    Returns:
    pd.DataFrame: A dataframe containing the importance of each feature, sorted in descending order.
    """
    x = df.drop(target, axis=1)
    y = df[target]
    
    X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)
    
    lasso = Lasso(alpha=0.01)
    lasso.fit(X_train, y_train)
    
    importance = np.abs(lasso.coef_)
    feature_names = np.array(X_train.columns)
    
    return pd.DataFrame(importance, index=feature_names, columns=['importance']).sort_values('importance', ascending=False)
    