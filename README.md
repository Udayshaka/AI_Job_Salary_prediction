# AI Job Salary Prediction

This project uses Machine Learning to predict job salaries based on different job-related features. It follows an end-to-end Machine Learning workflow, including data cleaning, exploratory data analysis, feature engineering, preprocessing, model training, and evaluation.

## Project Objective

The objective of this project is to build a regression model that can estimate the expected salary based on available job-related information and compare different regression algorithms based on their performance.

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

## 🤖 Models Used

Three regression models were trained and compared:

- Linear Regression
- Random Forest Regressor
- Gradient Boosting Regressor

All models were implemented using a Scikit-learn Pipeline with the same preprocessing steps.

The model was implemented using a Scikit-learn Pipeline, which combines preprocessing and model training:

## 📊 Model Performance

The models were evaluated using **MAE, RMSE, and R² Score**.

| Model | MAE | RMSE | R² Score |
|---|---:|---:|---:|
| Linear Regression | 18,100.15 | 24,749.81 | 0.8320 |
| Random Forest Regressor | 15,492.55 | 21,794.68 | 0.8698 |
| Gradient Boosting Regressor | 14,754.32 | 20,534.30 | 0.8844 |

### 📈 Evaluation Metrics

- **MAE (Mean Absolute Error):** Measures the average absolute difference between actual and predicted salaries. Lower values indicate smaller prediction errors.

- **RMSE (Root Mean Squared Error):** Measures the prediction error and gives more weight to larger errors. Lower values indicate better performance.

- **R² Score:** Measures how well the model explains the variance in the target salary. Higher values indicate better explanatory performance.

## 🔍 Model Comparison

The three regression models were compared using the same test dataset and evaluation metrics.

The **Gradient Boosting Regressor** achieved an R² score of **0.8844**, with an MAE of **14,754.32** and RMSE of **20,534.30**.

The comparison helped evaluate how different regression algorithms perform on the salary prediction problem.


> **Note:** Salary predictions are estimates and should not be considered actual or guaranteed salary offers. Actual salaries may vary depending on experience, location, company, skills, industry, and market conditions.

## Future Improvements

- Try additional regression models
- Perform hyperparameter tuning
- Improve feature engineering

## Author

**Shaka Uday**


