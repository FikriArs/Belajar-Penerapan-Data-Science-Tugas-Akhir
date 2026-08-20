import streamlit as st
import pandas as pd
import joblib

# Load the model
@st.cache_resource
def load_model():
    return joblib.load('model/rf_model.joblib')

model = load_model()

st.title("Jaya Jaya Institut: Student Dropout Prediction")
st.write("A prototype machine learning application to predict if a student will Graduate or Dropout.")

st.sidebar.header("Student Features Input")

# We will group features into categories for a cleaner UI
st.sidebar.subheader("Demographics & Background")
marital_status = st.sidebar.number_input("Marital Status", min_value=1, max_value=6, value=1)
nacionality = st.sidebar.number_input("Nacionality", min_value=1, value=1)
displaced = st.sidebar.selectbox("Displaced", [0, 1])
gender = st.sidebar.selectbox("Gender", [0, 1])
age = st.sidebar.number_input("Age at Enrollment", min_value=15, max_value=80, value=20)
international = st.sidebar.selectbox("International", [0, 1])

st.sidebar.subheader("Academic Info")
course = st.sidebar.number_input("Course", min_value=1, value=171)
prev_qual = st.sidebar.number_input("Previous Qualification", min_value=1, value=1)
prev_qual_grade = st.sidebar.number_input("Previous Qualification Grade", min_value=0.0, value=122.0)
admission_grade = st.sidebar.number_input("Admission Grade", min_value=0.0, value=127.3)
daytime_evening = st.sidebar.selectbox("Daytime/Evening Attendance", [0, 1])
app_mode = st.sidebar.number_input("Application Mode", min_value=1, value=1)
app_order = st.sidebar.number_input("Application Order", min_value=0, value=1)

st.sidebar.subheader("Financial & Social")
debtor = st.sidebar.selectbox("Debtor", [0, 1])
tuition_up_to_date = st.sidebar.selectbox("Tuition Fees Up to Date", [0, 1])
scholarship = st.sidebar.selectbox("Scholarship Holder", [0, 1])
edu_special_needs = st.sidebar.selectbox("Educational Special Needs", [0, 1])

st.sidebar.subheader("Parental Background")
mothers_qual = st.sidebar.number_input("Mother's Qualification", min_value=1, value=19)
fathers_qual = st.sidebar.number_input("Father's Qualification", min_value=1, value=12)
mothers_occ = st.sidebar.number_input("Mother's Occupation", min_value=1, value=5)
fathers_occ = st.sidebar.number_input("Father's Occupation", min_value=1, value=9)

st.sidebar.subheader("Curricular Units (1st Sem)")
cu_1_credited = st.sidebar.number_input("CU 1st Sem Credited", min_value=0, value=0)
cu_1_enrolled = st.sidebar.number_input("CU 1st Sem Enrolled", min_value=0, value=0)
cu_1_eval = st.sidebar.number_input("CU 1st Sem Evaluations", min_value=0, value=0)
cu_1_approved = st.sidebar.number_input("CU 1st Sem Approved", min_value=0, value=0)
cu_1_grade = st.sidebar.number_input("CU 1st Sem Grade", min_value=0.0, value=0.0)
cu_1_wo_eval = st.sidebar.number_input("CU 1st Sem W/O Evaluations", min_value=0, value=0)

st.sidebar.subheader("Curricular Units (2nd Sem)")
cu_2_credited = st.sidebar.number_input("CU 2nd Sem Credited", min_value=0, value=0)
cu_2_enrolled = st.sidebar.number_input("CU 2nd Sem Enrolled", min_value=0, value=0)
cu_2_eval = st.sidebar.number_input("CU 2nd Sem Evaluations", min_value=0, value=0)
cu_2_approved = st.sidebar.number_input("CU 2nd Sem Approved", min_value=0, value=0)
cu_2_grade = st.sidebar.number_input("CU 2nd Sem Grade", min_value=0.0, value=0.0)
cu_2_wo_eval = st.sidebar.number_input("CU 2nd Sem W/O Evaluations", min_value=0, value=0)

st.sidebar.subheader("Macroeconomic Factors")
unemployment = st.sidebar.number_input("Unemployment Rate", value=10.8)
inflation = st.sidebar.number_input("Inflation Rate", value=1.4)
gdp = st.sidebar.number_input("GDP", value=1.74)

# Create a dataframe for the input
input_data = pd.DataFrame([[
    marital_status, app_mode, app_order, course, daytime_evening, prev_qual, prev_qual_grade, nacionality,
    mothers_qual, fathers_qual, mothers_occ, fathers_occ, admission_grade, displaced, edu_special_needs,
    debtor, tuition_up_to_date, gender, scholarship, age, international, cu_1_credited, cu_1_enrolled,
    cu_1_eval, cu_1_approved, cu_1_grade, cu_1_wo_eval, cu_2_credited, cu_2_enrolled, cu_2_eval,
    cu_2_approved, cu_2_grade, cu_2_wo_eval, unemployment, inflation, gdp
]], columns=[
    'Marital_status', 'Application_mode', 'Application_order', 'Course', 'Daytime_evening_attendance', 
    'Previous_qualification', 'Previous_qualification_grade', 'Nacionality', 'Mothers_qualification', 
    'Fathers_qualification', 'Mothers_occupation', 'Fathers_occupation', 'Admission_grade', 'Displaced', 
    'Educational_special_needs', 'Debtor', 'Tuition_fees_up_to_date', 'Gender', 'Scholarship_holder', 
    'Age_at_enrollment', 'International', 'Curricular_units_1st_sem_credited', 'Curricular_units_1st_sem_enrolled', 
    'Curricular_units_1st_sem_evaluations', 'Curricular_units_1st_sem_approved', 'Curricular_units_1st_sem_grade', 
    'Curricular_units_1st_sem_without_evaluations', 'Curricular_units_2nd_sem_credited', 'Curricular_units_2nd_sem_enrolled', 
    'Curricular_units_2nd_sem_evaluations', 'Curricular_units_2nd_sem_approved', 'Curricular_units_2nd_sem_grade', 
    'Curricular_units_2nd_sem_without_evaluations', 'Unemployment_rate', 'Inflation_rate', 'GDP'
])

st.subheader("Predict Student Status")
if st.button("Predict"):
    prediction = model.predict(input_data)[0]
    
    if prediction == 0:
        st.error("Prediction: **Dropout**")
        st.write("This student is at high risk of dropping out. Consider immediate academic or financial counseling.")
    else:
        st.success("Prediction: **Graduate**")
        st.write("This student is on track to graduate.")
