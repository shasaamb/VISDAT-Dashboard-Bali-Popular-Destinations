import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st

st.set_page_config(page_title="Distribution of Tourist Rating", page_icon="⭐")

st.markdown("# Distribution of Tourist Rating")
st.write("""
Halaman ini menampilkan diagram lingkaran interaktif yang menunjukkan distribusi peringkat Google Maps dari destinasi wisata populer di Bali. Anda dapat memasukkan rentang peringkat yang ingin Anda lihat dalam diagram lingkaran.

Format rentang: min_rating-max_rating (misal: 4.0-4.5)
""")

# Load data
@st.cache_data
def load_data():
    df = 'Bali Popular Destination for Tourist 2022.csv'
    data = pd.read_csv(df)
    return data

data = load_data()

# Input rentang peringkat dari pengguna
rating_range = st.text_input("Masukkan Rentang Peringkat (Format: min_rating-max_rating)", "4.0-5.0")

# Memecah rentang peringkat menjadi min_rating dan max_rating
try:
    min_rating, max_rating = map(float, rating_range.split("-"))
except ValueError:
    st.error("Format rentang tidak valid. Silakan masukkan kembali dengan format yang benar.")
    st.stop()

# Filter data berdasarkan rentang peringkat yang dimasukkan
filtered_data = data[(data['Google Maps Rating'] >= min_rating) & (data['Google Maps Rating'] <= max_rating)]

# Plotting the distribution
rating_ranges = pd.cut(filtered_data['Google Maps Rating'], bins=[4.0, 4.2, 4.4, 4.6, 4.8, 5.0], include_lowest=True)
rating_distribution = rating_ranges.value_counts().sort_index()

fig, ax = plt.subplots(figsize=(10, 8))  # Create a figure and axis
ax.pie(rating_distribution, labels=rating_distribution.index, autopct='%1.1f%%', colors=sns.color_palette('coolwarm', len(rating_distribution)))
ax.set_title(f'Distribution of Google Maps Ratings ({rating_range})')

# Display the plot using Streamlit
st.pyplot(fig)
