import streamlit as st

cols = st.columns([2,1.2,1,1.2,1.2,1.2,1.2,1.5])
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
with cols[7]:
    if st.button("Masuk/Daftar"):
        st.switch_page("pages/daftar.py")
st.divider()

cols = st.columns([1,50,1])
with cols[1]:
    st.image('pictures/bgdepan.jpg', width=1100)
st.divider()
st.markdown("<h1 style='text-align: center; font-size: 25px;'>UMKM PRIORITY</h1>", unsafe_allow_html=True)

cols = st.columns([3,2])
with cols[0]:
    st.markdown("<h1 style='text-align: left; font-size: 20px;'>Apa itu UMKM Priority?</h1>", unsafe_allow_html=True)
    st.write("<h1 style='text-align: justify; font-size: 15px; font-weight: normal; '>UMKM PRIORITY adalah sebuah aplikasi yang dirancang khusus untuk memberikan solusi terhadap tantangan akses terbatas ke pendanaan yang dihadapi oleh Usaha Mikro, Kecil, dan Menengah (UMKM). Aplikasi ini bertujuan untuk memberikan akses mudah dan cepat kepada UMKM untuk mendapatkan sumber pendanaan yang memadai, yang seringkali sulit diperoleh dari bank dan lembaga keuangan tradisional.</h1>", unsafe_allow_html=True)
    with cols[1]:
        st.image('pictures/Depan1.jpg', width=400)
st.write(
            """
            <div style='background-color: lightblue; padding: 10px; border-radius: 10px;'>
            <h1 style='text-align: center; font-size: 15px; font-weight: bold;'>Berkolaborasi dengan :</h1>
            </div>
            """, 
            unsafe_allow_html=True
        )
st.text('')
st.text('')
st.markdown("<h1 style='text-align: center; font-size: 25px;'>Apa kata mereka?</h1>", unsafe_allow_html=True)
cols = st.columns([1,1,1])
with cols[0]:
    container = st.container(border=True)
    container.write("Review dari pelanggan")
with cols[1]:
    container = st.container(border=True)
    container.write("Review dari pelanggan")
with cols[2]:
    container = st.container(border=True)
    container.write("Review dari pelanggan")
st.text('')
st.text('')

cols = st.columns([1,1.3])
with cols[0]:
    st.markdown("<h1 style='text-align: left; font-size: 15px;'>UMKMPriority</h1>", unsafe_allow_html=True)
with cols[1]:
    review = st.chat_input("Say something")
st.divider()
cols = st.columns([1,1,1,1])
with cols[0]:
    st.write('**Contact Us**')
    st.write('Twenty One')
    st.write('Twenty One')
    st.write('Twenty One')
    st.write('Twenty One')
with cols[1]:
    st.write('**Column Two**')
    st.write('Twenty One')
    st.write('Twenty One')
    st.write('Twenty One')
    st.write('Twenty One')
with cols[2]:
    st.write('**Column Three**')
    st.write('Twenty One')
    st.write('Twenty One')
    st.write('Twenty One')
    st.write('Twenty One')
with cols[3]:
    st.write('**Available On**')
    st.write(
                """
                <div style='text-align: left'>
                    <a href="https://www.apple.com/app-store/" target="_blank" style="margin-right: 10px;">
                        <img src="https://upload.wikimedia.org/wikipedia/commons/6/67/App_Store_%28iOS%29.svg" width="30" alt="Download on the App Store">
                    </a>
                    <a href="https://play.google.com/store" target="_blank">
                        <img src="https://upload.wikimedia.org/wikipedia/commons/7/78/Google_Play_Store_badge_EN.svg" width="100" alt="Get it on Google Play">
                    </a>
                </div>
                """, 
                unsafe_allow_html=True
            )
    st.text('')
    st.write('**Join Us**')
    st.write(
                """
                <div style='text-align: left;'>
                    <a href="https://www.facebook.com" target="_blank" style="margin-right: 10px;">
                        <img src="https://upload.wikimedia.org/wikipedia/commons/5/51/Facebook_f_logo_%282019%29.svg" width="30" alt="Facebook">
                    </a>
                    <a href="https://www.youtube.com" target="_blank" style="margin-right: 10px;">
                        <img src="https://upload.wikimedia.org/wikipedia/commons/4/42/YouTube_icon_%282013-2017%29.png" width="30" alt="YouTube">
                    </a>
                    <a href="https://www.instagram.com" target="_blank" style="margin-right: 10px;">
                        <img src="https://upload.wikimedia.org/wikipedia/commons/a/a5/Instagram_icon.png" width="30" alt="Instagram">
                    </a>
                    <a href="https://www.linkedin.com" target="_blank">
                        <img src="https://upload.wikimedia.org/wikipedia/commons/0/01/LinkedIn_Logo.svg" width="50" alt="LinkedIn">
                    </a>
                </div>
                """, 
                unsafe_allow_html=True
            )
    st.write("")
st.divider()
st.markdown("<h1 style='text-align: left; font-size: 15px; font-weight: normal;'>Copyright © 2024 UMKMPriority. All rights reserved.</h1>", unsafe_allow_html=True)