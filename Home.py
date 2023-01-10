import streamlit as st
import pandas as pd
import numpy as np
import math

st.set_page_config(
    page_title = "Decibel app",
    page_icon = "❤️",
)


col1, col2, col3 = st.columns(3)

with col2:
        st.image("download.png")

st.header("Perhitungan Menggunakan Decibel")
st.write("by: Affandi Supriadi")
st.write("Dosen: Ir. Rustamaji, M.T")
st.sidebar.success("pilih perhitungan yang anda inginkan")
st.write(
        "Saya Affandi Supriadi dengan NRP 11-2021-020 mempersembahkan Aplikasi web perhitungan menggunakan Decibel. Untuk memenuhi tugas dari mata kuliah Dasar Telekomunikasi. Silahkan klik tanda “>” disebelah kiri atas untuk memulai perhitungan."
    )
st.write("---")
st.subheader("Decibel")
st.write("Decibel (dB) adalah satuan yang sering digunakan sebagai skala penguatan dalam rangkaian elektronika seperti rangkaian pada peralatan komunikasi dan audio. Besaran yang menggunakan skala penguatan decibel tersebut diantaranya seperti penguatan pada daya, arus, dan tegangan. Pada dasarnya decibel adalah satuan yang menggambarkan suatu perbandingan/rasio. Decibel bisa disingkat menjadi “dB” ini bisa diartikan sebagai perbandingan antara dua besaran dalam skala logaritma.")
st.write("Umumnya desibel merupakan turunan dari besaran Bel, dimana 1 desibel sama dengan 1/10 Bel atau 0,1 Bel. Dalam prakteknya, para engineer atau fisikawan cenderung lebih nyaman menggunakan satuan Decibel (dB) daripada satuan Bel. Hal ini dikarenakan untuk menghindari kebanyakan angka dibelakang koma dalam menghitungnya. Dalam perhitungan decibel, gain/penguatan suatu sinyal akan ditandai dengan tanda “+” (positif), sedangkan pelemahan/loss akan ditandai dengan tanda “-” (negatif). Maka dengan demikian, jika sinyal output +6dB dari sinyal input maka hal ini menandakan terjadinya penguatan output sebanyak 6dB dari sinyal input. Sebaliknya jika sinyal output -2dB dari sinyal input yang artinya yaitu sudah terjadi pelemahan sinyal output sebanyak 2dB terhadap sinyal input.")
st.write("[akun instagram saya](https://www.instagram.com/affn_s/)")

st.write("---")
st.header("Rumus-rumus yang digunakan")

col1, col2, col3, col4 = st.columns(4)

with col1:
        st.subheader("Rumus rasio daya")
        st.image("dayalog.jpg")
with col2:
        st.subheader("Rumus rasio arus")
        st.image("arlog.jpg")
with col3:
        st.subheader("Rumus rasio tegangan")
        st.image("teglog.jpg")
    
st.write("---")