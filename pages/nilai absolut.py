import streamlit as st
import pandas as pd
import numpy as np
import math

st.title("Konversi nilai decibel (dB) ke absolut")
st.write("---")
st.header("Konversi nilai rasio arus ke absolut")
X = st.number_input("Masukkan nilai rasio arus (dB) = ")
hitung1 = st.button("Hitung nilai absolut rasio arus")
if hitung1:
    A = math.pow(10, X/20)
    st.write("Nilai absolut =",A ,"kali")
st.write("---")
st.header("Konversi nilai rasio daya ke absolut")
Y = st.number_input("Masukkan nilai rasio daya (dB) = ")
hitung2 = st.button("Hitung nilai absolut rasio daya")
if hitung2:
    B = math.pow(10, Y/10)
    st.write("Nilai absolut =",B ,"kali")
st.write("---")
st.header("Konversi nilai rasio tegangan ke absolut")
Z = st.number_input("Masukkan nilai rasio tegangan (dB) = ")
hitung3 = st.button("Hitung nilai absolut rasio tegangan")
if hitung3:
    C = math.pow(10, Z/20)
    st.write("Nilai absolut =",C ,"kali")
