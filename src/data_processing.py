import pandas as pd


def load_data(excel_path): 
    df = pd.read_excel(excel_path)  #To load the excel file
    df.set_index([df.columns[0], df.columns[1]], inplace=True)  # Set the first and second columns as the index
    df = df.apply(pd.to_numeric, errors='coerce') 
    df.dropna(inplace=True)  #drop missing values

    return df



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
