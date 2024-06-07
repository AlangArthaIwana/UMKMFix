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

st.write("**Pengaturan**")

cols = st.columns([1,4.5,1])
with cols[2]:
    on = st.toggle("Pemberitahuan")
    if on:
        st.write("Pemberitahuan Aktif!")
settings_options = {
    "Perbaharui Kontak Pribadi": ["Username", "Password", "No. Hp"],
    "Pilih Bahasa": ["Indonesia", "Inggris"],
    "Kebijakan Privasi": ["Kebijakan Privasi", "Baca Kebijakan Privasi"],
    "Syarat dan Ketentuan": ["Syarat dan Ketentuan", "Setuju", "Tidak Setuju"], 
    "Hubungi Kami": ["Hubungi Kami", "Informasi Kontak"],
}

# Define functions for setting actions (replace with actual implementation)
def update_contact_info(username, password, phone_number):
    # update informasi kontak di database
    pass

def change_language(language):
    # update bahasa
    pass

for setting_name, setting_options in settings_options.items():
    with st.expander(setting_name):
        if setting_name == "Perbaharui Kontak Pribadi":
            username = st.text_input("Username")
            password = st.text_input("Password", type="password")
            phone_number = st.text_input("No. Hp")
            if st.button("Simpan"):
                update_contact_info(username, password, phone_number)
        elif setting_name == "Pilih Bahasa":
            selected_language = st.selectbox("Pilih Bahasa", setting_options)
            if selected_language == "Inggris":
                # implementasikan logika untuk merubah bahasa
                pass  
        elif setting_name == "Kebijakan Privasi":
            st.write("**Isi Kebijakan Privasi UMKM Priority akan ditampilkan disini.**")
        elif setting_name == "Syarat dan Ketentuan":
            st.write("**Isi Syarat dan Ketentuan UMKM Priority akan ditampilkan disini.**")
            agree_to_terms = st.checkbox("Saya setuju dengan Syarat dan Ketentuan")
            if st.button("Setuju"):
                if agree_to_terms:
                    # implementasikan logika untuk persetujuan
                    pass  
                else:
                    st.warning("Anda harus menyetujui Syarat dan Ketentuan untuk melanjutkan.")
        elif setting_name == "Hubungi Kami":
            st.write("**Informasi kontak UMKM Priority akan ditampilkan disini.**")
        elif len(setting_options) == 2:
            if setting_options[1] == "Open in new tab":
                st.markdown(f"[Link]({setting_options[0]})", unsafe_allow_html=True)
            else:
                st.write(setting_options[0])
                # (e.g., update username, password, etc.)
        else:
            # (e.g., language selection)
            selected_option = st.selectbox("Pilih", setting_options)
            if selected_option == "Indonesia":
                change_language("Indonesia")
            elif selected_option == "Inggris":
                change_language("Inggris")
st.divider()
st.markdown("<h1 style='text-align: center; font-size: 15px; font-weight: normal;'>Copyright © 2024 UMKMPriority. All rights reserved.</h1>", unsafe_allow_html=True)