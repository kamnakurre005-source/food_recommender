import pandas as pd
import streamlit as st
import pickle

food_dict = pickle.load(open('food_dict.pkl','rb'))

foods =  pd.DataFrame(food_dict)

st.title('Food Recommender system')

selected_food = st.selectbox(' what do you want ?',
            foods['Food_Item'].values )

if st.button('suggest'):
    st.write(foods[foods['Food_Item'] == selected_food].head())
