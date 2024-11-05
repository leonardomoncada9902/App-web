import streamlit as st
import pandas as pd
import plotly.express as px

# Lectura de los datos del dataframe 

df = pd.read_csv('/Users/leonardo/Documents/Python/Herramientas-de-desarrollo-software/App-web/vehicles_us.csv')

# Creacion de encabezado de app web

st.header('Bienvenido a mi primera app web 	:bulb:')

st.write('Este es el dataframe que analizaremos:')

# Impresion de dataset en la app web

st.write(df)




