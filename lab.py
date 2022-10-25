import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st
plt.style.use('seaborn')
st.title('California Housing Data(1990) by Huixin Deng')
df=pd.read_csv('housing.csv')
#add a slider
house_filter = st.slider('Median House Price:', 0, 500001, 200000)
#filter by population
df = df[df.median_house_value <= house_filter]
#add a capital select filter
location_filter=st.sidebar.multiselect('choose the location type', ['NEAR BAY', '<1H OCEAN', 'INLAND', 'NEAR OCEAN', 'ISLAND'],default=['NEAR BAY', '<1H OCEAN', 'INLAND', 'NEAR OCEAN', 'ISLAND'] )
df=df[df.ocean_proximity.isin(location_filter)]
# create a input form
income = st.sidebar.radio(
     "Choose income level",
 ('Low', 'Medium', 'High'))

if income == 'Low':
   df=df[df.median_income<=2.5]
elif income=='Medium':
    df=df[df.median_income>2.5]
    df=df[df.median_income<4.5]
else:
    df=df[df.median_income>4.5]
#地图
df = df[df.median_house_value <= house_filter]
st.title('See more filters in the sidebar')
st.map(df)
#柱状图
st.title('Histogram of the Median House Value')
fig,ax=plt.subplots()
a=df.median_house_value.hist(bins=30)
st.pyplot(fig)