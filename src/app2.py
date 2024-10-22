from pickle import load
import streamlit as st

# Cargar el modelo y PCA
model = load(open('/workspaces/Streamlit/models/decission_tree_classifier_42_pca.sav', 'rb'))
pca = load(open('/workspaces/Streamlit/models/pcs_4.sav', 'rb'))

st.title('Prediction Exam Score')

# Entradas del usuario
horas_estudio = st.slider('Hours Studied', min_value=0, max_value=44, step=1)
asistencia = st.slider('Attendance', min_value=60, max_value=100, step=1)
horas_sueno = st.slider('Sleep Hours', min_value=4, max_value=10, step=1)
nota_previa = st.slider('Previous Score', min_value=50, max_value=100, step=5)
tutoria = st.slider('Tutoring Sessions', min_value=0, max_value=9, step=1)
act_fisica = st.slider('Physical Activity (hours)', min_value=0, max_value=6, step=1)
act_extra = st.toggle('Extracurricular Activities')

involucramiento_parental = st.radio("Parental Involvement", ["Low", "Mid", "High"])
tipo_escuela = st.radio("School Type", ["Public", "Private"])
nivel_educ_padres = st.radio("Parental Education Level", ["Mid", "Bachelor", "University", "None"])
influencia = st.radio("Peer Influence", ["Positive", "Negative", "Neutral"])

# Diccionarios para conversión
inv_parental_dict = {'Low': 0, 'Mid': 1, 'High': 2}
tipo_escuela_dict = {'Public': 0, 'Private': 1}
nivel_educ_padres_dict = {'Mid': 0, 'Bachelor': 1, 'University': 2, 'None': -1}
influencia_dict = {'Positive': 0, 'Negative': 1, 'Neutral': 2}

if st.button('Prediction'):
    # Convertir entradas
    conversion_pca = pca.transform([[
        horas_estudio,
        asistencia,
        horas_sueno,
        nota_previa,
        tutoria,
        act_fisica,
        0,  # Teacher_Quality
        0,  # Gender
        1 if act_extra else 0,  # Convertir Booleano a int
        nivel_educ_padres_dict[nivel_educ_padres],
        inv_parental_dict[involucramiento_parental],
        0,  # Learning Disabilities
        influencia_dict[influencia],
        tipo_escuela_dict[tipo_escuela],
        0,  # Family Income
        0,  # Distance from Home
        0,  # Access to Resources
        0,  # Motivation Level
        0   # Internet Access
    ]])
    
    # Realizar la predicción
    prediction = model.predict(conversion_pca)
    
    # Mostrar el resultado
    st.write(f'Predicted Exam Score: {prediction[0]}')


    #'Hours_Studied', 'Attendance', 'Sleep_Hours', 'Previous_Scores',
    #  'Tutoring_Sessions', 'Physical_Activity', 'Teacher_Quality_num',
    #   'Gender_num', 'Extracurricular_Activities_num',
    #   'Parental_Education_Level_num', 'Parental_Involvement_num',
    #   'Learning_Disabilities_num', 'Peer_Influence_num', 'School_Type_num',
    #  'Family_Income_num', 'Distance_from_Home_num',
    #   'Access_to_Resources_num', 'Motivation_Level_num',
    #   'Internet_Access_num'