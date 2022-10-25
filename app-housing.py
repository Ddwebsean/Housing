import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
plt.style.use('seaborn')


st.title('California Housing Data(1990) by Huixin Deng')
df = pd.read_csv('housing.csv')

price_filter = st.slider('Median house price:', 0, 500001, 200000)  # min, max, default

# filter by price
df = df[df.median_house_value <= price_filter]

# create a multi select
location_filter = st.sidebar.multiselect(
     'Choose the location type',
     df.ocean_proximity.unique(),  # options
     df.ocean_proximity.unique())  # defaults


df=df[df.median_income.isin(location_filter) ]

genre = st.sidebar.radio(
    "Choose income level",
    ('Low', 'Medium', 'High'))
if genre == 'Low':
    df=df[df['median_income']<=2.5]
    
elif genre == 'Medium':
    df =df[(df['median_income']>2.5)&(df['median_income']<4.5)]
    
else:
    df=df[df['median_income']>=4.5]

# show on map
st.map(df)

# show the plot
st.subheader('Histogram of the Median House Value')
fig, ax = plt.subplots(figsize=(20, 15))
df.median_house_value.hist(bins=30)
st.pyplot(fig)