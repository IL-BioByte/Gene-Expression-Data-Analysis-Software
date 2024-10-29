import pandas as pd

def load_data(excel_path): 
    df = pd.read_excel(excel_path)  #To load the excel file
    df.set_index(df.columns[0],inplace=True)  #Set first column as index (Sample IDs)
    df = df.apply(pd.to_numeric, errors='coerce')  # invalid parsing will be set as NaN
    #df.fillna(df.mean(), inplace=True) #Use this if want to use mean to replace missing value
    df.dropna(inplace=True)  #drop missing values

    return df

if __name__ == "__main__":
    df = load_data(excel_path)
    print(df.head())


# #DATA NORMALIZATION
# def normalize_data(df):
#     #using the mean of the control samples
#     control_mean = df['Control'].mean()  # 'Control' must be a column
#     normalized_df = df / control_mean
#     return normalized_df

# #Handling OUTLIERS USING IQR
# def remove_outliers(df):
#     Q1 = df.quantile(0.25)
#     Q3 = df.quantile(0.75)
#     IQR = Q3 - Q1
#     df_no_outliers = df[~((df < (Q1 - 1.5 * IQR)) | (df > (Q3 + 1.5 * IQR))).any(axis=1)]
#     return df_no_outliers
