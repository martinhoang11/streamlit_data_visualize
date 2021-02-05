import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import altair as alt
from matplotlib.pyplot import figure

#css
st.markdown('<style>h1{color: red;}</style>', unsafe_allow_html=True)

#function
@st.cache(allow_output_mutation=True)
def load_data(url):
    data = pd.read_excel(url)
    return data

#sidebar settings
st.sidebar.subheader('Configure Settings')

#Moigioi
st.title('Moi gioi data visualize')

#data url
data_url = ('C:/Users/huynh14/fina/moigioi_clean.xlsx')

#load data
data = load_data(data_url)
data = data.iloc[:, 3:]

#write info
st.write(f'Number of samples: {len(data)}')

#show data
if st.checkbox('Show raw data'):
    st.subheader('MG data')
    st.dataframe(data)

#side bar data
st.sidebar.subheader('Moi gioi config')
add_selectbox = st.sidebar.selectbox(
    'Which columns you want to show',
    (data.columns)
)
# Add a slider to the sidebar:
show_range = st.sidebar.slider(
    'Select a range of values',
    0.0, 100.0, (25.0, 75.0)
)

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

#write info
st.write(f'Number of samples: {len(vn_bank_data)}')

#side bar vn_bank
st.sidebar.subheader('Vietnam bank config')
add_selectbox = st.sidebar.selectbox(
    'Which columns you want to show',
    (vn_bank_data.columns)
)
#range
show_range = st.sidebar.slider(
    'Select a VN range of values',
    0.0, 100.0, (25.0, 75.0)
)

#website
st.subheader('No. of post from website: ')
fig_website = vn_bank_data['Website'].value_counts()
st.bar_chart(fig_website, width=1600,height=500)

#city_clean
st.subheader('Most popular cities: ')
fig_website = vn_bank_data['City_clean'].value_counts()
st.bar_chart(fig_website, width=1600,height=500)

#district
st.subheader('Most popular province: ')
fig_pro = vn_bank_data['Tinh'].value_counts()
if st.checkbox('Show province table'):
    st.write(fig_pro)
st.bar_chart(fig_pro, width=1600,height=500)

#quan_huyen
st.subheader('Most top 20 popular district: ')
fig_district = vn_bank_data['Quan_Huyen'].value_counts()[:20]
if st.checkbox('Show district table'):
    st.write(fig_district)
st.bar_chart(fig_district, width=1600,height=500)

#bat dong san
st.title('Real estate post data visualize')
bds_url = ('C:/Users/huynh14/fina/bat_dong_san_nha_dat_ban_new_crawl.xlsx')
bds_data = load_data(bds_url)
if st.checkbox('Show real-estate table'):
    st.write(bds_data)

#write info
st.write(f'Number of samples: {len(bds_data)}')

#side bar vn_bank
st.sidebar.subheader('Real estate config')
add_selectbox = st.sidebar.selectbox(
    'Which columns you want to show',
    (bds_data.columns)
)
#range
show_range = st.sidebar.slider(
    'Select a real estate range of values',
    0.0, 100.0, (25.0, 75.0)
)

#price
st.subheader('Top 20 prices')
bds_price = bds_data['Price'].value_counts()[:20]
st.bar_chart(bds_price, width=1600,height=500)

#type of post
st.subheader('No. of vip and normal post')
post_rank = bds_data['Post_rank'].value_counts()
st.bar_chart(post_rank, width=1600,height=500)

#Price-Area
st.subheader('Price with area frequency')
price_area = bds_data.groupby(["Price", "Area"]).size().reset_index(name="Time").sort_values('Time')[-20:]
st.write(price_area)
st.bar_chart(price_area)





