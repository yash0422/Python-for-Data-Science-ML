# imported pandas module
import pandas as pd

# Read CSV
FairDealCD = pd.read_csv('FairDealCustomerData.csv', header=None)
print(FairDealCD)

# Named column for 'Last Name', 'Full Name', and 'Eligibility'
FairDealCD.rename(columns={0: 'Last_Name', 1: 'Full_Name', 2: 'Eligibility'}, inplace=True)

# column split value defined in new data frame
New_FairDealCD = FairDealCD['Full_Name'].str.split(". ", n = 2, expand = True)

# created new column for Title
FairDealCD["Title"] = New_FairDealCD[0]

# created new column for First Name
FairDealCD["First Name"] = New_FairDealCD[1]

# created new column for Middle Name
FairDealCD["Middle Name"] = New_FairDealCD[2]

# Insert old column named (Full_Name)
FairDealCD.drop(columns=["Full_Name"], inplace=True)

#print(FairDealCD)
#print(New_FairDealCD)
New_FairDealCD.rename(columns={0: 'Title', 1: 'Name', 2: 'Middle Name'}, inplace=True)
#print(New_FairDealCD)
#print(FairDealCD)

columns = FairDealCD.columns.tolist()
columns = columns[-3:] + columns[:-3]
print(columns)
FairDealCD = FairDealCD[columns]
print(FairDealCD)

#FairDealCD.Full_Name.str.split(expand=True)
#FairDealCD[['First','Middle']] = FairDealCD.Full_Name.str.split("_", expand=True,)
# save to new csv file
FairDealCD.to_csv('Sorted FairDealCD.csv', index=False)