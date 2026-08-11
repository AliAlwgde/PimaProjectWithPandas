import pandas as pd

data = pd.read_csv('PimaPandasProjectData/cleaned_diabetes.csv')

# This second file will read the csv file we created with the cleaned data.

pd.set_option('display.max_columns', None)
# This will allow us to see all columns in the dataset when we print it, without pandas cutting anything out in the output.

# Functions in this file will aid in the reusability of the code.


def data_initialization(data):
    mean = data.mean(numeric_only=True)
    minimum = data.min(numeric_only=True)
    maximum = data.max(numeric_only=True)
    std = data.std(numeric_only=True)
    correlations = data.corr(numeric_only=True)[
        "Outcome"].sort_values(ascending=False)
    # This will give us the correlation of each column with outcome variable.
    outcome_means = data.groupby("Outcome").mean(numeric_only=True)

    return mean, minimum, maximum, std, correlations, outcome_means


def display(mean, minimum, maximum, std, correlations, diabetic_percentage, nondiabetic_percentage, obese_precentage, overweight_percentage, normal_percentage, outcome_means):
    print(f"Mean values for each column:\n: {mean}")
    print(f"\nMinimum values for each column:\n: {minimum}")
    print(f"\nMaximum values for each column:\n: {maximum}")
    print(f"\nCorrelation with outcome:\n: {correlations}")
    print(f"\nStandard deviation for each column:\n: {std}")
    print(
        f"\nPercentage of diabetic patients in the dataset: {diabetic_percentage:.2f}%")
    print(
        f"\nPercentage of non-diabetic patients in the dataset: {nondiabetic_percentage:.2f}%")
    print(
        f"\nPercentage of obese patients in the dataset: {obese_precentage:.2f}%")
    print(
        f"\nPercentage of overweight patients in the dataset: {overweight_percentage:.2f}%")
    print(
        f"\nPercentage of normal-weight patients in the dataset: {normal_percentage:.2f}%")
    print(f"\nMeans by outcome:{outcome_means}")


def percentages(data):
    total_entries = len(data)
    diabetic_entries = len(data[data['Outcome'] == 1])
    non_diabetic_entries = len(data[data['Outcome'] == 0])
    diabetic_percentage = (diabetic_entries / total_entries) * 100
    nondiabetic_percentage = (non_diabetic_entries / total_entries) * 100
    obese_entries = len(data[data['BMI'] >= 30])
    obese_precentage = (obese_entries / total_entries) * 100
    overweight_entries = len(data[(data['BMI'] >= 25) & (data['BMI'] < 30)])
    overweight_percentage = (overweight_entries / total_entries) * 100
    normal_entries = len(data[data['BMI'] < 25])
    normal_percentage = (normal_entries / total_entries) * 100
    return diabetic_percentage, nondiabetic_percentage, obese_precentage, overweight_percentage, normal_percentage


# Program execution starts here
mean, minimum, maximum, std, correlations, outcome_means = data_initialization(
    data)
diabetic_percentage, nondiabetic_percentage, obese_precentage, overweight_percentage, normal_percentage = percentages(
    data)
display(mean, minimum, maximum, std, correlations,
        diabetic_percentage, nondiabetic_percentage, obese_precentage, overweight_percentage, normal_percentage, outcome_means)
