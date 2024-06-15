import streamlit as st

# Atur konfigurasi halaman
st.set_page_config(
    page_title="Introduction",
    page_icon="👋",
)

# Tampilkan judul dan deskripsi
st.write("# Tugas Besar Visualisasi Data")

st.sidebar.success("Select a demo above.")

st.markdown(
    """
    Selamat datang di website visualisasi kami! 👋
    Kami adalah kelompok yang terdiri dari:

    1. **Chairunnisa Mahadewi** (1301213104)
    2. **Kamelia Khoirunnisa** (1301213070)
    3. **Ashiva Prameswara** (1301213134)
    4. **Andini Aprilia Putri** (1301210545)
    5. **Annisa Rahma** (1301213011)

    ### Deskripsi Data

    Data yang kami gunakan berasal dari [Bali Popular Destination for Tourist 2022](https://www.kaggle.com/datasets/fuarresvij/bali-popular-destination-for-tourist-2022) yang diambil dari Kaggle. 
    Dataset ini berisi informasi tentang destinasi populer di Bali untuk para wisatawan pada tahun 2022. Beberapa kolom penting dalam dataset ini antara lain:

    - **Place**: Nama tempat wisata di Bali.
    - **Location**: Lokasi tempat wisata.
    - **Google Maps Rating**: Peringkat tempat wisata di Google Maps.
    - **Google Reviews (Count)**: Jumlah ulasan dari pengguna di Google.

    ### Tujuan

    Kami menggunakan dataset ini untuk melakukan analisis dan visualisasi terkait destinasi populer di Bali serta menampilkan informasi yang berguna bagi pengguna yang ingin mengetahui lebih banyak tentang tempat-tempat wisata tersebut.
    """
)
