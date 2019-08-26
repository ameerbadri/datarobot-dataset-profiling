import pandas as pd 
import pandas_profiling 

# read the dataset 
df = pd.read_csv('10K_Lending_Club_Loans.csv')
# Profile the dataset 
profile = df.profile_report(title='10K Lending Club Loans Dataset Profile')
profile.to_file(output_file="10K_Lending_Club_Loans_dataset_profile.html")
