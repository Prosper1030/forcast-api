import streamlit as st
import pandas as pd

st.header("Weather Forcast Cast for the next Days")
place = st.text_input("Place: ")
days = st.slider("forcast Days", min_value=1, max_value=5,
                 help="Select a number of forecasted days")
option = st.selectbox("Select data to view",
                      ("Temperature", "Sky"))
st.subheader(f"{option} for the next {days} days in {place}")
