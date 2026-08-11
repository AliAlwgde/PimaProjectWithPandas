import pandas as pd

# This file serves only to explore and clean the data of zero-coded values.

data = pd.read_csv('PimaPandasProjectData/diabetes.csv')

# print(data.columns)
# Columns present are: Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age, Outcome

# print(data.info())

# All data columns are integers, except BMI and DiabetesPedigreeFunction which are floats. There are no null/NaN/? values in the dataset.

# print(data.isnull().sum()) # Confirming there are no null values in the dataset.
# pd.set_option('display.max_columns', None)
# print(data.describe())
# This gives us a general overview of the data. Here we see that many data values have minimums of zero where not physiologically plausible for a human being, such as glucose, blood pressure, skin thickness, insulin, and BMI. This data will be considered 'missing data' and removed from the data set using pandas. Other datasets can have a valid zero values, however, such as the number of pregnancies.


# We want to explore the correlations between different variables in the dataset before cleaning.
# pd.set_option('display.max_columns', None)
# print('Correlation matrix:\n \n')
# correlations = data.corr(numeric_only=True)
# print(correlations)
# print("\n\n\n\n\n\n\n\n\n")
# From this we can tell that while relationships exist between most variables, they are not particularly strong. The strongest correlations are between outcome and insulin (around 0.47) and between BMI and skin thickness (0.39). This will be turned into a .csv file for later examination and comparison.

data.corr(numeric_only=True).to_csv(
    "PimaPandasProjectData/correlation_matrix.csv"
)


# Here, a function will be used and the data will be passed through it in order to remove zero-coded values. It is important to note that since this is a beginner project, I have decided to remove the zeros initially to make the data easier to work with. This introduces the problem of selection bias, however.

def data_filtering(data):
    # filter out rows where glucose, blood pressure, skin thickness, insulin and BMI are 0.
    filteredData = data[(data['Glucose'] != 0) &
                        (data['BloodPressure'] != 0) & (data['SkinThickness'] != 0) & (data['Insulin'] != 0) & (data['BMI'] != 0)]
    # this filters the whole dataset to remove missing values, where values are zero.
    return filteredData


filteredData = data_filtering(data)


# After cleaning, we want to explore the correlations between different variables in the dataset.
pd.set_option('display.max_columns', None)
print('Correlational matrix:\n \n')
correlations = filteredData.corr(numeric_only=True)
print(correlations)
print("\n\n\n\n\n\n\n\n\n")
# From this, we observe much stronger relationships, such as that between age and pregnancies (0.67), glucose and insulin (0.58), outcome and age (0.35), outcome and insulin (0.30), and blood pressure and BMI (0.30). This will also be turned into a .csv file to observe and compare later on.

filteredData.corr(numeric_only=True).to_csv(
    "PimaPandasProjectData/cleaned_correlation_matrix.csv"
)

print(filteredData.info())
# This prints out the data after the zero values are removed.

# After this, we are left wtih 392 observations instead of 768, suggesting nearly half the rows had zero-coded data in one of the fields. We will turn the filtered data into a new csv file to work with.

filteredData.to_csv("PimaPandasProjectData/cleaned_diabetes.csv", index=False)

# This completes our initial exploration of the data. The goal with this was to understand how many data entries we had, how many we were left with after removing zero-coded data (while acknowling selection bias), the columns we had, the minimums and maximums, and the correlations between different variables. After this, I will move on to working with the cleaned data in a more detailed manner.
