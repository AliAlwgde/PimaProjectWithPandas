import pandas as pd

# This file serves only to explore and clean the data of zero-coded values.

data = pd.read_csv('PimaPandasProjectData/diabetes.csv')

# print(data.columns)
# Columns present are: Pregnancies, Glucodse, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age, Outcome

# print(data.info())

# All data columns are integers, except BMI and DiabetesPedigreeFunction which are floats. There are no null/NaN/? values in the dataset.

# print(data.isnull().sum()) # Confirming there are no null values in the dataset.
# pd.set_option('display.max_columns', None)
# print(data.describe())
# This gives us a general overview of the data. Here we see that many data values have minimums of zero where biologically impossible for a human being, such as glucose, blood pressure, skin thickness, insulin, and BMI. This data will be considered 'missing data' and removed from the data set using pandas.


# After this, we want to explore the correlations between different variables in the dataset.
pd.set_option('display.max_columns', None)
print('Correlational matrix:\n \n')
correlations = data.corr(numeric_only=True)
print(correlations)
print("\n\n\n\n\n\n\n\n\n")
# From this we can tell that while relationships exist between most variables, they are not very strong.


# Here, a function will be used and the data will be passed through it in order to remove zero-coded values. It is important to note that since this is a beginner project, I have decided to remove the zeros initially to make the data easier to work with. This introduces the problem of selection bias, however.

def data_filtering(data):
    # filter out rows where glucose, blood pressure, skin thickness, insulin and BMI are 0.
    filteredData = data[(data.iloc[:, 1] != 0) & (data.iloc[:, 2] != 0) & (
        data.iloc[:, 3] != 0) & (data.iloc[:, 4] != 0) & (data.iloc[:, 5] != 0)]
    # this filters the whole dataset to remove missing values, where values are zero.
    return filteredData


filteredData = data_filtering(data)
print(filteredData.info())


# This prints out the data after the zero values are removed.

# After this, we are left wtih 392 entries instead of 768, suggesting nearly half of the data entries had zero-coded data in one of the fields. We will turn the filtered data into a new csv file to work with.

filteredData.to_csv("PimaPandasProjectData/cleaned_diabetes.csv", index=False)

# This completes our initial exploration of the data. The goal with this was to understand how many data entries we had, how many we were left with after removing zero-coded data (while acknowling selection bias), the columns we had, the minimums and maximums, and the correlations between different variables. After this, I will move on to working with the cleaned data in a more detailed manner.

data.corr(numeric_only=True).to_csv(
    "PimaPandasProjectData/cleaned_correlation_matrix.csv"
)
