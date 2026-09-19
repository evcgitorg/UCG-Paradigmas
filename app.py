import streamlit as st
import libreria_funciones as lf



st.title("Paradigmas de la programación")

st.sidebar.image("UCGlogo.png")

st.sidebar.title("Parámetros")

st.write("Elaborado por Enrique Villalta")

capital = st.number_input("Ingrese el capital: ", value = 1000)
tasa_anual_pct = st.number_input("Ingrese tasa anual: ", value = 0.15)
dias_mora = st.number_input("Ingrse los días de mora: ", value = 30)

resultado = lf.calcular_interes_mora(capital,tasa_anual_pct,dias_mora)

st.write("El resultado por atraso es: ",resultado)
