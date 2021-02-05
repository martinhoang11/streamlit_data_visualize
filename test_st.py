import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import altair as alt
from matplotlib.pyplot import figure

#function
@st.cache(allow_output_mutation=True)
def load_data(url):
    data = pd.read_excel(url)
    return data

#sidebar settings
st.sidebar.subheader('Configure Settings')
add_selectbox = st.sidebar.selectbox(
    'How would you like to be contacted?',
    ('Email', 'Home phone', 'Mobile phone')
)

# Add a slider to the sidebar:
show_range = st.sidebar.slider(
    'Select a range of values',
    0.0, 100.0, (25.0, 75.0)
)


#Moigioi
st.title('Moi gioi data visualize')

#data url
data_url = ('C:/Users/huynh14/fina/moigioi_clean.xlsx')

#load data
data = load_data(data_url)
data = data.iloc[:, 3:]

#show data
if st.checkbox('Show raw data'):
    st.subheader('MG data')
    st.dataframe(data)

#website visualize
st.subheader('No. of post from website: ')
fig_website = data['Webiste'].value_counts()
st.bar_chart(fig_website, width=1600,height=500)

#email visualize
st.subheader('No. of (in)valid email: ')
email_dict = {'Valid': 0, 'Not_valid': 0}
for phone in data['Email']:
    if phone == 'Khong Co':
        email_dict['Not_valid'] += 1
    else:
        email_dict['Valid'] += 1

st.bar_chart(pd.DataFrame(pd.Series(email_dict).to_frame()), width=1600,height=500)

#City visualize
st.subheader('Top 10 cities for Moi Gioi: ')
fig_website = data['City_clean'].value_counts().sort_values()[-10:]
if st.checkbox('Show data'):
    st.write(fig_website)
st.bar_chart(fig_website, width=1600,height=500)


#Vietnam_bank
st.title('Vietnam Bank post data visualize')
vn_bank_url = ('C:/Users/huynh14/fina/vietnam_bank_amc.xlsx')
vn_bank_data = load_data(vn_bank_url)

st.subheader('No. of post from website: ')
fig_website = vn_bank_data['Website'].value_counts()
st.bar_chart(fig_website, width=1600,height=500)