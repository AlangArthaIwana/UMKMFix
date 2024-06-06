import streamlit as st
import pandas as pd
import hashlib

# Fungsi untuk hash password
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

# Fungsi untuk memeriksa kredensial
def check_credentials(username, password, users_df):
    hashed_password = hash_password(password)
    user_row = users_df[(users_df['username'] == username) & (users_df['password'] == hashed_password)]
    return not user_row.empty

# Fungsi untuk menambah pengguna baru
def add_user(username, password, users_df, users_file):
    if username in users_df['username'].values:
        st.error('Username sudah ada. Gunakan username lain.')
    else:
        hashed_password = hash_password(password)
        new_user = pd.DataFrame({'username': [username], 'password': [hashed_password]})
        new_user.to_csv(users_file, mode='a', header=False, index=False)
        st.success('Registrasi berhasil. Anda sekarang dapat masuk.')

# Baca data pengguna dari file CSV
users_file = 'users.csv'
try:
    users_df = pd.read_csv(users_file)
except FileNotFoundError:
    users_df = pd.DataFrame(columns=['username', 'password'])

# # Tampilan Sign In dan Sign Up
st.title('Selamat Datang di UMKMPriority')

menu = st.radio('',options=['Sign In', 'Sign Up'], horizontal=True)

if menu == 'Sign In':
    st.subheader('Sign In')
    username = st.text_input('Username')
    password = st.text_input('Password', type='password')
    if st.button('Sign In'):
        if check_credentials(username, password, users_df):
            st.success('Sign In berhasil!')
            # if st.button("Home"):
            st.switch_page("Home.py")
        else:
            st.error('Username atau password salah.')

elif menu == 'Sign Up':
    st.subheader('Sign Up')
    username = st.text_input('Username')
    password = st.text_input('Password', type='password')
    if st.button('Sign Up'):
        add_user(username, password, users_df, users_file)

