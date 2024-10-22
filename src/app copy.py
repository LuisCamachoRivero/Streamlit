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

act_extra_num = int(act_extra)

involucramiento_parental = st.radio("Parental Involvement", ["Low", "Mid", "High"])
tipo_escuela = st.radio("School Type", ["Public", "Private"])
nivel_educ_padres = st.radio("Parental Education Level", ["Mid", "Bachelor", "University", "None"])
influencia = st.radio("Peer Influence", ["Positive", "Negative", "Neutral"])

# Mapping categorical values to numbers
env_parental_num = env_parental_dict[involucramiento_parental]
tipo_escuela_num = tipo_escuela_dict[tipo_escuela]
nivel_educ_padres_num = nivel_educ_padres_dic[nivel_educ_padres]
influencia_num = influencia_dic[influencia]

if st.button('Predict'):
    # Create input array for PCA
    input_data = np.array([
        horas_estudio,
        asistencia,
        horas_sueno,
        nota_previa,
        tutoria,
        act_fisica,
        act_extra_num,
        env_parental_num,
        tipo_escuela_num,
        nivel_educ_padres_num,
        influencia_num
    ]).reshape(1, -1)

    # Transform the input data using PCA
    conversion_pca = pca.transform(input_data)

    # Make prediction
    prediction = model.predict(conversion_pca)

    # Display the result
    st.write(f'Predicted Exam Score: {prediction[0]}')