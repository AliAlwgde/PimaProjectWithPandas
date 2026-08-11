This is a basic Exploratory Data Analysis project that explores the same Indigenous Pima diabetes dataset from Kaggle as my previous Numpy project. This project, however, focuses on cleaning the data and aggregating it through pandas and drawing visuals through Matplotlib. 

## File 1 (exploringData.py)
The first file is exploringData.py. In this file, I took the diabetes.csv dataset, did some exploratory analysis on it, and ended up cleaning it by removing zero-coded values
and created a new file, *cleaned_correlation_matrix.csv* to better view the correlations between different x-inputs after the data had been cleaned and gain a further 
understandingof the data.

## File 2 (pimaPandasProject.py)
After cleaning and gaining a greater understanding of the data, I moved to the pimaPandasProject.py file where the data was aggregated and key statistics, 
such as the rate of obesity, were calculated. Through this, the following discoveries were made from the dataset: 

This is the information attained from the dataset:
1. The mean number of pregnancies is 3.3 with a standard deviation of 3.21, with a minimum of 0 and a maximum of 17.
2. The mean number for glucose is 122.63 with a standard deviation of 30.86, with a minumum of 56 and a maximum of 198.
3. The mean blood pressure is 70.7 with a standard deviation of 12.5, with a minimum of 24, and a maximum of 110.
4. The mean skin thickness is 29.14 with a standard deviation of 10.52, with a minimum of 7, and a maximum of 63.
5. The mean insulin is 156.06 with a standard deviation of 118.84, with a minimum of 14, and a maximum of 846.
6. The mean BMI is 33.09 with a standard deviation of 7.03, with a minimum of 18.2, and a maximum of 67.1.
7. The mean diabetes pedigree function is 0.52 with a standard deviation of 0.34, with a minimum of 0.085, and a maximum of 2.42.
8. The mean age is 30.86 with a standard deviation of 10.2, with a minimum of 21, and a maximum of 81.

Correlation between the *outcome* and different x-variables:
Overall, outcome has the strongest correlation with glucose at 0.52. Its correlation with age and insulin were around 0.3-0.35, and its correlation with other variables ranged from about 0.2-0.29.

About 1/3 of all patients had diabetes, the other 2/3 do not.

The majority of patients are obese at 66.84%, about 21.68% are overweight, and the remaining 11.48% are at normal weight.

When analyzing means by outcome, it was found that women with diabetes on average had almost twice as many pregnancies as non-diabetic women, were generally 7-8 years older, had 0.15 higher pedigree functions, had a BMI 4 points above non-diabetic women, and generally greater skin thickness (almost 5-6 units thicker), higher glucose level by about 5 units, and higher blood pressure by about 6 mmHg.

In the general correlation matrix, I focused specifically on the relations between glucose and insulin which was one of the strongest relevant correlations (positive correlation at around 0.6) and will be mapped with matplotlib along with other correlations. While other variables such as skin thickness and BMI also had strong correlations, we want to focus on the biological factors and metrics for diabetes.

## File 3

After this, I moved on to visiualization in Matplotlib. 
Initialized subplot for relations between multiple variables and the outcomes in scatter plots as well as other visiual representations of the data. 
*It should be noted that the indices start from 0*

1. This subplot (0,0) is a scatter plot, showing the correlation between pregnancies and insulin, which is a weak positive relationship at 0.08. 
the data here nearly lines up into whole numbers, because the number of pregnancies is discrete and may only be whole numbers, not continous, thus why the scatterplot looks the way it does.

2. The subplot at (0,1) represents the correlation between skin thickness and BMI which is a positive relationship at 0.67 [after the data was cleaned].
3. This subplot (0,2) compares the data between Glucose and Insulin, a positive correlation at 0.58.
4. This subplot (1,0) represents the correlation between age and pregnancies, a strong, positive relationship at 0.68.
5. This subplot (1,1) represents the correlation between insulin and BMI, colored by outcome. It is a weak, positive relationship at 0.22. Visiually speaking, diabetic patients cluster at higher levels of insulin and slightly higher levels of BMI than non-diabetic patients.
6. A bar chart (1,2) to show the frequency of obesity, overweight and normal weight in the dataset. The majority of the entries in the dataset are obese with a BMI over 30 after cleaning.
7. Subplot (2,0) is a scatter plot showing the correlation between age and glucose which is a positive relationship at around 0.34.
8. Subplot (2,1) shows the correlation between glucose and BMI, a weak positive correlation at 0.21, grouped by outcomes through color. Diabetic patients visually have higher glucose overall, but there is no notable difference between BMI for diabetic and non-diabetic patients.
9. Pie chart (2,2) shows the portion of diabetic to non-diabetic patients, about 1/3 to 2/3. Here we established a python list of colors for the pie chart


## Limitations ## 
This project was done with the sole intent of demonstrating Pandas' and Matplotlib's ability to be used for data analysis. Whether the results are scientifically conclusive was not taken into account. Furtheremore, there was clear selection bias because most entries containing zero values where impossible were removed, thus nearly half the entries were gone. This will be a point of focus in my upcoming projects. 




