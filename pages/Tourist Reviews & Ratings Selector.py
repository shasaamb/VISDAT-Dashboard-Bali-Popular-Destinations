import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Set the Streamlit deprecation option
st.set_option('deprecation.showPyplotGlobalUse', False)

st.set_page_config(page_title="Tourist Reviews & Ratings Selector", page_icon="🔍")
st.markdown("# Ulasan Google dan Peringkat Google Maps untuk Tempat Wisata Terpilih")

st.write("""
Halaman ini memungkinkan Anda untuk memilih beberapa tempat wisata populer di Bali dari daftar yang disediakan. Setelah memilih tempat-tempat tersebut, akan menampilkan jumlah ulasan dan peringkat Google Maps untuk setiap tempat yang dipilih.

Gunakan multiselect dropdown di bawah ini untuk memilih tempat-tempat yang ingin Anda lihat:
""")

# Load data
@st.cache_data
def load_data():
    df = 'Bali Popular Destination for Tourist 2022.csv'
    data = pd.read_csv(df)
    return data

data = load_data()

# List semua tempat wisata di Bali
list_of_places = [
    "Tanah Lot", "Mount Batur", "Uluwatu Temple", "Ubud Monkey Forest",
    "Goa Gajah", "Jatiluwih Rice Terraces in Bali", "Tenggalang Rice Terrace",
    "Pura Ulun Danu Bratan", "Seminyak Beach", "Nusa Dua Beach", "Besakih Temple (Pura Besakih)",
    "Kuta Beach", "Pura Penataran Agung Lempuyang", "Sidemen Valley", "Tirta Empul Temple",
    "West Bali National Park", "Garuda Wisnu Kencana Cultural Park", "Bali Zoo", "Bali Bird Park",
    "Tirta Gangga", "Tegenungan Waterfall", "Bali Swing", "Waterboom Bali", "Campuhan Ridge Walk",
    "Bali Safari and Marine Park", "Bajra Sandhi Monument", "Sukawati Art Market", "Taman Ujung",
    "Secret Garden Village", "Penglipuran Village", "Banjar Hot Spring", "Bali Pulina",
    "Goa Lawah Temple", "Pantai Batu Bolong"
]

# Pilih tempat
selected_places = st.multiselect("Pilih tempat", list_of_places)

# Filter data berdasarkan tempat yang dipilih
selected_data = data[data['Place'].isin(selected_places)]

if not selected_data.empty:
    # Tampilkan ulasan Google dan peringkat Google Maps
    st.write(selected_data[['Place', 'Google Reviews (Count)', 'Google Maps Rating']])

    # Plot barplot untuk ulasan Google
    plt.figure(figsize=(6, 5))
    sns.barplot(data=selected_data, y='Place', x='Google Reviews (Count)', color='skyblue')
    plt.title('Ulasan Google untuk Tempat Wisata Terpilih')
    plt.xlabel('Jumlah Ulasan')
    plt.ylabel('Tempat')
    plt.xticks(rotation=45)
    fig_reviews = plt.gcf()  # Get the current figure

    # Plot barplot untuk peringkat Google Maps
    plt.figure(figsize=(6, 5))
    sns.barplot(data=selected_data, y='Place', x='Google Maps Rating', color='salmon')
    plt.title('Peringkat Google Maps untuk Tempat Wisata Terpilih')
    plt.xlabel('Rating')
    plt.ylabel('Tempat')
    plt.xticks(rotation=45)
    fig_rating = plt.gcf()  # Get the current figure

    # Display the figures using st.pyplot()
    st.pyplot(fig_reviews)
    st.pyplot(fig_rating)
else:
    st.warning("Silakan pilih tempat terlebih dahulu.")
