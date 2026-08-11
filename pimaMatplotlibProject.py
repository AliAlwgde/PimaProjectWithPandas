import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("PimaPandasProjectData/cleaned_diabetes.csv")

outcome_counts = data["Outcome"].value_counts()


figures, axes = plt.subplots(3, 3, figsize=(10, 8))

axes[0, 0].scatter(data["Pregnancies"], data["Insulin"])
axes[0, 0].set_xlabel("Pregnancies")
axes[0, 0].set_ylabel("Insulin")
axes[0, 0].set_title("Pregnancies vs Insulin")

axes[0, 1].scatter(data["SkinThickness"], data["BMI"])
axes[0, 1].set_xlabel("Skin Thickness")
axes[0, 1].set_ylabel("BMI")
axes[0, 1].set_title("Skin Thickness vs BMI")

axes[0, 2].scatter(data['Glucose'], data["Insulin"])
axes[0, 2].set_xlabel("Glucose")
axes[0, 2].set_ylabel("Insulin")
axes[0, 2].set_title("Glucose vs Insulin")

axes[1, 0].scatter(data["Age"], data["Pregnancies"])
axes[1, 0].set_xlabel("Age")
axes[1, 0].set_ylabel("Pregnancies")
axes[1, 0].set_title("Age vs Pregnancies")

axes[1, 1].scatter(data["Insulin"], data["BMI"],
                   c=data["Outcome"], edgecolors='black')
axes[1, 1].set_xlabel("Insulin")
axes[1, 1].set_ylabel("BMI")
axes[1, 1].set_title("Insulin vs BMI")

weight_categories = pd.cut(
    data["BMI"],
    bins=[18.5, 25, 30, float("inf")],
    labels=["Normal", "Overweight", "Obese"]
).value_counts().sort_index()

axes[1, 2].barh(
    weight_categories.index,
    weight_categories.values,
    color="lightblue"
)

axes[1, 2].set_title("Weight Distribution in the Dataset")
axes[1, 2].set_xlabel("Frequency")
axes[1, 2].set_ylabel("BMI Category")
axes[1, 2].set_title("Weight Distribution in the Dataset")
axes[1, 2].set_xlabel("BMI")
axes[1, 2].set_ylabel("Frequency")

axes[2, 0].scatter(data["Age"], data["Glucose"])
axes[2, 0].set_xlabel("Age")
axes[2, 0].set_ylabel("Glucose")
axes[2, 0].set_title("Age vs Glucose")

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
plt.savefig("PimaPandasProjectData/eda_visualizations.png", dpi=300)
plt.show()
