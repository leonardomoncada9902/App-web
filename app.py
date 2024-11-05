import streamlit as st
import pandas as pd
import plotly.express as px

# Lectura de los datos del dataframe 

url = 'https://practicum-content.s3.us-west-1.amazonaws.com/new-markets/Data_sprint_4_Refactored/vehicles_us.csv'

df = pd.read_csv(url)

# Creacion de encabezado de app web

st.header('Bienvenido a mi primera app web 	:bulb:')

st.write('Tabla de autos ofertados en los ultimos 270 dias.')

# Impresion de dataset en la app web

option = st.selectbox(
    "Mostrar autos ofertados:",
    ("Ultimos 30 dias", "Ultimos 90 dias", "Ultimos 180 dias", "Todos"),
)

if option == "Ultimos 30 dias":
    st.write(df.query('days_listed <=30'))

elif option == "Ultimos 90 dias":
    st.write(df.query('days_listed <=90'))

elif option == "Ultimos 180 dias":
    st.write(df.query('days_listed <=180'))

elif option == "Todos":
    st.write(df)








