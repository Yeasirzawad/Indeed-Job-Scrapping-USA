import pandas as pd
import numpy as np
import re

# Wrangling function
def wrangle(path):
    # Read the CSV file into a DataFrame
    df = pd.read_csv(path)

    # Drop unnecessary columns
    cols_to_drop_1 = ['rating','Unnamed: 0']
    df.drop(columns=cols_to_drop_1 ,inplace=True)

    # Clean 'ceo_approve_percentage' column
    df['ceo_approve_percentage'] = df['ceo_approve_percentage'].str.replace("%","")
    df['ceo_approve_percentage'] = df['ceo_approve_percentage'].fillna(0)
    df['ceo_approve_percentage'] = df['ceo_approve_percentage'].astype(int)
    df['ceo_approve_percentage'].replace(0,np.nan)

    # Clean 'company_size' column
    df['company_size'] = df['company_size'].str.replace('more than\n', '>').str.replace('less than\n', '<').str.replace(',', '').str.replace(' to ', '-').fillna('0')
    df['company_size'] = df['company_size'].replace({'0': 'Not Mentioned'})
    df['company_size'] = df['company_size'].replace({'Hidden by employer': 'Not Mentioned'})

    # Clean 'review_count' column
    df['review_count'] = df['review_count'].str.replace('Reviews',"").str.replace(' Reviews',"").str.strip()
    
    # Define function to convert review counts to thousands
    def convert_to_thousands(value):
        if isinstance(value, float) or value == '':  # Check if the value is a float (NaN) or an empty string
            return 0  # Return 0 for NaN or empty string
        elif 'K' in value:
            return float(value.replace('K', '')) * 1000
        else:
            return float(value)

    # Apply the function to the 'review_counts' column
    df['review_count'] = df['review_count'].apply(convert_to_thousands)

    # Define function to determine salary type
    def make_salary_type_column(salary):
        if 'hour' in salary:
            return 'hour'
        if 'month' in salary:
            return 'month'
        if 'year' in salary:
            return 'year'
        else:
            'Not Mentioned'

    # Apply the salary type function to create a new column
    df['salary_type']  = df['salary'].apply(make_salary_type_column)

    # Clean 'salary' column
    df['salary'] = df['salary'].str.replace('$',"").str.replace(',',"").str.replace('From',"").str.replace("Up to","").str.replace('an hour',"").str.replace("a month","").str.replace("a year","")
    df['salary']= df['salary'].str.strip()
    df['salary'].replace('No Salary',np.nan)

    # Split 'salary' column into 'min_salary' and 'max_salary'
    df[['min_salary', 'max_salary']] = df['salary'].str.split(' - ', expand=True)

    # Convert string columns to numeric
    df['min_salary'] = pd.to_numeric(df['min_salary'], errors='coerce')
    df['max_salary'] = pd.to_numeric(df['max_salary'], errors='coerce')

    # Define function to adjust salaries based on salary type
    def adjust_salaries(row):
        if row['salary_type'] == 'hour':
            row['min_salary'] = row['min_salary'] * 1920
            row['max_salary'] = row['max_salary'] * 1920
        elif row['salary_type'] == 'month':
            row['min_salary'] = row['min_salary']*12
            row['max_salary'] = row['max_salary']*12
        return row

    # Apply adjustment function to the DataFrame
    df[['min_salary', 'max_salary']] = df.apply(adjust_salaries, axis=1)[['min_salary', 'max_salary']]

    # Define function to extract revenue information
    def extract_revenue(rev_str):
        if pd.isna(rev_str):
            return pd.Series([None, None])
        else:
            # Extract numerical values using regular expression
            matches = re.findall(r'\$([0-9\.]+)([BM]?)', rev_str)
            if len(matches) == 1:  # If only one value is found
                return pd.Series([matches[0][0] + matches[0][1], matches[0][0] + matches[0][1]])
            elif len(matches) == 2:  # If a range is found
                return pd.Series([matches[0][0] + matches[0][1], matches[1][0] + matches[1][1]])
            else:
                return pd.Series([None, None])

    # Apply the function to create min_revenue and max_revenue columns
    df[['min_revenue', 'max_revenue']] = df['company_revenue'].apply(extract_revenue)

    # Combine min_revenue and max_revenue into a single column
    df['min_max_revenue'] = df['min_revenue'] + "-" + df['max_revenue']
    df['min_max_revenue'] = df['min_max_revenue'].fillna('Not Mentioned')
    df['min_max_revenue'] = df['min_max_revenue'].replace({'1M-1M': '<1M', '10B-10B': '>10B'})

    # Define function to encode measure categories
    def encode_measure(row):
        if row == 'High':
            return 5
        elif row == 'Above average':
            return 4
        elif row == 'Average':
            return 3
        elif row == 'Below average':
            return 2
        elif row == 'Low':
            return 1
        else:
            return row  # if the value is not one of the specified categories, return the original value

    # Apply encoding function to measure columns
    measures = ['Happiness',  'Stress-free',  'Purpose',   'Satisfaction',  'Flexibility',  'Achievement', 'Learning',  'Inclusion',  'Support',   'Appreciation',   'Energy',  'Compensation',  'Management', 'Trust',  'Belonging']
    for measure in measures:
        df[measure] = df[measure].apply(encode_measure)

    # Define skills to extract from the 'description' column
    skills = ['python', 'mysql', 'postgresql', 'tensorflow', 'pytorch', 'aws', 'tableau', 'powerbi', 'hadoop', 'kafka', 'java', 'excel', 'scikit-learn', 'sklearn', ' r ', 'scala']

    # Fill missing values in 'description' column with an empty string
    df['description'] = df['description'].fillna('')

    # Iterate over each skill
    for skill in skills:
        # Create a new column with the skill name and initialize with 0
        df[skill] = 0
        # Set 1 to the column if the skill appears in the description
        df.loc[df['description'].str.contains(skill, case=False), skill] = 1

    # Drop redundant columns
    cols_to_drop_2 = ['min_revenue','max_revenue','company_revenue']
    df.drop(columns=cols_to_drop_2,inplace=True)

    # Reset index and return the DataFrame
    return df.reset_index()
