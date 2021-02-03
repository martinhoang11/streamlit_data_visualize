import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

st.title('Fina data visualize')

data_url = ('C:/Users/huynh14/fina/moigioi_clean.xlsx')

@st.cache
def load_data(nrows):
    data = pd.read_excel(data_url, nrows=nrows)
    return data

#load data
data_load_state = st.text('Loading data...')
data = load_data(500)
data_load_state.text('Loading data...done!')

#show data
if st.checkbox('Show raw data'):
    st.subheader('MG data')
    st.dataframe(data)

#draw histogram
st.subheader('Number of email')
hist_val = np.histogram(
    data['Email'].value_counts().sort_index()
)
st.bar_chart(hist_val)

#draw histogram
st.subheader('Number of city')
hist_val = data['City_clean'].plot(kind='bar')
st.bar_chart(hist_val)

# #draw map data
# st.subheader('Map data')
# st.map(data)