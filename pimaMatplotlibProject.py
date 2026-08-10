import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("PimaPandasProjectData/cleaned_diabetes.csv")

outcome_counts = data["Outcome"].value_counts()


figures, axes = plt.subplots(3, 3, figsize=(10, 8))

axes[0, 0].scatter(data["Pregnancies"], data["Insulin"])
axes[0, 0].set_xlabel("Pregnancies")
axes[0, 0].set_ylabel("Insulin")
axes[0, 0].set_title("Pregnancies and Insulin correlation")

axes[0, 1].scatter(data["SkinThickness"], data["BMI"])
axes[0, 1].set_xlabel("Skin Thickness")
axes[0, 1].set_ylabel("BMI")
axes[0, 1].set_title("Skin Thickness and BMI correlation")

axes[0, 2].scatter(data['Glucose'], data["Insulin"])
axes[0, 2].set_xlabel("Glucose")
axes[0, 2].set_ylabel("Insulin")
axes[0, 2].set_title("Glucose and Insulin correlation")

axes[1, 0].scatter(data["Age"], data["SkinThickness"])
axes[1, 0].set_xlabel("Age")
axes[1, 0].set_ylabel("Skin Thickness")
axes[1, 0].set_title("Age and Skin Thickness correlation")

axes[1, 1].scatter(data["Insulin"], data["BMI"],
                   c=data["Outcome"], edgecolors='black')
axes[1, 1].set_xlabel("Insulin")
axes[1, 1].set_ylabel("BMI")
axes[1, 1].set_title("Insulin and BMI correlation")

axes[1, 2].hist(
    data["BMI"],
    bins=[0, 18.5, 25, 30, data["BMI"].max()],
    edgecolor='black',
    color='lightblue'
)
axes[1, 2].set_title("Weight Distribution in the Dataset")
axes[1, 2].set_xlabel("BMI")
axes[1, 2].set_ylabel("Frequency")

axes[2, 0].scatter(data["Age"], data["Glucose"])
axes[2, 0].set_xlabel("Age")
axes[2, 0].set_ylabel("Glucose")
axes[2, 0].set_title("Age and Glucose correlation")

axes[2, 1].scatter(data["Glucose"], data["BMI"],
                   s=data['Insulin'] * 1.3, c=data["Outcome"], edgecolors='black', alpha=0.7)
axes[2, 1].set_xlabel("Glucose")
axes[2, 1].set_ylabel("BMI")
axes[2, 1].set_title(
    "Glucose vs BMI by Diabetes Outcome")


colors = ['yellow', 'cyan']

axes[2, 2].pie(outcome_counts, colors=colors, labels=["No Diabetes", "Diabetes"],
               autopct='%1.1f%%', explode=[0.3, 0], startangle=90, shadow=True)
axes[2, 2].set_title("Diabetes Outcome Distribution")


plt.tight_layout()
plt.grid()
plt.show()
plt.savefig("PimaIndiansProjectOutput/eda_visualizations.png", dpi=300)
