import streamlit as st
import pandas as pd
import numpy as np
import math

st.title ("Perhitungan rasio daya")
st.image ("dayagambar.jpg", width=400)
P1 = st.number_input ("Masukkan nilai daya input (watt) = ")
P2 = st.number_input ("Masukkan nilai daya output (watt) = ")
hitung = st.button ("Hitung Rasio daya")
if hitung:
        rasio_daya = 10 * (math.log10(P2/P1))
        print = rasio_daya
        if rasio_daya > 0 :
            A = math.pow(10, rasio_daya/10)
            st.write("Terjadi penguatan (gain) sinyal output dengan nilai absolut",A ,"kali dari sinyal input")
        elif rasio_daya < 0 :
            A = math.pow(10, rasio_daya/10)
            st.write("Terjadi redaman (loss) sinyal output dengan nilai absolut",A ,"kali dari sinyal input")
        st.write("Nilai rasio daya adalah", print, "dB")
