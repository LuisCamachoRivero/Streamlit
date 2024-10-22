# your code here
from pickle import load
import streamlit as st

model = load(open('/workspaces/Streamlit/models/decission_tree_classifier_42_pca.sav','rb'))
pca = load(open('/workspaces/Streamlit/models/pcs_4.sav','rb'))

st.title('Prediction Exam Score')

horas_estudio = st.slider('Hours Studied', min_value=0, max_value=44, step=1)
asistencia = st.slider('Attendance', min_value=60, max_value=100, step=1)
horas_sueno = st.slider('Sleep Hours', min_value=4, max_value=10, step=1)
nota_previa = st.slider('Previous Score', min_value=50, max_value=100, step=5)
tutoria = st.slider('Tutoring Sessions', min_value=0, max_value=9, step=1)
act_fisica = st.slider('Physical Activity (hours)', min_value=0, max_value=6, step=1)
act_extra = st.toggle('Extracurricular Activities')
if act_extra:
    st.write("Yes")
involucramiento_parental = st.radio(
    "Parental Involvement",
    ["Low", "Mid", "High"],
    index=None)
tipo_escuela = st.radio(
    "School Type",
    ["Public", "Private"],
    index=None)
nivel_educ_padres = st.radio(
    "Parental Education Level",
    ["Mid", "Bachelor", "University", "None"],
    index=None)
influencia = st.radio(
    "Peer Influence",
    ["Positive", "Negative", "Neutral"],
    index=None)
Family_income_num=0
Access_to_Resources_num=0
Motivation_Level_num=0
Distance_from_Home_num=0
Teacher_Quality_num=0
Internet_Access_num=0
Learning_Disabilities_num=0

inv_parental_dict = {'Low':0,
                     'Mid':1,
                     'High':2}

tipo_escuela_dict = {'Public':0,
                     'Private':1}

nivel_educ_padres_dic= {'Mid':0,
                        'Bachelor':1,
                        'University':2,
                        'None':-1}

influencia_dic = {'Positive':0,
                  'Negative':1,
                  'Neutral':2}

if st.button('Prediction'):
    conversion_pca = pca.transform([horas_estudio,asistencia,horas_sueno,nota_previa,tutoria,act_fisica,0,0,act_extra,
                                    nivel_educ_padres[inv_parental_dict],involucramiento_parental[inv_parental_dict],0,
                                    influencia[inv_parental_dict],tipo_escuela[inv_parental_dict],0,0,0,0,0
                                    ])

    prediction = model.predict(conversion_pca)
    
    st.write(f'Predicted Exam Score: {prediction[0]}')

"""'Hours_Studied', 'Attendance', 'Sleep_Hours', 'Previous_Scores',
       'Tutoring_Sessions', 'Physical_Activity', 'Teacher_Quality_num',
       'Gender_num', 'Extracurricular_Activities_num',
       'Parental_Education_Level_num', 'Parental_Involvement_num',
       'Learning_Disabilities_num', 'Peer_Influence_num', 'School_Type_num',
       'Family_Income_num', 'Distance_from_Home_num',
       'Access_to_Resources_num', 'Motivation_Level_num',
       'Internet_Access_num'"""