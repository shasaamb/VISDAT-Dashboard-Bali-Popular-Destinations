import pandas as pd
import plotly.express as px
import streamlit as st

st.set_page_config(page_title="Tourist Ratings Explorer", page_icon="⭐")

st.markdown("# Tourist Ratings Explorer")
st.write("""
Halaman ini menampilkan diagram batang interaktif yang menunjukkan peringkat Google Maps dari destinasi wisata populer di Bali. Pengguna dapat memilih rentang peringkat (rating) dengan menggunakan slider "Min Rating" dan "Max Rating" yang ada dibawah.

Dengan menggunakan slider tersebut, pengguna dapat mengatur rentang peringkat yang ingin ditampilkan pada diagram batang. Diagram batang akan secara otomatis memperbarui dirinya untuk menampilkan destinasi wisata yang memiliki peringkat sesuai dengan rentang yang dipilih.

Tujuan dari halaman ini adalah memberikan pengalaman eksplorasi yang interaktif dan informatif mengenai peringkat Google Maps dari destinasi wisata di Bali. Pengguna dapat melihat dan membandingkan peringkat destinasi wisata untuk membuat keputusan yang lebih baik dalam merencanakan perjalanan mereka di Bali.
""")


# Load data
@st.cache_data
def load_data():
    df = 'Bali Popular Destination for Tourist 2022.csv'
    data = pd.read_csv(df)
    return data

data = load_data()

bar_chart_data = data[['Place', 'Google Maps Rating', 'Google Reviews (Count)']].sort_values(by='Google Maps Rating', ascending=False)

min_rating = st.slider('Min Rating', float(bar_chart_data['Google Maps Rating'].min()),
                       float(bar_chart_data['Google Maps Rating'].max()), float(bar_chart_data['Google Maps Rating'].min()))
max_rating = st.slider('Max Rating', float(bar_chart_data['Google Maps Rating'].min()),
                       float(bar_chart_data['Google Maps Rating'].max()), float(bar_chart_data['Google Maps Rating'].max()))

filtered_data = bar_chart_data[(bar_chart_data['Google Maps Rating'] >= min_rating) &
                               (bar_chart_data['Google Maps Rating'] <= max_rating)]
fig_bar = px.bar(filtered_data, x='Place', y='Google Maps Rating',
                 title='Google Maps Ratings of Bali Tourist Destinations',
                 labels={'Place': 'Tourist Destination', 'Google Maps Rating': 'Rating'},
                 hover_data=['Google Maps Rating', 'Google Reviews (Count)'])
st.plotly_chart(fig_bar)



