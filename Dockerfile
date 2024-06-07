# Gunakan image dasar yang berisi Python
FROM python:3.9-slim

# Set lingkungan kerja di dalam container
WORKDIR /app

# Salin requirements.txt ke dalam container
COPY requirements.txt .

# Install dependencies
RUN pip install -r requirements.txt

# Salin seluruh kode aplikasi ke dalam container
COPY . .

# Tentukan port yang digunakan oleh Streamlit
EXPOSE 8501

# Jalankan aplikasi Streamlit
CMD ["streamlit", "run", "Home.py", "--server.port=8501"]