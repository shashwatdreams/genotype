import pandas as pd
import numpy as np
import os

data_dir = "/../../CS2PD/"

def remove_outliers(df, column_names):
    for column in column_names:
        Q1 = df[column].quantile(0.25)
        Q3 = df[column].quantile(0.75)
        IQR = Q3 - Q1
        lower_bound = Q1 - 1.5 * IQR
        upper_bound = Q3 + 1.5 * IQR
        df = df[(df[column] >= lower_bound) & (df[column] <= upper_bound)]
    return df

def process_file(filename):
    filepath = os.path.join(data_dir, filename)
    # Read the CSV file
    df = pd.read_csv(filepath)
    # Calculate basic statistics
    summary_stats = df.describe()
    # You can print or save the summary statistics if needed
    print("Summary statistics for", filename)
    print(summary_stats)
    # Clean the data by removing outliers
    cleaned_df = remove_outliers(df, df.columns[1:])
    return cleaned_df

gt_df = pd.read_csv('GT_DataPD_MIT-CS2PD.csv', usecols=['H'])

cleaned_data = []
for filename in gt_df['H'].dropna():
    try:
        cleaned_df = process_file(filename)
        # Append cleaned data to the list
        cleaned_data.append(cleaned_df)
    except Exception as e:
        print(f"Error processing file {filename}: {e}")

# Concatenate all cleaned dataframes if you need one single dataframe
final_dataset = pd.concat(cleaned_data, ignore_index=True)

# Now, final_dataset is ready for further processing or model training