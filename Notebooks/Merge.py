import pandas as pd

years = [str(year) for year in range(2017, 2024)]

dataset_names = []
# Loop through the years and import the corresponding datasets
for year in years:
    # Construct the filename for the current year
    filename = year + '.csv'
    
    # Construct the variable name for the current year
    varname = 'FIFA' + year
    
    # Import the dataset and assign it to the variable
    exec(f"{varname} = pd.read_csv('../Data/Fifa/{filename}')")

    exec(f"{varname}['Version'] = '{varname}'")

    dataset_names.append(varname)

years = [str(year) for year in range(2018, 2024)]

df = pd.read_csv('../Data/Fifa/2017.csv')

for year in years:
  varname = 'FIFA' + year
  exec(f"df = pd.concat([df,{varname}], ignore_index=True)")

df.to_csv('../Data/Fifa/FIFA_2017-2023.csv', index=False)
