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
