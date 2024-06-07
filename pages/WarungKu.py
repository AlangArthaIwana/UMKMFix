import streamlit as st
import numpy as np
import joblib

def make_prediction(input_data):
     model_path = 'model-training/random_forest_model.pkl'
     model = joblib.load(model_path)
     prediction = model.predict(input_data)
     return prediction

def get_prediction_label(prediction):
    if prediction[0] == 0:
        return "Average"
    elif prediction[0] == 1:
        return "High"
    elif prediction[0] == 2:
        return "Low"
    else:
        return "Unknown"

def display_profile_data(nama_pemilik, nama_usaha, age, gender, income, education, marital_Status, number_of_Children, home_Ownership, prediction):
    # Tampilkan
    prediction_label = get_prediction_label(prediction)
    st.write(f'Halo! **{nama_pemilik}** berikut ada data diri Anda.')  
    st.write(f'Nama Usaha: **{nama_usaha}**')
    st.write(f'Umur: **{age}** tahun')
    st.write(f'Jenis Kelamin: **{gender}**')
    st.write(f'Pendapatan Bulanan: **{income}**')
    st.write(f'Pendidikan: **{education}**')
    st.write(f'Status Pernikahan: **{marital_Status}**')
    st.write(f'Jumlah Pegawai: **{number_of_Children}**')
    st.write(f'Status Kepemilikan: **{home_Ownership}**')
    st.write(f'Skor Kredit: **{prediction_label}**')

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

st.write("**WarungKu**")

st.markdown("<h1 style='text-align: center; font-size: 25px;'>Profil UMKM</h1>", unsafe_allow_html=True)
cols = st.columns([1.5,1,1.5])
with cols[1]:
    st.image('pictures/user.jpg', width=250)
    uploaded_files = st.file_uploader("Upload Photo", accept_multiple_files=True)
    for uploaded_file in uploaded_files:
            bytes_data = uploaded_file.read()
            st.write("filename:", uploaded_file.name)
            st.write(bytes_data)
with st.form("my_form"):
        nama_pemilik = st.text_input("Nama Pemilik")
        nama_usaha = st.text_input("Nama Usaha")
        age = st.number_input('Umur', min_value=0, max_value=120)
        gender = st.selectbox("Jenis Kelamin (laki-laki=1, perempuan=0)",(1,0))
        income = st.number_input("Pendapatan Bulanan", min_value=1, max_value=100000000)
        education = st.text_input("Pendidikan")
        marital_Status = st.text_input("Status Pernikahan (single=1, married=0)")
        number_of_Children = st.number_input('Jumlah Pegawai', min_value=0, max_value=120)
        home_Ownership = st.text_input("Status Kepemilikan (Owner=0, Rented=1)")
        submitted = st.form_submit_button("Submit")
if submitted:
    # Prepare the input data
    input_data = np.array([[age, gender, income, education, marital_Status, number_of_Children, home_Ownership]])
    prediction = make_prediction(input_data)
    display_profile_data(nama_pemilik, nama_usaha, age, gender, income, education, marital_Status, number_of_Children, home_Ownership, prediction)
   

st.divider()
st.markdown("<h1 style='text-align: center; font-size: 15px; font-weight: normal;'>Copyright © 2024 UMKMPriority. All rights reserved.</h1>", unsafe_allow_html=True)