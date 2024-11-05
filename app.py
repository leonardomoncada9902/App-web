import streamlit as st
import pandas as pd
import plotly.express as px

# Lectura de los datos del dataframe 

url = 'https://practicum-content.s3.us-west-1.amazonaws.com/new-markets/Data_sprint_4_Refactored/vehicles_us.csv'

df = pd.read_csv(url)

# Creacion de encabezado de app web

st.header('Bienvenido a mi primera app web 	:bulb:')

st.write('Tabla de autos ofertados en los ultimos 270 dias.')

# Creacion de columnas para seleccion de formato de tabla

col1, col2 = st.columns(2)

with col1: # Columna 1

    # Creacion de selector de numero de dias

    option = st.selectbox(
        "Mostrar autos ofertados:",
        ("Ultimos 30 dias", "Ultimos 90 dias", "Ultimos 180 dias", "Todos"),
    )

with col2: # Columna 2

    # Configuracion de orden de la tabla

    sort = st.radio(
        "Ordena la lista",
        ["Orden ascendente", "Orden descendente", "Aleatorio"],
        key="visibility")
    
# Implementacion de opciones en la columnas 1 y 2 
    
if sort == 'Orden ascendente': # Orden ascendente

    if option == "Ultimos 30 dias": # Fitrado de df en valores de la columna 'days_listed' en valores entre 0 y 30 en orden ascendente
        st.write(df.query('days_listed <=30').sort_values(by='days_listed', ascending=True)) 

    elif option == "Ultimos 90 dias": # Fitrado de df en valores de la columna 'days_listed' en valores entre 0 y 90 en orden ascendente
        st.write(df.query('days_listed <=90').sort_values(by='days_listed', ascending=True))

    elif option == "Ultimos 180 dias": # Fitrado de df en valores de la columna 'days_listed' en valores entre 0 y 180 en orden ascendente
        st.write(df.query('days_listed <=180').sort_values(by='days_listed', ascending=True))

    elif option == "Todos": # Ordenamiento de los valores de dt sobre la columna 'days_listed' en orden ascendente
        st.write(df.sort_values(by='days_listed', ascending=True))


elif sort == 'Orden descendente': # Orden descendente

    if option == "Ultimos 30 dias": # Fitrado de df en valores de la columna 'days_listed' en valores entre 0 y 30 en orden descendente
        st.write(df.query('days_listed <=30').sort_values(by='days_listed', ascending=False))

    elif option == "Ultimos 90 dias": # Fitrado de df en valores de la columna 'days_listed' en valores entre 0 y 90 en orden descendente
        st.write(df.query('days_listed <=90').sort_values(by='days_listed', ascending=False))

    elif option == "Ultimos 180 dias": # Fitrado de df en valores de la columna 'days_listed' en valores entre 0 y 180 en orden descendente
        st.write(df.query('days_listed <=180').sort_values(by='days_listed', ascending=False))

    elif option == "Todos": # Ordenamiento de los valores de dt sobre la columna 'days_listed' en orden descendente
        st.write(df.sort_values(by='days_listed', ascending=False))

elif sort == 'Aleatorio': # Orden aleatorio

    if option == "Ultimos 30 dias": # Fitrado de df en valores de la columna 'days_listed' en valores entre 0 y 30 en orden aleatorio
        st.write(df.query('days_listed <=30'))

    elif option == "Ultimos 90 dias": # Fitrado de df en valores de la columna 'days_listed' en valores entre 0 y 90 en orden aleatorio
        st.write(df.query('days_listed <=90'))

    elif option == "Ultimos 180 dias": # Fitrado de df en valores de la columna 'days_listed' en valores entre 0 y 180 en orden aleatorio
        st.write(df.query('days_listed <=180'))

    elif option == "Todos": # Impresion de df sin modificar 
        st.write(df)


st.write('Comparacion del tipo de combustible usado por vehiculo. :fuelpump:')

# Impresion de histograma de los datos de la columna 'fuel'

fig1 = px.histogram(df, x="fuel", text_auto=True).update_xaxes(categoryorder='total descending')
st.plotly_chart(fig1, use_container_width=True)

st.write('Grafico de dispercion en relacion al precio y el modelo del vehiculo. :heavy_dollar_sign:')

# Impresion de grafico de dispercion de los datos de la columna 'price' y 'model_year'

fig2 = px.scatter(df, x="price", y="model_year",color="model_year")
st.plotly_chart(fig2, use_container_width=True)

st.write('Histograma del precio comparado con la condicion del automovil. :money_with_wings:')

# Impresion de histograma de los datos de la columna 'price' comparado con la columna 'condition'

fig3 = px.histogram(df, x="price", color="condition")
st.plotly_chart(fig3, use_container_width=True)

# Creacion de tabla dinamica de df con base a columnas 'type' y 'model'

df_t = df.pivot_table(index=['type'],
                            values='model',
                            aggfunc='count').reset_index()

# Creacion de tabla dinamica de df filtrado en 'model_year' datos solo de 2010 en adelante con base a columnas 'type' y 'model'

df_tr = df.query('model_year >= 2010').pivot_table(index=['type'],
                            values='model',
                            aggfunc='count').reset_index()

# Implementacion de casilla 

st.write('Grafico de dispercion con relacion al año del vehiclo y el tipo. :racing_car:')

modern = st.checkbox("Solo autos modernos (2010 en delante)")

if modern: # Si modern es seleccionado muestra grafica de datos filtrados de 'df_tr'
    
    fig4 = px.scatter(df_tr, x="model", y="type",
                size="model", color="type",
                    hover_name="type", log_x=True, size_max=60)
    st.plotly_chart(fig4, use_container_width=True)

else: # Si modern no es seleccionado muestra grafica de datos de 'df_t'

    fig5 = px.scatter(df_t, x="model", y="type",
                size="model", color="type",
                    hover_name="type", log_x=True, size_max=60)
    st.plotly_chart(fig5, use_container_width=True)








