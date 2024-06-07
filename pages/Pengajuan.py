import streamlit as st

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

st.write("**Pengajuan**")

st.markdown("<h1 style='text-align: center; font-size: 30px;'>Data Pengajuan</h1>", unsafe_allow_html=True)
cols = st.columns([1,2])
with cols[0]:
    st.image('pictures/user.jpg', width=300)    
with cols[1]:
    with st.form("my_form"):
        nama_pemilik = st.text_input("Nama Pemilik")
        nama_usaha = st.text_input("Nama Usaha")
        d = st.date_input("Didirikan pada Tahun", value=None)
        deskripsi = st.text_input("Deskripsi Usaha")
        pinjaman = st.number_input("Jumlah Pinjaman", min_value=1, max_value=100000000)
        uploaded_files = st.file_uploader("Dokumen Jaminan", accept_multiple_files=True)
        for uploaded_file in uploaded_files:
            bytes_data = uploaded_file.read()
            st.write("filename:", uploaded_file.name)
            st.write(bytes_data)
        ajukan = st.form_submit_button("Ajukan")

if ajukan:
    st.write("**Berikut keterangan pengajuan Anda. Mohon tunggu balasan dari penyedia jasa keuangan.**")
    st.write("Nama Pemilik : ", nama_pemilik)
    st.write("Nama Usaha : ", nama_usaha)
    st.write("Didirikan pada Tahun : ", d)
    st.write("Deskripsi Usaha : ", deskripsi)
    st.write("Jumlah Pinjaman : ", pinjaman)
st.divider()
st.markdown("<h1 style='text-align: center; font-size: 15px; font-weight: normal;'>Copyright © 2024 UMKMPriority. All rights reserved.</h1>", unsafe_allow_html=True)