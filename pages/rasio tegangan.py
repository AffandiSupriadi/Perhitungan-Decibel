import streamlit as st
import pandas as pd
import numpy as np
import math

st.title("Perhitungan rasio tegangan")
st.image("tegangangambar.jpg", width=400)
V1 = st.number_input ("Masukkan nilai tegangan input (volt) = ")
V2 = st.number_input ("Masukkan nilai tegangan output (volt) = ")
hitung = st.button ("Hitung Rasio tegangan")
if hitung:
        rasio_tegangan = 20 * (math.log10(V2/V1))
        print = rasio_tegangan
        if rasio_tegangan > 0 :
            A = math.pow(10, rasio_tegangan/20)
            st.write("Tejadi penguatan (gain) sinyal output dengan nilai absolut",A ,"kali dari sinyal input")
        elif rasio_tegangan < 0 :
            A = math.pow(10, rasio_tegangan/20)
            st.write("Terjadi redaman (loss) sinyal output dengan nilai absolut",A ,"kali dari sinyal input")
        st.write("Nilai rasio tegangan adalah",print ,"dB")