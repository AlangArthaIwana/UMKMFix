import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

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
        st.switch_page("pages/WarungKU.py")
with cols[6]:
    if st.button("Pengaturan"):
        st.switch_page("pages/Pengaturan.py")
st.divider()

st.write("**myCashFlow**")

# cols = st.columns([1,50,1])
# with cols[1]:
#     st.image('pictures/bgdepan.jpg', width=1100)
st.markdown("<h1 style='text-align: center; font-size: 30px;'>Analisis Tahun 2024</h1>", unsafe_allow_html=True)
chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])
st.bar_chart(chart_data)
    
cols = st.columns([1,0.7])
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
    st.write('**Income**')
    # Data 
    months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    income = [5000, 6000, 5500, 7000, 7500, 8000, 8500, 9000, 9500, 10000, 10500, 11000]
    # process
    fig, ax = plt.subplots(figsize=(8, 4))
    ax.bar(months, income, color='skyblue')  # Use bar() for vertical bars
    ax.set_xlabel('Months')
    ax.set_ylabel('Income ($)')
    ax.set_title('Income per Month')
    plt.xticks(rotation=45)
    st.pyplot(fig)

    st.write('**Riwayat Kredit**')
    # Data 
    months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    income = [5000, 6000, 5500, 7000, 7500, 8000, 8500, 9000, 9500, 10000, 10500, 11000]
    # process
    fig, ax = plt.subplots(figsize=(8, 4))
    ax.bar(months, income, color='skyblue')  # Use bar() for vertical bars
    ax.set_xlabel('Months')
    ax.set_ylabel('Income ($)')
    ax.set_title('Income per Month')
    plt.xticks(rotation=45)
    st.pyplot(fig)

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