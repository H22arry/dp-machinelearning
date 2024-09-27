import streamlit as st
import pandas as pd 
st.title('🎈 Machine Learning')

with st.expander('**Data**'):
  st.write('**Raw Data**')
  df = pd.read_csv('https://raw.githubusercontent.com/dataprofessor/data/refs/heads/master/penguins_cleaned.csv')
  df

  st.write('**X**')
  X = df.drop('species',axis = 1)
  X

  st.write('**Y**')
  y = df.species
  y

with st.expander('**Data visualization**'):
  st.scatter_chart(data=df, x='bill_length_mm',y='body_mass_g',color='species') 

# Data Preparation
with st.sidebar:
  st.header('Input Features')
