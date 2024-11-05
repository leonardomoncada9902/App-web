import streamlit as st
import pandas as pd
import plotly.express as px

# Lectura de los datos del dataframe 

url = 'https://practicum-content.s3.us-west-1.amazonaws.com/new-markets/Data_sprint_4_Refactored/vehicles_us.csv'

df = pd.read_csv(url)

# Creacion de encabezado de app web

st.header('Bienvenido a mi primera app web 	:bulb:')

st.write('Este es el dataframe que analizaremos:')

# Impresion de dataset en la app web

st.write(df)




