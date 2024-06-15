import pandas as pd
import folium
import streamlit as st
from streamlit_folium import folium_static

# Display the map using Streamlit
st.set_page_config(page_title="Exploration 1", page_icon="🗺️")
st.markdown("# Bali Tourist Destination Map Exploration pt. 1")
st.markdown("Peta ini menampilkan destinasi wisata populer di Bali.")
st.markdown("Setiap penanda menunjukkan sebuah tempat dengan peringkat dan jumlah ulasan yang diberikan.")

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

# Define ratings and reviews data
ratings_reviews = {
    "Tanah Lot": {"rating": 4.6, "reviews": 75899},
    "Mount Batur": {"rating": 4.5, "reviews": 2580},
    "Uluwatu Temple": {"rating": 4.6, "reviews": 28800},
    "Ubud Monkey Forest": {"rating": 4.5, "reviews": 36099},
    "Goa Gajah": {"rating": 4.2, "reviews": 6683},
    "Jatiluwih Rice Terraces": {"rating": 4.7, "reviews": 7798},
    "Tenggalang Rice Terrace": {"rating": 4.4, "reviews": 33732},
    "Pura Ulun Danu Bratan": {"rating": 4.7, "reviews": 29178},
    "Seminyak Beach": {"rating": 4.5, "reviews": 3195},
    "Nusa Dua Beach": {"rating": 4.6, "reviews": 6171},
    "Besakih Temple (Pura Besakih)": {"rating": 4.5, "reviews": 9672},
    "Kuta Beach": {"rating": 4.5, "reviews": 37663},
    "Pura Penataran Agung Lempuyang": {"rating": 4.3, "reviews": 6192},
    "Sidemen Valley": {"rating": 4.3, "reviews": 172},
    "Tirta Empul Temple": {"rating": 4.6, "reviews": 16456},
    "West Bali National Park": {"rating": 4.5, "reviews": 2912},
    "Garuda Wisnu Kencana Cultural Park": {"rating": 4.5, "reviews": 50703},
    "Bali Zoo": {"rating": 4.4, "reviews": 14401},
    "Bali Bird Park": {"rating": 4.6, "reviews": 9847},
    "Tirta Gangga": {"rating": 4.6, "reviews": 12992},
    "Tegenungan Waterfall": {"rating": 4.3, "reviews": 23349},
    "Bali Swing": {"rating": 4.5, "reviews": 8311},
    "Waterboom Bali": {"rating": 4.7, "reviews": 10650},
    "Campuhan Ridge Walk": {"rating": 4.4, "reviews": 9019},
    "Bali Safari and Marine Park": {"rating": 4.4, "reviews": 16042},
    "Bajra Sandhi Monument": {"rating": 4.6, "reviews": 12694},
    "Sukawati Art Market": {"rating": 4.3, "reviews": 8248},
    "Taman Ujung": {"rating": 4.6, "reviews": 3984},
    "Secret Garden Village": {"rating": 4.6, "reviews": 4432},
    "Penglipuran Village": {"rating": 4.8, "reviews": 13207},
    "Banjar Hot Spring": {"rating": 4.3, "reviews": 2422},
    "Bali Pulina": {"rating": 4.5, "reviews": 3960},
    "Goa Lawah Temple": {"rating": 4.7, "reviews": 4479},
    "Pantai Batu Bolong": {"rating": 4.4, "reviews": 7248},
}

# Create a DataFrame from places_data
places_df = pd.DataFrame(places_data)

# Add ratings and reviews to the DataFrame
places_df["rating"] = places_df["place"].map(lambda x: ratings_reviews[x]["rating"])
places_df["reviews"] = places_df["place"].map(lambda x: ratings_reviews[x]["reviews"])

# Create the map centered around Bali
bali_map = folium.Map(location=[-8.4095, 115.1889], zoom_start=9)

# Add markers for each place
for index, row in places_df.iterrows():
    label = f'Place: {row["place"]}, Rating: {row["rating"]}, Reviews: {row["reviews"]}'
    folium.Marker(
        [row["lat"], row["lon"]],
        popup=label,
        icon=folium.Icon(color="blue")
    ).add_to(bali_map)

# Convert Folium map to HTML
folium_static(bali_map)
