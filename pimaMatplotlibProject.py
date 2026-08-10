import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("cleaned_diabetes.csv")

outcome_counts = data["Outcome"].value_counts()

# Subplot for relations between multiple variables and the outcomes in scatter plots as well as other visiual representations of the data. It should be notes that the indices start from 0.

figures, axes = plt.subplots(3, 3, figsize=(10, 8))
# This subplot (0,0) is a scatter plot, showing the correlation between pregnancies and insulin, which is a negative relationship at -0.17. The data here nearly lines up into whole numbers, because the number of pregnancies is discrete and may only be whole numbers, not continous, thus why the scatterplot looks the way it does.
axes[0, 0].scatter(data["Pregnancies"], data["Insulin"])
axes[0, 0].set_xlabel("Pregnancies")
axes[0, 0].set_ylabel("Insulin")
axes[0, 0].set_title("Pregnancies and Insulin correlation")

# The subplot at (0,1) represents the correlation between skin thickness and BMI which is a strong, positive correlation at 0.84.
axes[0, 1].scatter(data["SkinThickness"], data["BMI"])
axes[0, 1].set_xlabel("Skin Thickness")
axes[0, 1].set_ylabel("BMI")
axes[0, 1].set_title("Skin Thickness and BMI correlation")

# This subplot (0,2) compares the data between Glucose and Insulin, a positive correlation at 0.58.
axes[0, 2].scatter(data['Glucose'], data["Insulin"])
axes[0, 2].set_xlabel("Glucose")
axes[0, 2].set_ylabel("Insulin")
axes[0, 2].set_title("Glucose and Insulin correlation")

# This subplot (1,0) represents the correlation between age and skin thickness, a weak, positive correlation at 0.17.
axes[1, 0].scatter(data["Age"], data["SkinThickness"])
axes[1, 0].set_xlabel("Age")
axes[1, 0].set_ylabel("Skin Thickness")
axes[1, 0].set_title("Age and Skin Thickness correlation")

# This subplot (1,1) represents the correlation between insulin and BMI, colored by outcome. It is a weak, positive correlation at 0.22. Visiually, we can infer that diabetic patients cluster at higher levels of insulin slightly higher levels of BMI than non-diabetic patients.
axes[1, 1].scatter(data["Insulin"], data["BMI"],
                   c=data["Outcome"], edgecolors='black')
axes[1, 1].set_xlabel("Insulin")
axes[1, 1].set_ylabel("BMI")
axes[1, 1].set_title("Insulin and BMI correlation")

# Histogram (1,2) to show the rate of obesity, overweight and normal weight in the dataset. The majority of the entries in the dataset are obese with a BMI over 30.

axes[1, 2].hist(
    data["BMI"],
    bins=[0, 18.5, 25, 30, data["BMI"].max()],
    edgecolor='black',
    color='lightblue'
)
axes[1, 2].set_title("Weight Distribution in the Dataset")
axes[1, 2].set_xlabel("BMI")
axes[1, 2].set_ylabel("Frequency")

# Subplot (2,0) is a scatter plot showing the correlation between age and glucose which is a medium positive correlation at around 0.34.
axes[2, 0].scatter(data["Age"], data["Glucose"])
axes[2, 0].set_xlabel("Age")
axes[2, 0].set_ylabel("Glucose")
axes[2, 0].set_title("Age and Glucose correlation")

# Subplot (2,1) shows the correlation between glucose and BMI, a weak positive correlation at 0.21, grouped by outcomes through color. Diabetic patients to have higher glucose overall, but there is no notable difference between BMI for diabetic and non-diabetic patients.
axes[2, 1].scatter(data["Glucose"], data["BMI"],
                   s=data['Insulin'] * 1.3, c=data["Outcome"], edgecolors='black', alpha=0.7)
axes[2, 1].set_xlabel("Glucose")
axes[2, 1].set_ylabel("BMI")
axes[2, 1].set_title(
    "Glucose vs BMI by Diabetes Outcome")

# Pie chart shows the portion of diabetic to non-diabetic patients, about 1/3 to 2/3
# Here we established a python list of colors for the pie chart
colors = ['yellow', 'cyan']

axes[2, 2].pie(outcome_counts, colors=colors, labels=["No Diabetes", "Diabetes"],
               autopct='%1.1f%%', explode=[0.3, 0], startangle=90, shadow=True)
axes[2, 2].set_title("Diabetes Outcome Distribution")


plt.tight_layout()
plt.grid()
plt.show()
