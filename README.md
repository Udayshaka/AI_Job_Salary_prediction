# AI Job Salary Prediction

This project uses Machine Learning to predict job salaries based on different job-related features. It follows an end-to-end Machine Learning workflow, including data cleaning, exploratory data analysis, feature engineering, preprocessing, model training, and evaluation.

## Project Objective

The objective of this project is to build a regression model that can estimate the expected salary based on available job-related information.

## Technologies Used

Python, Pandas, NumPy, Matplotlib, Seaborn, Scikit-learn, and Jupyter Notebook.

## Machine Learning Workflow

The project follows these steps:

1. Data Collection
2. Data Cleaning and Preprocessing
3. Exploratory Data Analysis (EDA)
4. Train-Test Split
5. Feature Scaling
6. Model Training
7. Model Evaluation
8. Hyper Parameter Tuning

## Model

I used **Linear Regression** as the Machine Learning model.

The model was implemented using a Scikit-learn Pipeline, which combines preprocessing and model training:

```python
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LinearRegression

model = Pipeline(steps=[
    ("preprocessor", preprocessor),
    ("regressor", LinearRegression())
])
```

## Model Performance

The Linear Regression model was evaluated using **MAE, RMSE, and R² Score**.

| Metric | Score |
|---|---:|
| R² Score | 0.8320 |
| MAE | 18,095.39 |
| RMSE | 24,751.79 |

- **R² Score:** The model explains approximately **83.2% of the variance** in the target salary.
- **MAE:** Represents the average absolute difference between actual and predicted salary.
- **RMSE:** Represents the prediction error and gives more weight to larger errors.

> **Note:** Salary predictions are estimates and should not be considered actual or guaranteed salary offers. Actual salaries may vary depending on experience, location, company, skills, industry, and market conditions.

## Future Improvements

- Try additional regression models
- Perform hyperparameter tuning
- Improve feature engineering
- Compare models using MAE, RMSE, and R²

## Author

**Shaka Uday**


