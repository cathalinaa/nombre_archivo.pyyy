# -*- coding: utf-8 -*-
import streamlit as st
import pandas as pd


# Título de la aplicación
st.title('Mi Primera Aplicación Web con Streamlit')
# Texto simple
st.write('Esta es una aplicación web de ejemplo utilizando Streamlit.')

# Título de la aplicación
st.title('Aplicación de Análisis de Datos')
# Cargar el archivo CSV
uploaded_file = st.file_uploader('Sube tu archivo CSV', type=['csv'])

if uploaded_file is not None:
    # Leer el archivo CSV usando Pandas
    df = pd.read_csv(uploaded_file)
    # Mostrar las primeras filas del archivo
    st.write('Primeras 5 filas del archivo:')
    st.write(df.head())

if uploaded_file is not None:
    # Leer el archivo CSV
    df = pd.read_csv(uploaded_file)
    
    # Mostrar la estructura del DataFrame
    st.write('Estructura del DataFrame:')
    st.write(df.describe())
    
    # Seleccionar una columna numérica para analizar
    col = st.selectbox('Selecciona una columna para filtrar', df.columns)
    
    # Filtrar datos según el valor de la columna
    valor_min = st.slider('Selecciona un valor mínimo',
float(df[col].min()), float(df[col].max()))
    df_filtrado = df[df[col] >= valor_min]
    
    # Mostrar los datos filtrados
    st.write(f'Datos filtrados donde {col} >= {valor_min}:')
    st.write(df_filtrado)
