import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

cols = st.columns([3,1.3,1,1.2,1.2,1.2,1.2,1])
with cols[0]:
    st.markdown("<h1 style='text-align: left; font-size: 15px;'>UMKMPriority</h1>", unsafe_allow_html=True)
with cols[2]:
    if st.button("Home"):
        st.switch_page("Home.py")
with cols[3]:
    if st.button("Pengajuan"):
        st.switch_page("pages/Pengajuan.py")
with cols[4]:
    if st.button("myCashflow"):
        st.switch_page("pages/MyCashFlow.py")
with cols[5]:
    if st.button("WarungKu"):
        st.switch_page("pages/WarungKu.py")
with cols[6]:
    if st.button("Pengaturan"):
        st.switch_page("pages/Pengaturan.py")
st.divider()

st.write("**myCashFlow**")

st.markdown("<h1 style='text-align: center; font-size: 30px;'>Analisis Tahun 2024</h1>", unsafe_allow_html=True)
# Read data from CSV
csv_file = 'data_umkm.csv'
if os.path.exists(csv_file):
    df = pd.read_csv(csv_file,sep=",",skipinitialspace=True)
else:
    st.error(f"Data file {csv_file} does not exist.")
    df = pd.DataFrame()  # Create an empty dataframe


if not df.empty:
    # Bar chart for monthly income
    st.write("### Pendapatan Bulanan")
    st.line_chart(df[['Income Update','Income']].set_index('Income Update'))

    cols = st.columns([1,1])
    with cols[0]:
        st.text('')
        st.write('**Persentase Resiko**')
        # data
        labels = ['Income', 'Riwayat Kredit', 'Data Pendukung', 'Keterampilan']
        sizes = [30, 12.5, 12.5, 20]
        colors = ['#ff9999','#66b3ff','#99ff99','#ffcc99']
        explode = (0.1, 0, 0, 0)  # explode the 1st slice (Income)
        # process
        fig, ax = plt.subplots()
        ax.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%',
                shadow=True, startangle=90)
        ax.axis('equal')
        st.pyplot(fig)
    with cols[1]:
        st.write("### Pendapatan Bulanan")
        st.bar_chart(df[['Age','Income']].set_index('Age'))

        # Pie chart for credit score distribution
        st.write("### Distribusi Skor Kredit")
        credit_score_counts = df['Credit Score'].value_counts()
        fig, ax = plt.subplots(figsize=(1, 1))  # Adjust the figsize to make the pie chart smaller
        ax.pie(credit_score_counts, labels=credit_score_counts.index, autopct='%1.1f%%', startangle=60, colors=['#ff9999', '#66b3ff', '#99ff99', '#ffcc99'])
        ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
        st.pyplot(fig)

else:
    st.write("No data available.")


st.markdown("<h1 style='text-align: center; font-size: 20px;'>Dokumentasi Pengajuan</h1>", unsafe_allow_html=True)
cols = st.columns([1,1,1])
with cols[0]:
    st.image('pictures/bgdepan.jpg')
with cols[1]:
    st.image('pictures/bgdepan.jpg')
with cols[2]:
    st.image('pictures/bgdepan.jpg')
st.divider()
st.markdown("<h1 style='text-align: center; font-size: 15px; font-weight: normal;'>Copyright © 2024 UMKMPriority. All rights reserved.</h1>", unsafe_allow_html=True)