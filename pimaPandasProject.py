import pandas as pd

data = pd.read_csv('cleaned_diabetes.csv')

# This second file will read the csv file we created with the cleaned data.

pd.set_option('display.max_columns', None)
# This will allow us to see all columns in the dataset when we print it, without pandas cutting anything out in the output.

# Functions in this file will aid in the reusability of the code.


def data_initialization(data):
    mean = data.mean(numeric_only=True)
    miniumum = data.min(numeric_only=True)
    maximum = data.max(numeric_only=True)
    std = data.std(numeric_only=True)
    correlations = data.corr(numeric_only=True)[
        "Outcome"].sort_values(ascending=False)
    # This will give us the correlation of each column with diabetic patients.
    outcome_means = data.groupby("Outcome").mean(numeric_only=True)

    return mean, miniumum, maximum, std, correlations, outcome_means


def display(mean, miniumum, maximum, std, correlations, diabetic_percentage, nondiabetic_percentage, obese_precentage, overweight_percentage, normal_percentage, outcome_means):
    print(f"Mean values for each column:\n: {mean}")
    print(f"\nMinimum values for each column:\n: {miniumum}")
    print(f"\nMaximum values for each column:\n: {maximum}")
    print(f"\nCorrelational matrix:\n: {correlations}")
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
    print(
        f"\n\n\n\n\nCorelation between different variables:{data.corr(numeric_only=True)}")


def precentages(data):
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
diabetic_percentage, nondiabetic_percentage, obese_precentage, overweight_percentage, normal_percentage = precentages(
    data)
display(mean, minimum, maximum, std, correlations,
        diabetic_percentage, nondiabetic_percentage, obese_precentage, overweight_percentage, normal_percentage, outcome_means)


# This is the information attained from the dataset:
# 1. The mean number of pregnancies is 3.3 with a standard deviation of 3.21, with a minimum of 0 and a maximum of 17.
# 2. The mean number for glucose is 122.63 with a standard deviation of 30.86, with a minumum of 56 and a maximum of 198.
# 3. The mean blood pressure is 24 with a standard deviation of 12.5, with a minimum of 24, and a maximum of 110.
# 4. The mean skin thickness is 29.5 with a standard deviation of 10.52, with a minimum of 7, and a maximum of 63.
# 5. The mean insulin is 156.06 with a standard deviation of 118.84, with a minimum of 14, and a maximum of 846.
# 6. The mean BMI is 33.09 with a standard deviation of 7.03, with a minimum of 18.2, and a maximum of 67.1.
# 7. The mean diabetes pedigree function is 0.52 with a standard deviation of 0.34, with a minimum of 0.085, and a maximum of 2.42.
# 8. The mean age is 30.86 with a standard deviation of 10.2, with a minimum of 21, and a maximum of 81.

# Correlation between the outcome and different x-variables:
# Overall, outcome has the strongest linear correlation with glucose. Its correlation with age and insulin were around 0.3-0.35, and its correlation with other variables ranged from about 0.2-0.29.

# About 1/3 of all patients had diabetes, the other 2/3 do not.

# The majority of patients are obese at 66.84%, about 21.68% are overweight, and the remaining 11.48% are at normal weight.

# When analyzing means by outcome, it was found that women with diabetes on average had almost twice as many pregnancies as non-diabetic women, were generally 7-8 years older, had 0.15 higher pedigree functions, had a BMI 4 points above non-diabetic women, and generally had much greater skin thickness (almost 80 inches thicker), higher glucose, and higher blood pressure. This will be turned into its own CSV files and uploaded onto GitHub with the rest of the project.

# In the general correlation matrix, I focused specifically on the relations between glucose and insulin which were the strongest (positive linear correlation at around 0.7) and will be mapped with matplotlib along with other correlations. While other variables such as skin thickness and BMI were also strong, we want to focus on the relevant biological factors and metrics for diabetes.

data.corr(numeric_only=True).to_csv(
    "cleaned_correlation_matrix.csv")
