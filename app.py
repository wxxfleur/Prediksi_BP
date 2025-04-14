import streamlit as st
import pandas as pd
import joblib
import datetime

# Load model
model = joblib.load('model_rf_harga.pkl')

st.title("📈 Prediksi Harga Komoditas Harian")
st.write("Masukkan detail pasar dan waktu untuk prediksi harga bahan pokok.")

# Input fitur (kamu bisa sesuaikan dengan fitur sebenarnya)
provinsi = st.text_input("Provinsi")
kab_kota = st.text_input("Kabupaten/Kota")
nama_pasar = st.text_input("Nama Pasar")
nama_komoditas = st.text_input("Nama Komoditas (Variant)")
tanggal = st.date_input("Tanggal", value=datetime.date.today())

# Konversi input ke dataframe sesuai format pelatihan model
if st.button("Prediksi Harga"):
    # Simpan input jadi dataframe
    input_df = pd.DataFrame([{
        "Provinsi": provinsi,
        "Kabupaten/Kota": kab_kota,
        "Nama Pasar": nama_pasar,
        "Nama Variant": nama_komoditas,
        "Tanggal": tanggal.strftime('%Y-%m-%d')
    }])
    
    # Pra-pemrosesan harus disesuaikan dengan data pelatihan
    # Misal ubah ke fitur numerik/datetime dan encode kategori
    # Di sini kita asumsikan fitur sudah cocok

    # Prediksi harga
    prediksi = model.predict(input_df)[0]
    st.success(f"Prediksi Harga: Rp {prediksi:,.2f}")

Add app.py for price prediction
