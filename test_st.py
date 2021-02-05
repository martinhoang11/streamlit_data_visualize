import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import altair as alt
from matplotlib.pyplot import figure

st.title('Fina data visualize')

data_url = ('C:/Users/huynh14/fina/moigioi_clean.xlsx')

@st.cache(allow_output_mutation=True)
def load_data():
    data = pd.read_excel(data_url)
    return data

add_selectbox = st.selectbox(
    'How would you like to be contacted?',
    ('Email', 'Home phone', 'Mobile phone')
)

# Add a slider to the sidebar:
show_range = add_slider = st.slider(
    'Select a range of values',
    0.0, 100.0, (25.0, 75.0)
)
st.write(f"- Range choose: {show_range}")


#load data
data_load_state = st.text('Loading data...')
data = load_data()
data = data.iloc[:, 3:]
data_load_state.text('Loading data...done!')

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
# st.set_option('deprecation.showPyplotGlobalUse', False) 