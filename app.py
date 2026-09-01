import streamlit as st
import pandas as pd
import pickle


# --------------------------------------------------
# Load trained pipeline
# --------------------------------------------------

with open("salary_model.pkl", "rb") as f:
    model = pickle.load(f)


# --------------------------------------------------
# Page configuration
# --------------------------------------------------

st.set_page_config(
    page_title="AI Job Salary Prediction",
    page_icon="💰",
    layout="centered"
)


# --------------------------------------------------
# Title
# --------------------------------------------------

st.title("💰 AI Job Salary Prediction")

st.write(
    "Enter the job details below to estimate the expected salary."
)


# --------------------------------------------------
# Get categories from the fitted pipeline
# --------------------------------------------------

preprocessor = model.named_steps["preprocessor"]

ordinal_encoder = preprocessor.named_transformers_["ordinal"]
onehot_encoder = preprocessor.named_transformers_["nominal"]

ordinal_categories = ordinal_encoder.categories_
nominal_categories = onehot_encoder.categories_


# Ordinal columns
ordinal_cols = [
    "experience_level",
    "company_size"
]

# Nominal columns
nominal_cols = [
    "job_title",
    "employment_type",
    "company_location",
    "employee_residence",
    "education_required",
    "industry"
]


# Create dictionaries of available categories
ordinal_options = dict(
    zip(ordinal_cols, ordinal_categories)
)

nominal_options = dict(
    zip(nominal_cols, nominal_categories)
)


# --------------------------------------------------
# User Inputs
# --------------------------------------------------

st.subheader("Job Information")


job_title = st.selectbox(
    "Job Title",
    nominal_options["job_title"]
)


experience_level = st.selectbox(
    "Experience Level",
    ordinal_options["experience_level"]
)


employment_type = st.selectbox(
    "Employment Type",
    nominal_options["employment_type"]
)


company_location = st.selectbox(
    "Company Location",
    nominal_options["company_location"]
)


company_size = st.selectbox(
    "Company Size",
    ordinal_options["company_size"]
)


employee_residence = st.selectbox(
    "Employee Residence",
    nominal_options["employee_residence"]
)


education_required = st.selectbox(
    "Education Required",
    nominal_options["education_required"]
)


years_experience = st.number_input(
    "Years of Experience",
    min_value=0,
    max_value=50,
    value=2,
    step=1
)


industry = st.selectbox(
    "Industry",
    nominal_options["industry"]
)


number_of_skills = st.number_input(
    "Number of Skills",
    min_value=1,
    max_value=20,
    value=4,
    step=1
)


# --------------------------------------------------
# Prediction
# --------------------------------------------------

if st.button("Predict Salary", type="primary"):

    input_data = pd.DataFrame({
        "job_title": [job_title],
        "experience_level": [experience_level],
        "employment_type": [employment_type],
        "company_location": [company_location],
        "company_size": [company_size],
        "employee_residence": [employee_residence],
        "education_required": [education_required],
        "years_experience": [years_experience],
        "industry": [industry],
        "number_of_skills": [number_of_skills]
    })


    # Prediction
    prediction = model.predict(input_data)[0]


    # --------------------------------------------------
    # Display result
    # --------------------------------------------------

    st.success(
        f"### Estimated Salary: ${prediction:,.2f} USD"
    )

    st.info(
        "This prediction is an estimate based on the job details provided."
    )