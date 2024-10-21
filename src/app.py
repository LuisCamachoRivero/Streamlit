# your code here
from pickle import load
import streamlit as st

model = load(open('../models/decission_tree_classifier_42_pca.sav','rb'))
pca = load(open('../models/pca_4.sav','rb'))

st.title('Prediction Exam Score')

#'Hours_Studied', 'Attendance', 'Sleep_Hours', 'Previous_Scores',
#'Tutoring_Sessions', 'Physical_Activity', 'Teacher_Quality_num',
#'Gender_num', 'Extracurricular_Activities_num',
#'Parental_Education_Level_num', 'Parental_Involvement_num',
#'Learning_Disabilities_num', 'Peer_Influence_num',
#'School_Type_num', 'Family_Income_num', 'Distance_from_Home_num',
#'Access_to_Resources_num', 'Motivation_Level_num',
#'Internet_Access_num'

horas_estudio = st.slider('Hours Studied', min_value=0, max_value=44, step=1)
asistencia = st.slider('Attendance', min_value=60, max_value=100, step=1)
horas_sueno = st.slider('Sleep Hours', min_value=4, max_value=10, step=1)
nota_previa = st.slider('Previous Score', min_value=50, max_value=100, step=5)
tutoria = st.slider('Tutoring Sessions', min_value=0, max_value=9, step=1)
act_fisica = st.slider('Physical Activity (hours)', min_value=0, max_value=6, step=1)
calidad_profe = 