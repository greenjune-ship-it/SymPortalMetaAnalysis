import pandas as pd

def read_datasheet(file_path):
    if file_path.endswith('.xlsx'):
        return pd.read_excel(file_path, header=0, usecols='A:N', skiprows=[0])
    if file_path.endswith('csv'):
        return pd.read_csv(file_path)