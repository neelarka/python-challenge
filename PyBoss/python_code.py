import os
import csv
from pathlib import Path  
filepath = Path("employee_data.csv")
with open(filepath, newline="", encoding='utf-8' ) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    reader = csv.reader(csvfile)
    next(reader, None)
    emp_id = []
    name = []
    DOB = []
    SSN = []
    state = []
    for row in csvreader:
        emp_id.append(row[0])
        name.append(row[1])
        DOB.append(row[2])
        SSN.append(row[3])
        state.append(row[4])

FirstName = []
LastName = []
for elements in name:
    namelist = (elements.split())
    FirstName.append(namelist[0])
    LastName.append(namelist[1])
    
date = []
month = []
year = []
New_DOB_list = []
for elements in DOB:
    DOBlist = (elements.split('-'))
    date.append(DOBlist[0])
    month.append(DOBlist[1])
    year.append(DOBlist[2])
    New_DOB = (DOBlist[2] + '/' + DOBlist[1] + '/' + DOBlist[0]) 
    New_DOB_list.append(New_DOB)
#print(New_DOB_list)

New_SSN_list = []
for elements in SSN:
    SSNlist = (elements.split('-'))
    New_SSN = ('***' + '-' + '**' + '-' + SSNlist[2])
    New_SSN_list.append(New_SSN)
#print(New_SSN_list)

# Function returns the state abbreviation indexed by state name
def get_state_abbrev(state):
    us_state_abbrev = {
    'Alabama': 'AL',
    'Alaska': 'AK',
    'Arizona': 'AZ',
    'Arkansas': 'AR',
    'California': 'CA',
    'Colorado': 'CO',
    'Connecticut': 'CT',
    'Delaware': 'DE',
    'Florida': 'FL',
    'Georgia': 'GA',
    'Hawaii': 'HI',
    'Idaho': 'ID',
    'Illinois': 'IL',
    'Indiana': 'IN',
    'Iowa': 'IA',
    'Kansas': 'KS',
    'Kentucky': 'KY',
    'Louisiana': 'LA',
    'Maine': 'ME',
    'Maryland': 'MD',
    'Massachusetts': 'MA',
    'Michigan': 'MI',
    'Minnesota': 'MN',
    'Mississippi': 'MS',
    'Missouri': 'MO',
    'Montana': 'MT',
    'Nebraska': 'NE',
    'Nevada': 'NV',
    'New Hampshire': 'NH',
    'New Jersey': 'NJ',
    'New Mexico': 'NM',
    'New York': 'NY',
    'North Carolina': 'NC',
    'North Dakota': 'ND',
    'Ohio': 'OH',
    'Oklahoma': 'OK',
    'Oregon': 'OR',
    'Pennsylvania': 'PA',
    'Rhode Island': 'RI',
    'South Carolina': 'SC',
    'South Dakota': 'SD',
    'Tennessee': 'TN',
    'Texas': 'TX',
    'Utah': 'UT',
    'Vermont': 'VT',
    'Virginia': 'VA',
    'Washington': 'WA',
    'West Virginia': 'WV',
    'Wisconsin': 'WI',
    'Wyoming': 'WY',
    }
    if state in us_state_abbrev:        
        return us_state_abbrev[state] 
    else:
        return "state" 

emp_state = []
for elements in state:
    emp_state.append(get_state_abbrev(elements))
#print(emp_state)

zipped_list = zip(  emp_id, FirstName, LastName, New_DOB_list, New_SSN_list, emp_state)

# Set variable for output file
output_file = os.path.join("employee_data.csv")
with open("output_file_PyBoss.csv", "w") as csvfile:
    header = ['Emp ID', 'First Name', 'Last Name', 'DOB', 'SSN', 'State']
    writer = csv.writer(csvfile, delimiter=',')
    writer.writerow(header)
    writer.writerows(zipped_list)