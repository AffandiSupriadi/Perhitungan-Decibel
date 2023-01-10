import streamlit as st
import pandas as pd
import numpy as np
import math


st.title ("Perhitungan rasio arus")
st.image ("arusgambar.jpg", width=400)
I1 = st.number_input ("Masukkan nilai arus input (ampere) = ")
I2 = st.number_input ("Masukkan nilai arus output (ampere) = ")
hitung = st.button ("Hitung Rasio arus")
if hitung:
        rasio_arus = 20 * (math.log10(I2/I1))
        print = rasio_arus
        if rasio_arus > 0 :
            A = math.pow(10, rasio_arus/20)
            st.write("Terjadi penguatan (gain) sinyal output dengan nilai absolut",A ,"kali dari sinyal input")
        elif rasio_arus < 0 :
            A = math.pow(10, rasio_arus/20)
            st.write("Terjadi redaman (loss) sinyal output dengan nilai absolut",A ,"kali dari sinyal input")
        st.write("Nilai rasio arus adalah", print, "dB")