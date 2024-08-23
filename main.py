import streamlit as st
import plotly.express as px
from backend import get_data

st.header("Weather Forcast Cast for the next Days")
place = st.text_input("Place: ")
days = st.slider("forcast Days", min_value=1, max_value=5,
                 help="Select a number of forecasted days")
option = st.selectbox("Select data to view",
                      ("Temperature", "Sky"))

st.subheader(f"{option} for the next {days} days in {place}")

if place:
    try:
        filtered_data = get_data(place, days)
        if option == "Temperature":
            temperatures = [dict["main"]["temp"]/10 for dict in filtered_data]
            dates = [dict["dt_txt"] for dict in filtered_data]
            figure = px.line(x=dates, y=temperatures, labels={"x": "Date ", "y": "Temperature (C)"})
            st.plotly_chart(figure)

        if option == "Sky":
            images = {"Clear": "images/clear.png", "Clouds": "images/cloud.png",
                      "Rain": "images/rain.png", "Snow": "images/snow.png"}
            sky_conditions = [dict["weather"][0]["main"] for dict in filtered_data]
            image_path = [images[condition] for condition in sky_conditions]
            st.image(image_path, width=115)
    except KeyError:
        st.write("The place is not exist")
