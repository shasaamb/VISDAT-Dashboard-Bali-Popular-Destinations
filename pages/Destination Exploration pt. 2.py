import pandas as pd
import streamlit as st
import plotly.express as px

# Set page configuration
st.set_page_config(page_title="Exploration 2", page_icon="🌍")

st.markdown("# Bali Tourist Distribution Rating Destination Map Exploration")
st.write("Peta interaktif di bawah ini menampilkan distribusi peringkat Google Maps dari destinasi wisata populer di Bali. Anda dapat melihat informasi lebih lanjut dengan mengarahkan kursor ke titik pada peta.")

# Load data
@st.cache_data
def load_data():
    df = 'Bali Popular Destination for Tourist 2022.csv'
    data = pd.read_csv(df)
    return data

data = load_data()

# Define the coordinates for each place
places_data = [
    {"place": "Tanah Lot", "lat": -8.6212, "lon": 115.0868},
    {"place": "Mount Batur", "lat": -8.2389, "lon": 115.3775},
    {"place": "Uluwatu Temple", "lat": -8.8291, "lon": 115.0849},
    {"place": "Ubud Monkey Forest", "lat": -8.5194, "lon": 115.2606},
    {"place": "Goa Gajah", "lat": -8.5069, "lon": 115.2625},
    {"place": "Jatiluwih Rice Terraces", "lat": -8.3686, "lon": 115.1305},
    {"place": "Tenggalang Rice Terrace", "lat": -8.4028, "lon": 115.2880},
    {"place": "Pura Ulun Danu Bratan", "lat": -8.2753, "lon": 115.1664},
    {"place": "Seminyak Beach", "lat": -8.6913, "lon": 115.1682},
    {"place": "Nusa Dua Beach", "lat": -8.7941, "lon": 115.2302},
    {"place": "Besakih Temple (Pura Besakih)", "lat": -8.3739, "lon": 115.4522},
    {"place": "Kuta Beach", "lat": -8.7185, "lon": 115.1686},
    {"place": "Pura Penataran Agung Lempuyang", "lat": -8.3915, "lon": 115.6315},
    {"place": "Sidemen Valley", "lat": -8.4845, "lon": 115.4442},
    {"place": "Tirta Empul Temple", "lat": -8.4070, "lon": 115.3155},
    {"place": "West Bali National Park", "lat": -8.1333, "lon": 114.4833},
    {"place": "Garuda Wisnu Kencana Cultural Park", "lat": -8.8104, "lon": 115.1676},
    {"place": "Bali Zoo", "lat": -8.5913, "lon": 115.2659},
    {"place": "Bali Bird Park", "lat": -8.6000, "lon": 115.2500},
    {"place": "Tirta Gangga", "lat": -8.4123, "lon": 115.5873},
    {"place": "Tegenungan Waterfall", "lat": -8.5754, "lon": 115.2888},
    {"place": "Bali Swing", "lat": -8.4939, "lon": 115.2346},
    {"place": "Waterboom Bali", "lat": -8.7286, "lon": 115.1694},
    {"place": "Campuhan Ridge Walk", "lat": -8.5059, "lon": 115.2538},
    {"place": "Bali Safari and Marine Park", "lat": -8.5904, "lon": 115.2946},
    {"place": "Bajra Sandhi Monument", "lat": -8.6717, "lon": 115.2339},
    {"place": "Sukawati Art Market", "lat": -8.5965, "lon": 115.2826},
    {"place": "Taman Ujung", "lat": -8.4631, "lon": 115.6307},
    {"place": "Secret Garden Village", "lat": -8.3727, "lon": 115.1933},
    {"place": "Penglipuran Village", "lat": -8.4217, "lon": 115.2747},
    {"place": "Banjar Hot Spring", "lat": -8.2105, "lon": 114.9671},
    {"place": "Bali Pulina", "lat": -8.4227, "lon": 115.2788},
    {"place": "Goa Lawah Temple", "lat": -8.5516, "lon": 115.4688},
    {"place": "Pantai Batu Bolong", "lat": -8.6595, "lon": 115.1301}
]

# Create a DataFrame for places_data
places_df = pd.DataFrame(places_data)

# Merge data with places_df based on place name
data = data.merge(places_df, how='left', left_on='Place', right_on='place')

# Drop the redundant 'place' column
data.drop('place', axis=1, inplace=True)

# Plot interactive map using Plotly Express
fig_map = px.scatter_mapbox(data, lat='lat', lon='lon',
                            hover_name='Place', hover_data=['Description', 'Tourism/Visitor Fee (approx in USD)'],
                            color='Google Maps Rating', size='Google Maps Rating',
                            color_continuous_scale=px.colors.cyclical.IceFire, size_max=15, zoom=8)
fig_map.update_layout(mapbox_style="open-street-map")
fig_map.update_layout(margin={"r":0,"t":0,"l":0,"b":0})

# Display the interactive map
st.plotly_chart(fig_map)
