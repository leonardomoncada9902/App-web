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

col1, col2 = st.columns(2)

with col1:

    option = st.selectbox(
        "Mostrar autos ofertados:",
        ("Ultimos 30 dias", "Ultimos 90 dias", "Ultimos 180 dias", "Todos"),
    )

with col2: 

    sort = st.radio(
        "Ordena la lista",
        ["Orden ascendente", "Orden descendente", "Aleatorio"],
        key="visibility")
    
if sort == 'Orden ascendente':

    if option == "Ultimos 30 dias":
        st.write(df.query('days_listed <=30').sort_values(by='days_listed', ascending=True))

    elif option == "Ultimos 90 dias":
        st.write(df.query('days_listed <=90').sort_values(by='days_listed', ascending=True))

    elif option == "Ultimos 180 dias":
        st.write(df.query('days_listed <=180').sort_values(by='days_listed', ascending=True))

    elif option == "Todos":
        st.write(df.sort_values(by='days_listed', ascending=True))


elif sort == 'Orden descendente':

    if option == "Ultimos 30 dias":
        st.write(df.query('days_listed <=30').sort_values(by='days_listed', ascending=False))

    elif option == "Ultimos 90 dias":
        st.write(df.query('days_listed <=90').sort_values(by='days_listed', ascending=False))

    elif option == "Ultimos 180 dias":
        st.write(df.query('days_listed <=180').sort_values(by='days_listed', ascending=False))

    elif option == "Todos":
        st.write(df.sort_values(by='days_listed', ascending=False))

elif sort == 'Aleatorio':

    if option == "Ultimos 30 dias":
        st.write(df.query('days_listed <=30'))

    elif option == "Ultimos 90 dias":
        st.write(df.query('days_listed <=90'))

    elif option == "Ultimos 180 dias":
        st.write(df.query('days_listed <=180'))

    elif option == "Todos":
        st.write(df)









